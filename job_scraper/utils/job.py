
class ScrapedJob:

    def __init__(self, title, description, location, company, salary, pub_date, end_date, job_type, url):
        self.title = title
        self.description = description
        self.location = location  # used by scraper.py to fill the job location as a plain string
        self.company_name = company
        self.salary = salary
        self.pub_date = pub_date
        self.end_date = end_date
        self.job_type = job_type
        self.url = url
        self.cities = None  # used by run_scraper.py in enrich_location() to generate the cities based on self.location

    def __str__(self):
        return self.title + "\t at " + self.company_name
