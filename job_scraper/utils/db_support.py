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
    Job.objects.create(title=job_offer.title, description=job_offer.description, location=job_offer.location, salary=job_offer.salary,
                       pub_date=job_offer.pub_date, end_date=job_offer.end_date, job_type=job_offer.job_type, highlighted=False, company=company)
    log_support.saved_job(job_offer)

def is_new_job(job_offer, company):
    """
    Checks if job already exists in DB. Two jobs are the same when they have the same title, end_date, company and job type
    :param job_offer: JofOffer instance retrieved by scrapper
    :param company: company that job belongs to
    :return: True/Fase
    """
    return not Job.objects.filter(title=job_offer.title, company=company, end_date=job_offer.end_date, job_type=job_offer.job_type).exists()
