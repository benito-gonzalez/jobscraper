# -*- coding: utf-8 -*-
from job_scraper.utils import request_support
from job_scraper.utils import scraper


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
            info = line.split()
            servers.append({'name': info[0], 'url': info[1]})

    return servers


def main():
    servers = read_server_urls()
    jobs = []
    for server in servers:
        client = scraper.generate_instance_from_client(server.get('name').lower(), server.get('url'))
        html = request_support.simple_get(server.get('url'))
        if html:
            jobs.extend(client.extract_info(html))

    # method to validate job information

    # method to store to DB checking that job does not exist yet.
    for job in jobs:
        print(job)


main()
