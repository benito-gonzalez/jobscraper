from bs4 import BeautifulSoup
import dateutil.parser as parser
from dateutil import tz
import json
from re import sub

from job_scraper.utils.job import ScrapedJob
from job_scraper.utils import request_support
from job_scraper.utils import log_support


def generate_instance_from_client(client_name, url):
    if client_name.lower() == "dna":
        return Dna(client_name, url)
    if client_name.lower() == "elisa":
        return Elisa(client_name, url)
    if client_name.lower() == "vala group oy":
        return Vala(client_name, url)
    if client_name.lower() == "siili solutions oyj":
        return Siili(client_name, url)
    if client_name.lower() == "innofactor oyj":
        return Innofactor(client_name, url)
    else:
        return None


class Scraper(object):

    def __init__(self, client_name, url):
        self.url = url
        self.client_name = client_name

    def extract_info(self, html_content):
        pass


class Dna(Scraper):

    def extract_info(self, html):
        """
        Receives an HTML from DNA client and scraps it filling job offer information
        :param html:
        :return: ScrapedJob
        """
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'news__article-container'})
        lis = ul.findAll('li')
        for li in lis:
            title = li.find('span', attrs={'class': 'title'}).text
            url = self.url + li.find('span', attrs={'class': 'title'}).find('a')['href']
            location = li.find('span', attrs={'class': 'news__location-item'}).text

            # Get job details
            job_details_html = request_support.simple_get(url)
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description = self.get_full_description(job_details_soup)
            pub_date, end_date = self.get_dates(job_details_soup)
            job_type = self.get_job_type(job_details_soup)
            job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, job_type, url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_full_description(job_details_soup):
        description = ""
        details_block = job_details_soup.find('div', attrs={'class': 'news-single'})

        for tag in details_block.find("h5").next_siblings:
            if tag.name == "h5" and tag.text != "Tehtävän kuvaus":
                break
            elif tag.name == "p":
                description += tag.text + "\n"

        return description

    @staticmethod
    def get_dates(job_details_soup):
        pub_date = ""
        end_date = ""
        pub_date_block = job_details_soup.find('h5', string='Hakuaika')

        for tag in pub_date_block.next_siblings:
            if tag.name == "p":
                date0 = tag.text.split("-")[0]
                pub_date = parser.parse(date0, tzinfos={'EEST': tz.gettz("Europe/Helsinki"), 'EET': tz.gettz("Europe/Helsinki")}).strftime('%Y-%m-%d')
                date1 = tag.text.split("-")[1]
                end_date = parser.parse(date1, tzinfos={'EET': tz.gettz("Europe/Helsinki"), 'EEST': tz.gettz("Europe/Helsinki")}).strftime('%Y-%m-%d')
                break

        return pub_date, end_date

    @staticmethod
    def get_job_type(job_details_soup):
        job_type = ""
        pub_date_block = job_details_soup.find('h5', string='Työsuhdetyyppi')

        for tag in pub_date_block.next_siblings:
            if tag.name == "p":
                job_type = tag.text
                break

        return job_type


class Elisa(Scraper):
    def extract_info(self, html):
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title = item["title"]
            description = BeautifulSoup(item["jobDescription"], "lxml").text

            if item["startDate"] != "":
                pub_date = parser.parse(item["startDate"]).strftime('%Y-%m-%d')
            else:
                pub_date = None
            if item["endDate"] != "":
                end_date = parser.parse(item["endDate"]).strftime('%Y-%m-%d')
            else:
                end_date = None

            job_type = item["jobDomain"]
            url = item["jobDescUrl"]
            job = ScrapedJob(title, description, None, self.client_name, None, pub_date, end_date, job_type, url)
            jobs.append(job)

        return jobs


class Vala(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        section = soup.find("div", attrs={'class': 'sections_group'})
        items = section.findAll("a")
        for item in items:
            title = item.find("h4", attrs={'class': 'title'}).text
            # Vala has a list of jobs. Last item from the list is not a job a an applicatin form. Script must skip here
            if title == "Open Application":
                continue
            relative_url = item['href']
            full_url = self.url + relative_url
            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            details_bock = soup.find('div', attrs={'class': 'column_attr clearfix'})

            description = ""
            for tag in details_bock.find("h1").next_siblings:
                if tag.name == "h4":
                    break
                elif tag.name == "p":
                    description += tag.text

            job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs


class Siili(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_block = soup.find('div', attrs={'class': 'listing--job-ads'})

        items = jobs_block.find_all("article")
        for item in items:
            title = item.find("h3").text.strip()
            location = item.find("div", attrs={'class': 'job-ad__office--listing'}).text.strip()
            relative_url = item.find("a")['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url

            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            job_description = soup.find('div', attrs={'class': 'job-ad__description'})
            description = job_description.get_text()

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs


class Innofactor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        lis = ul.findAll('li')
        for li in lis:
            title = li.find('span', attrs={'class': 'title'}).text
            # "avoin hakemus" == "open application"
            if "avoin hakemus" in title.lower():
                continue
            relative_url = li.find("a")['href']
            full_url = self.url.split("fi/")[0] + "fi" + relative_url

            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = soup.find('div', attrs={'class': 'body'})
            description = description_block.get_text('\n', strip=True)

            # description has multiple consecutive whitespaces. we need to remove them
            formatted_description = sub(' +', ' ', description)
            job = ScrapedJob(title, formatted_description, None, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs
