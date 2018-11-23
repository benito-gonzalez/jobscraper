from _datetime import datetime
from pytz import timezone


SCRAPERLOG = "logs/scraper.log"
zone = "Europe/Helsinki"


def get_formatted_date():
    date = datetime.now(timezone(zone)).strftime("%d-%m-%Y %H:%M:%S")
    return "[" + date + "]\t"


def set_company_not_found(company_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Company can not be retrieved from DB. '" + company_name + "' does not exist\n")
    f.close()


def set_invalid_request(url, e):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Invalid requests to {0} : {1}".format(url, str(e)) + "\n")
    f.close()


def set_invalid_response(url, status_code):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Invalid response from {0} HTTP {1}".format(url, status_code) + "\n")
    f.close()


def saved_job(job_offer):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Saving job {0}".format(job_offer) + "\n")
    f.close()


def request_url(url):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Getting jobs from {0}".format(url) + "\n")
    f.close()


def log_extract_info(client_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Extracting information from {0}".format(client_name) + "\n")
    f.close()


def disabled_job(job):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Updated job '{0}' from '{1}'".format(job, job.company) + " to 'is_active = False'\n")
    f.close()


def scraper_failure(client_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Invalid information from {0}".format(client_name) + "\n")
    f.close()


def set_invalid_location(client_name, job_title):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Could not get a valid job location from {0} client for the job {1}".format(client_name, job_title) + "\n")
    f.close()


def no_jobs_found(url):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "WARNING. No jobs retrieved from {0}".format(url) + "\n")
    f.close()
