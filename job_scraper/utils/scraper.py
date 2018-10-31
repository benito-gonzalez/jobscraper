from bs4 import BeautifulSoup
import dateutil.parser as parser
from dateutil import tz

from job_scraper.utils.job import Job
from job_scraper.utils import request_support


def generate_instance_from_client(client_name, url):
    if client_name == "dna":
        return Dna(url)
    if client_name == "elisa":
        return Elisa(url)


class Scraper(object):

    def __init__(self, url):
        self.url = url

    def extract_info(self, html_content):
        pass


class Dna(Scraper):

    def extract_info(self, html):
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
            job = Job(title, description, location, "dna", None, pub_date, end_date, job_type, url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_full_description(job_details_soup):
        description = ""
        details_bock = job_details_soup.find('div', attrs={'class': 'news-single'})

        for tag in details_bock.find("h5").next_siblings:
            if tag.name == "h5" and tag.text != "Tehtävän kuvaus":
                break
            elif tag.name == "p":
                description += tag.text

        return description

    @staticmethod
    def get_dates(job_details_soup):
        pub_date = ""
        end_date = ""
        pub_date_block = job_details_soup.find('h5', string='Hakuaika')

        for tag in pub_date_block.next_siblings:
            if tag.name == "p":
                date0 = tag.text.split("-")[0]
                pub_date = parser.parse(date0, tzinfos={'EEST':tz.gettz("Europe/Helsinki"), 'EET':tz.gettz("Europe/Helsinki")}).strftime('%Y-%m-%d')
                date1 = tag.text.split("-")[1]
                end_date = parser.parse(date1, tzinfos={'EET':tz.gettz("Europe/Helsinki"), 'EEST':tz.gettz("Europe/Helsinki")}).strftime('%Y-%m-%d')
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
        return jobs
