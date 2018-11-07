# -*- coding: utf-8 -*-
from job_scraper.utils import request_support
from job_scraper.utils import scraper
from job_scraper.utils import db_support
from job_scraper.utils import error_log
FILENAME = "servers.txt"


def read_server_urls():
    """
    Reads the info from servers.txt, line by line where the first word is the name and the second one its URL
    :return: An array of dicts as [{'name': A, 'url':B}]
    """
    servers = []
    lines = [line.rstrip('\n') for line in open(FILENAME)]

    for line in lines:
        if line and line[0] != "#":
            info = line.split("-")
            servers.append({'name': info[0].strip(), 'url': info[1].strip()})

    return servers


def main():
    servers = read_server_urls()
    job_offers = []
    for server in servers:
        client = scraper.generate_instance_from_client(server.get('name').lower(), server.get('url'))
        html = request_support.simple_get(server.get('url'))
        if html:
            job_offers.extend(client.extract_info(html))

    # method to validate job information

    # method to store to DB checking that job does not exist yet.
    for job in job_offers:
        company = db_support.get_company_by_name(job.company_name)
        if company:
            if db_support.is_new_job(job, company):
                db_support.save_to_db(job, company)
        else:
            error_log.set_company_not_found(job.company_name)


main()
