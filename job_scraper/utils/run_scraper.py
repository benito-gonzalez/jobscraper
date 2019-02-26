# -*- coding: utf-8 -*-
import os
import random

from job_scraper.utils import request_support
from job_scraper.utils import scraper
from job_scraper.utils import db_support
from job_scraper.utils import log_support
from job_scraper.utils.locator import CityLocator

my_path = os.path.abspath(os.path.dirname(__file__))
FILENAME = os.path.join(my_path, "servers.txt")

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/secretkey.txt'):
    PRODUCTION_ENV = True
else:
    PRODUCTION_ENV = False


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
    return db_job.title == scraped_job.title and db_job.company.name == scraped_job.company_name and db_job.location == scraped_job.location


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
    :return: New location and if it is valid.
    """
    location = None

    locator = CityLocator()
    if locator.is_foreign_job_location(job_location) or locator.is_foreign_job_title(title):
        location = job_location
        valid_location = False
    else:
        valid_location = True

        if locator.has_finnish_cities(job_location):
            cities = locator.get_finnish_cities(job_location)
            # If location is "Finland" and the title has a specific Finnish city, that city must be used.
            if len(cities) == 1 and "Finland" in cities:
                if locator.has_finnish_cities(title):
                    cities = locator.get_finnish_cities(title)
        else:
            cities = locator.get_finnish_cities(title)

        if cities:
            location = ", ".join(cities)

    return location, valid_location


def main():
    # Companies that return HTTP != 200 should not delete jobs from DB
    failed_companies = []

    servers = read_server_urls()
    scraped_jobs = []
    for server in servers:
        client = scraper.generate_instance_from_client(server.get('name'), server.get('url'))
        html = request_support.simple_get(server.get('url'))

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
                    log_support.scraper_failure(server.get('name') + str(e))
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
            scraped_job.location, valid_location = enrich_location(scraped_job.title, scraped_job.location)
            if valid_location:
                job_db = db_support.get_job_from_db(scraped_job, company)

                if job_db:
                    if not job_db.is_active:
                        db_support.enable_job(job_db)
                        if job_db.is_new:
                            db_support.update_new_job(job_db)
                else:
                    # if it does not exist
                    db_support.save_to_db(scraped_job, company)

            else:
                log_support.skipping_job_due_location(scraped_job.title, scraped_job.location, scraped_job.company_name)
        else:
            log_support.set_company_not_found(scraped_job.company_name)

    # disable jobs which no longer exist in the websites (skip jobs that belong to a company that failed)
    update_active_jobs(scraped_jobs, failed_companies)
    log_support.set_completed_scraper()


if __name__ == "__main__":
    # execute only if run as a script
    main()
