import os
from _datetime import datetime
from pytz import timezone

my_path = os.path.abspath(os.path.dirname(__file__))
SCRAPERLOG = os.path.join(my_path, "logs/scraper.log")

zone = "Europe/Helsinki"


def get_formatted_date():
    date = datetime.now(timezone(zone)).strftime("%d-%m-%Y %H:%M:%S")
    return "[" + date + "]\t"


def set_company_not_found(company_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Company can not be retrieved from DB. '" + company_name + "' does not exist\n")
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


def updated_existent_job(job):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Updated job '{0}' from '{1}'".format(job, job.company) + " to 'is_new = False'\n")
    f.close()


def updated_active_job(job):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Updated job '{0}' from '{1}'".format(job, job.company) + " to 'is_active = True'\n")
    f.close()


def updated_end_date(job, new_end_date):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Updated end_date in job '{0}' ('{1}') to {2}".format(job, job.company, new_end_date) + "\n")
    f.close()


def scraper_failure(client_name, exception):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. '{0}' - {1}".format(client_name, exception) + "\n")
    f.close()


def set_invalid_location(client_name, job_title):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "WARNING. Could not get a valid job location from {0} client for the job {1}".format(client_name, job_title) + "\n")
    f.close()


def no_jobs_found(url):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "WARNING. No jobs retrieved from {0}".format(url) + "\n")
    f.close()


def set_invalid_dates(company, title):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "WARNING. Invalid dates scraped from the company {0} for the job {1}".format(company, title) + "\n")
    f.close()


def set_invalid_title(company):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Job title could not be scraped from company {0}".format(company) + "\n")
    f.close()


def set_invalid_description(company, title):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Job description could not be scraped from the company {0} for the job {1}".format(company, title) + "\n")
    f.close()


def set_invalid_description_url(company, title):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Description URL could not be scraped from the company {0} for the job {1}".format(company, title) + "\n")
    f.close()


def set_completed_scraper():
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "Finished scraper \n")
    f.close()


def skipping_job_due_location(title, location, company_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "INFO. Skipping job '{0}' from '{1}' because of its location '{2}'".format(title, company_name, location) + "\n")
    f.close()


def set_invalid_pagination(company_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Can not retrieve latest page from '{0}'".format(company_name) + "\n")
    f.close()


def set_invalid_json(company_name):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. Can not generate a JSON with jobs information from '{0}'".format(company_name) + "\n")
    f.close()


def set_error_message(company_name, message):
    f = open(SCRAPERLOG, 'a')
    f.write(get_formatted_date() + "ERROR. From '{0}'. {1}".format(company_name, message) + "\n")
    f.close()
