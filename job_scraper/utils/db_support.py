import os
import django
from django.utils import timezone

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/secretkey.txt'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')

django.setup()

from job_scraper.models import Company  # noqa: E402
from job_scraper.models import Job  # noqa: E402
from job_scraper.utils import log_support  # noqa: E402


def get_jobs_by_company(company):
    try:
        jobs = Job.objects.get(company_id=company)
    except Job.DoesNotExist:
        jobs = []

    return jobs


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
                       is_active=True,
                       is_new=True)

    log_support.saved_job(job_offer)


def is_new_job(scraped_job, company):
    """
    Checks if job already exists in DB. Two jobs are the same when they have the same title, end_date, company and job type
    :param scraped_job: instance retrieved by scrapper
    :param company: company that job belongs to
    :return: True/Fase
    """
    return not Job.objects.filter(title=scraped_job.title, company=company, location=scraped_job.location, is_active=True).exists()


def get_job_from_db(scraped_job, company):
    """
    Gets a job from DB based on its title, location and company
    :param scraped_job: instance retrieved by scrapper
    :param company: company that job belongs to
    :return: Model.Job if the job exists in DB. None otherwise.
    :rtype job_scraper.models.Job
    """
    try:
        job_db = Job.objects.get(title=scraped_job.title, company=company, location=scraped_job.location)
    except Job.DoesNotExist:
        job_db = None
    except Job.MultipleObjectsReturned:
        # This exception must never be thrown
        job_db = None
        log_support.set_multiple_duplicated_jobs(scraped_job.title, company, scraped_job.location)

    return job_db


def update_new_job(job):
    """
    Updates a job to "is_new = False"
    :param job: job to be updated
    :type job: Job
    :return: None
    """
    job.is_new = False
    job.save()
    log_support.updated_existent_job(job)


def enable_job(job):
    """
    Updates a job to "is_active = True"
    :param job: job to be updated
    :type job: Job
    :return: None
    """
    job.is_active = True
    job.updated_at = timezone.now()
    job.save()
    log_support.updated_active_job(job)


def disable_job(job):
    """
    Updates a job to "is_active = False"
    :param job: job to be updated
    :type job: Job
    :return: None
    """
    job.is_active = False
    job.updated_at = timezone.now()
    job.save()
    log_support.disabled_job(job)


def get_active_jobs():
    """
    Get a list of jobs that are active.
    :return: QuerySet<Job> with the list of jobs
    """
    return Job.objects.filter(is_active=True)
