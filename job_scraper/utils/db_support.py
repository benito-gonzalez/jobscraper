import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webapp.settings")
django.setup()

from job_scraper.models import Company
from job_scraper.models import Job
from job_scraper.utils import log_support

def get_jobs_by_company(company):
    try:
        jobs = Job.objects.get(company_id=company)
    except Job.DoesNotExist:
        jobs = []

    return  jobs


def get_company_by_name(name):
    try:
        company = Company.objects.get(name=name)
    except Company.DoesNotExist:
        company = None

    return company


def save_to_db(job_offer, company):
    Job.objects.create(title=job_offer.title,
                       description=job_offer.description,
                       location=job_offer.location,
                       salary=job_offer.salary,
                       pub_date=job_offer.pub_date,
                       end_date=job_offer.end_date,
                       job_type=job_offer.job_type,
                       is_highlighted=False,
                       company=company,
                       job_url=job_offer.url,
                       is_active=True)

    log_support.saved_job(job_offer)


def is_new_job(scraped_job, company):
    """
    Checks if job already exists in DB. Two jobs are the same when they have the same title, end_date, company and job type
    :param scraped_job: instance retrieved by scrapper
    :param company: company that job belongs to
    :return: True/Fase
    """
    return not Job.objects.filter(title=scraped_job.title, company=company, location=scraped_job.location, is_active=True).exists()


def get_active_jobs():
    """
    Get a list of jobs that are active.
    :return: QuerySet<Job> with the list of jobs
    """
    return Job.objects.filter(is_active=True)


def disable_job(job):
    """
    :param job: job to be updated
    :type job: Job
    :return: None
    """
    job.is_active = False
    job.save()
    log_support.disabled_job(job)
