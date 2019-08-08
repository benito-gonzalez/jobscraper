import os
import django
from django.utils import timezone
from django.db import IntegrityError

if os.path.isfile(os.path.dirname(os.path.dirname(__file__)) + '/../webapp/.is_development'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.development')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'webapp.settings.production')

django.setup()

from job_scraper.models import Company  # noqa: E402
from job_scraper.models import Job  # noqa: E402
from job_scraper.models import City  # noqa: E402
from job_scraper.models import Tag  # noqa: E402
from job_scraper.models import JobTagMap  # noqa: E402
from job_scraper.models import JobCityMap  # noqa: E402
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
    job = Job.objects.create(title=job_offer.title,
                             description=job_offer.description,
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
    return job


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
        # Once we have filled the whole JobCityMap we run this code
        #job_db = None
        #matched_jobs = Job.objects.filter(title=scraped_job.title, company=company)
        #for record in matched_jobs:
        #    # if both locations are empty
        #    record_cities = record.cities.all()
        #    if not record_cities and not scraped_job.cities:
        #        job_db = record
        #        break

        #    if record_cities and scraped_job.cities:
        #        if set(record_cities) == set(scraped_job.cities):
        #            job_db = record
        #            break

        # While JobCityMap is not filled run this:
        job_db = None
        jobs_db = Job.objects.filter(title=scraped_job.title, company=company)
        if len(jobs_db) == 1:
            if not jobs_db[0].location and not scraped_job.cities:
                job_db = jobs_db[0]
                return job_db

        for record in jobs_db:
            record_location_list = scraped_job_location_list = swedish_names_list = []
            if record.location:
                record_location_list = record.location.split(", ")
            if scraped_job.cities:
                scraped_job_location_list = [c.name for c in scraped_job.cities]
                swedish_names_list = [c.swedish_name for c in scraped_job.cities]
                swedish_names_list = [x for x in swedish_names_list if x is not None]

            if set(record_location_list) == set(scraped_job_location_list) or (swedish_names_list and set(record_location_list) == set(swedish_names_list)):
                job_db = record
                return job_db

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


def update_end_date(scraped_job, job_db):
    """
    Updates the end_date job in case it has been updated
    :param scraped_job:
    :param job_db:
    :return:
    """
    end_date_db = None

    if not scraped_job.end_date:
        return

    if job_db.end_date:
        end_date_db = job_db.end_date.strftime('%Y-%m-%d')

    if scraped_job.end_date != end_date_db:
        job_db.end_date = scraped_job.end_date
        # end date information can come from the description so this could be out-of-date. It needs to be updated
        job_db.description = scraped_job.description
        job_db.save()
        log_support.updated_end_date(job_db, scraped_job.end_date)


def get_active_jobs():
    """
    Get a list of jobs that are active.
    :return: QuerySet<Job> with the list of jobs
    """
    return Job.objects.filter(is_active=True)


def get_tags():
    """
    Get all tags from DB
    :return: QuerySet<Tag> with the list of tags
    """
    return Tag.objects.all()


def add_job_tag(job, tag, num_times):
    entry = JobTagMap(job=job, tag=tag, num_times=num_times)
    entry.save()


def is_job_tag_mapped(job, tag):
    return JobTagMap.objects.filter(job=job, tag=tag).exists()


def add_keyword(keyword):
    try:
        Tag.objects.create(name=keyword)
    except IntegrityError:
        # If a tag with the same name already exists, we pass
        pass


def get_cities():
    """
    Get all cities from DB
    :return: QuerySet<City> with the list of cities
    """
    return City.objects.all()


def get_location_by_name(location_name):
    """
    Get the location by a name
    :return: Model.City if the job exists in DB. None otherwise.
    """
    try:
        city_db = City.objects.get(name=location_name)
    except City.DoesNotExist:
        city_db = None

    return city_db


def is_job_location_mapped(job, city):
    return JobCityMap.objects.filter(job=job, city=city).exists()


def add_job_location(job, city):
    entry = JobCityMap(job=job, city=city)
    entry.save()


def get_job_city_map_by_job(job):
    """
    Get a list of job city map.
    :return: QuerySet<Job> with the list of JobCityMap
    """
    return JobCityMap.objects.filter(job=job)


def get_job_cities_by_job(job):
    """
    Get a list of cities.
    :return: QuerySet<City> with the list of City
    """
    return City.objects.filter(job=job)


def delete_job_city_record(job_city):
    """
    :param job_city: Record to be removed
    :return:
    """
    job_city.delete()
