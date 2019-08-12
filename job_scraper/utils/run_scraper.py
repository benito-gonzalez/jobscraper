# -*- coding: utf-8 -*-
import os
import random
import re
from collections import Counter

from job_scraper.utils import request_support
from job_scraper.utils import scraper
from job_scraper.utils import db_support
from job_scraper.utils import log_support
from job_scraper.utils.locator import CityLocator

my_path = os.path.abspath(os.path.dirname(__file__))
FILENAME = os.path.join(my_path, "servers.txt")

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/.is_development'):
    PRODUCTION_ENV = False
else:
    PRODUCTION_ENV = True


def read_server_urls():
    """
    Reads the info from servers.txt, line by line where the first word is the name and the second one its URL
    :return: An array of dicts as [{'name': A, 'url':B}]
    """
    servers = []
    lines = [line.rstrip('\n') for line in open(FILENAME)]

    for line in lines:
        if line and line[0] != "#":
            info = line.split(" - ", 1)
            servers.append({'name': info[0].strip(), 'url': info[1].strip()})

    return servers


def are_same_jobs(db_job, scraped_job):
    if db_job.title == scraped_job.title and db_job.company.name == scraped_job.company_name:
        # check same location only when title and company are the same
        cities = scraped_job.cities
        cities_db = db_support.get_job_cities_by_job(db_job)
        return Counter(cities) == Counter(cities_db)

    return False


def update_active_jobs(scraped_jobs, failed_companies):
    """
    Updates those jobs which are active and do not appear among the scraped jobs so they no longer exist in the website.
    If the company job is in 'failed_companies', skip it
    For those which no longer exit, 'is_activate' is updated to False
    :param scraped_jobs: jobs which have been found by the scraper
    :param failed_companies: array with the company names that return a HTTP Error
    :return: None
    """
    active_jobs = db_support.get_active_jobs()
    for active_job in active_jobs:
        if active_job.company.name in failed_companies:
            continue
        found = False
        for scraped_job in scraped_jobs:
            if are_same_jobs(active_job, scraped_job):
                found = True
                break
        if not found:
            db_support.disable_job(active_job)


def enrich_location(title, job_location):
    """
    Jobs which are located out of Finland are marked as invalid. If job location does not exist and title contains a Finnish city, job location is overwritten
    :param title: Job title
    :param job_location: Current job location retrieved by the scraper
    :return: If location is valid (Finnish) returns an array of model.City and valid_location=True. If is not valid it return a string with the location and valid_location=False
    """

    locator = CityLocator()
    if locator.is_foreign_job_location(job_location) or locator.is_foreign_job_title(title):
        valid_location = False
        return valid_location, job_location
    else:
        valid_location = True

        if locator.has_finnish_cities(job_location):
            cities = locator.get_finnish_cities(job_location)
            # If location is "Finland" and the title has a specific Finnish city, that city must be used.
            if len(cities) == 1 and cities[0].name == "Finland":
                if locator.has_finnish_cities(title):
                    cities = locator.get_finnish_cities(title)
        else:
            cities = locator.get_finnish_cities(title)

        return valid_location, cities


def find_whole_world(tag, description):
    # ++ is a special character in the regex. If we add r'\b' it will return nothing.
    if tag == "C++":
        matches = re.findall(r'\b' + re.escape(tag), description, flags=re.IGNORECASE)
    else:
        matches = re.findall(r'\b' + re.escape(tag) + r'\b', description, flags=re.IGNORECASE)
    return matches


def map_tag_job_descriptions(job):
    tags = db_support.get_tags()
    for tag in tags:
        # If tag and job have been already mapped skip
        mapped = db_support.is_job_tag_mapped(job, tag)
        if not mapped:
            matches = find_whole_world(tag.name, job.description)
            if matches:
                db_support.add_job_tag(job, tag, len(matches))


def map_job_location(job, cities):
    for city in cities:
        # If job and city have been already mapped skip
        mapped = db_support.is_job_location_mapped(job, city)
        if not mapped:
            db_support.add_job_location(job, city)

    # If the job no longer has one of its previous cities, that city-job must be removed from JobCityMap
    job_city_map = db_support.get_job_city_map_by_job(job)
    for job_city in job_city_map:
        found = False
        for city in cities:
            if city == job_city.city:
                found = True

        if not found:
            db_support.delete_job_city_record(job_city)


def main():
    # Companies that return HTTP != 200 should not delete jobs from DB
    failed_companies = []

    servers = read_server_urls()
    scraped_jobs = []
    for server in servers:
        client = scraper.generate_instance_from_client(server.get('name'), server.get('url'))
        try:
            html = request_support.simple_get(server.get('url'))
        except Exception as e:
            log_support.scraper_failure(server.get('name'), e)
            failed_companies.append(server.get('name'))
            continue

        if not html:
            failed_companies.append(server.get('name'))
        if client and html:
            if PRODUCTION_ENV:
                try:
                    jobs = client.extract_info(html)
                    if jobs:
                        scraped_jobs.extend(jobs)
                    else:
                        log_support.no_jobs_found(server.get('url'))
                except Exception as e:
                    log_support.scraper_failure(server.get('name'), e)
                    failed_companies.append(server.get('name'))
            else:
                jobs = client.extract_info(html)
                if jobs:
                    scraped_jobs.extend(jobs)
                else:
                    log_support.no_jobs_found(server.get('url'))

    # shuffle jobs to avoid to store them in order they were scraped
    random.shuffle(scraped_jobs)

    # method to store to DB checking that job does not exist yet.
    for scraped_job in scraped_jobs:
        company = db_support.get_company_by_name(scraped_job.company_name)
        if company:
            valid_location, scraped_job.cities = enrich_location(scraped_job.title, scraped_job.location)
            if valid_location:
                job_db = db_support.get_job_from_db(scraped_job, company)

                if job_db:
                    # update end_date in case it has changed
                    db_support.update_end_date(scraped_job, job_db)

                    if not job_db.is_active:
                        db_support.enable_job(job_db)
                        if job_db.is_new:
                            db_support.update_new_job(job_db)
                else:
                    # if it does not exist
                    job_db = db_support.save_to_db(scraped_job, company)

                # Map tags with job description
                map_tag_job_descriptions(job_db)
                map_job_location(job_db, scraped_job.cities)

            else:
                log_support.skipping_job_due_location(scraped_job.title, scraped_job.cities, scraped_job.company_name)
        else:
            log_support.set_company_not_found(scraped_job.company_name)

    # disable jobs which no longer exist in the websites (skip jobs that belong to a company that failed)
    update_active_jobs(scraped_jobs, failed_companies)
    log_support.set_completed_scraper()


if __name__ == "__main__":
    # execute only if run as a script
    main()
