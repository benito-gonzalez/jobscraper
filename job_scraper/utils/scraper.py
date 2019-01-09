from bs4 import BeautifulSoup
import re
import dateutil.parser as parser
from dateutil import tz
import json
import time
import geotext

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
    if client_name.lower() == "smarp oyj":
        return Smarp(client_name, url)
    if client_name.lower() == "silo.ai oy":
        return Silo(client_name, url)
    if client_name.lower() == "abb oy":
        return Abb(client_name, url)
    if client_name.lower() == "qvik oy":
        return Qvik(client_name, url)
    if client_name.lower() == "blueprint genetics oy":
        return Blueprint(client_name, url)
    if client_name.lower() == "eficode oy":
        return Eficode(client_name, url)
    if client_name.lower() == "ericsson":
        return Ericsson(client_name, url)
    if client_name.lower() == "varjo technologies":
        return Varjo(client_name, url)
    if client_name.lower() == "telia finland oyj":
        return Telia(client_name, url)
    if client_name.lower() == "wärtsilä":
        return Wartsila(client_name, url)
    if client_name.lower() == "nordea":
        return Nordea(client_name, url)
    if client_name.lower() == "tieto":
        return Tieto(client_name, url)
    if client_name.lower() == "rightware":
        return Rightware(client_name, url)
    if client_name.lower() == "rovio":
        return Rovio(client_name, url)
    if client_name.lower() == "futurice":
        return Futurice(client_name, url)
    if client_name.lower() == "supercell":
        return Supercell(client_name, url)
    if client_name.lower() == "nokia":
        return Nokia(client_name, url)
    if client_name.lower() == "verto analytics":
        return Verto(client_name, url)
    if client_name.lower() == "efecte oyj":
        return Efecte(client_name, url)
    if client_name.lower() == "nets":
        return Nets(client_name, url)
    if client_name.lower() == "danske bank":
        return Danske(client_name, url)
    if client_name.lower() == "nordcloud":
        return Nordcloud(client_name, url)
    if client_name.lower() == "nebula oy":
        return Nebula(client_name, url)
    else:
        return None


class Scraper(object):
    h_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]

    def __init__(self, client_name, url):
        self.url = url
        self.client_name = client_name

    def extract_info(self, html_content):
        """
        Get all scraped jobs for a specific client
        :param html_content: HTML from the client website to be scraped
        :return: List of Jobs
        """
        pass

    def get_mandatory_fields(self, job):
        """
        Gets the mandatory fields for a specific job
        :param job: Object that contains information for only one specific job
        :return: 'title', 'description_url', 'description'
        """
        pass

    def is_valid_job(self, title, description_url, description):
        """
        :param title: job title. None if it is not valid
        :param description_url: job description url. None if it is not valid
        :param description: job description. "" (empty string) if it is not valid
        :return: Boolean
        """
        application_job_titles = ["avoin hakemus",
                                  "open application",
                                  "open application (finland & sweden)",
                                  "avoin hakemus innofactorille",
                                  "avoin hakemus / open application",
                                  "Every tech position at Futurice. Ever."]
        valid = False

        if not title:
            log_support.set_invalid_title(self.client_name)
        elif title.lower() not in application_job_titles:
            if not description_url:
                log_support.set_invalid_description_url(self.client_name, title)
            elif description == "":
                log_support.set_invalid_description(self.client_name, title)
            else:
                valid = True

        return valid


class Dna(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'news__article-container'})
        if ul:
            for li in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(li)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(li, title)
                    job_details_html = request_support.simple_get(description_url)
                    job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
                    pub_date, end_date = self.get_dates(job_details_soup, title)
                    job_type = self.get_job_type(job_details_soup)
                    job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, job_type, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_span = item.find('span', attrs={'class': 'title'})
        if title_span:
            title = title_span.text

            # Check description_url
            url_span = title_span.find('a')
            if url_span:
                relative_url = url_span.get('href')
                if relative_url:
                    description_url = self.url + relative_url

            # Check description
            description = self.get_full_description(description_url)

        return title, description_url, description

    def get_full_description(self, url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'news-single'})
            if details_block:
                p = details_block.find("p")
                if p:
                    description += str(p)
                    for p in p.next_siblings:
                        if p.name and p.name == "p":
                            description += str(p)
                        elif p.name in self.h_tags:
                            break

        return description

    def get_dates(self, job_details_soup, title):
        pub_date = end_date = None
        pub_date_block = job_details_soup.find('h5', string='Hakuaika')

        if pub_date_block:
            date_p = pub_date_block.find_next('p')
            if date_p:
                date_splited = date_p.text.split("-")
                if len(date_splited) == 2:
                    try:
                        pub_date_datetime = parser.parse(date_splited[0], tzinfos={'EEST': tz.gettz("Europe/Helsinki"), 'EET': tz.gettz("Europe/Helsinki")})
                        end_date_datetime = parser.parse(date_splited[1], tzinfos={'EEST': tz.gettz("Europe/Helsinki"), 'EET': tz.gettz("Europe/Helsinki")})

                        pub_date = pub_date_datetime.strftime('%Y-%m-%d')
                        end_date = end_date_datetime.strftime('%Y-%m-%d')
                    except ValueError:
                        log_support.set_invalid_dates(self.client_name, title)

        return pub_date, end_date

    @staticmethod
    def get_job_type(job_details_soup):
        job_type = ""
        job_type_block = job_details_soup.find('h5', string='Työsuhdetyyppi')

        if job_type_block:
            job_type_p = job_type_block.find_next('p')
            if job_type_p:
                job_type = job_type_p.text

        return job_type

    def get_location(self, item, title):
        location_span = item.find('span', attrs={'class': 'news__location-item'})
        if location_span:
            location = location_span.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location


class Elisa(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                try:
                    pub_date_datetime = parser.parse(item["startDate"])
                    pub_date = pub_date_datetime.strftime('%Y-%m-%d')
                except (ValueError, KeyError):
                    log_support.set_invalid_dates(self.client_name, title)
                    pub_date = None

                try:
                    end_date_datetime = parser.parse(item["endDate"])
                    end_date = end_date_datetime.strftime('%Y-%m-%d')
                except (ValueError, KeyError):
                    log_support.set_invalid_dates(self.client_name, title)
                    end_date = None

                if "jobDomain" in item:
                    job_type = item["jobDomain"]
                else:
                    job_type = None

                job = ScrapedJob(title, description, None, self.client_name, None, pub_date, end_date, job_type, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "jobDescUrl" in item:
                description_url = item["jobDescUrl"]
                if "jobDescription" in item:
                    description = self.get_description(item["jobDescription"])

        return title, description_url, description

    @staticmethod
    def get_description(description_raw):
        description = ""

        soup = BeautifulSoup(description_raw, 'html.parser')
        for tag in soup.find_all():
            for match in tag.find_all('img'):
                match.decompose()
            if tag.name:
                description += str(tag)

        return description


class Vala(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", attrs={'class': 'icon_box icon_position_top no_border'})
        for item in job_divs:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h4", attrs={'class': 'title'})
        if title_tag:
            title = title_tag.text

            url_tag = item.find('a')
            if url_tag and url_tag.get('href'):
                if "https://" in url_tag.get('href'):
                    description_url = url_tag.get('href')
                else:
                    description_url = self.url + url_tag.get('href')

                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_bock = soup.find('div', attrs={'class': 'column_attr clearfix'})
            if details_bock:
                for tag in details_bock.find("h1").next_siblings:
                    if tag.name == "h4" and tag.text.strip() == "Interested?":
                        break
                    if tag != "\n":
                        description += str(tag)

        return description


class Siili(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_block = soup.find('div', attrs={'class': 'listing--job-ads'})

        if jobs_block:
            items = jobs_block.find_all("article")
            for item in items:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location_tag = item.find("div", attrs={'class': 'job-ad__office--listing'})
                    if location_tag:
                        location = location_tag.text.strip()
                    else:
                        location = None
                        log_support.set_invalid_location(self.client_name, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.text.strip()

            relative_url_a = item.find("a")
            if relative_url_a:
                relative_url = relative_url_a.get('href')
                if relative_url:
                    description_url = self.url.split("com/")[0] + "com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(full_url):
        description = ""
        job_details_html = request_support.simple_get(full_url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            job_description_div = soup.find('div', attrs={'class': 'job-ad__description'})
            if job_description_div:
                job_description_tags = job_description_div.find_all(["p", "h3"])
                for tag in job_description_tags:
                    if tag.name == "h3" and "interested?" in tag.text.lower():
                        break
                    if tag != "\n" and tag.text != "":
                        description += str(tag)

        return description


class Innofactor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        if ul:
            for li in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(li)
                if self.is_valid_job(title, description_url, description):
                    job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', attrs={'class': 'title'})
        if title_tag:
            title = title_tag.text.strip()

            relative_url_a = item.find("a")
            if relative_url_a:
                relative_url = relative_url_a.get('href')
                if relative_url:
                    description_url = self.url.split("fi/")[0] + "fi" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = soup.find('div', attrs={'class': 'body'})
            if description_block:
                for p in description_block.find_all("p"):
                    if p.name == "p":
                        description += str(p)

        return description


class Smarp(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        if ul:
            for li in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(li)
                if self.is_valid_job(title, description_url, description):
                    job_details_html = request_support.simple_get(description_url)
                    soup = BeautifulSoup(job_details_html, 'html.parser')
                    location = self.get_location(soup, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("span", {"class": "title"})
        if title_tag:
            title = title_tag.text.strip()

            relative_url_a = item.find("a")
            if relative_url_a:
                relative_url = relative_url_a.get('href')
                if relative_url:
                    description_url = self.url.split("com/")[0] + "com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = soup.find('div', attrs={'class': 'body'})
            if description_block:
                for p in description_block.find_all("p"):
                    if p.name == "p":
                        description += str(p)

        return description

    def get_location(self, soup, job_title):
        location = None
        location_tag = soup.find('h2', attrs={'class': 'byline'})
        if location_tag:
            location_text = location_tag.text
            location_splited = location_text.split("–")
            if len(location_splited) == 2:
                location = location_splited[1].strip()

        if not location:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Silo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", attrs={'class': 'elementor-icon-box-content'})
        for job_div in job_divs:
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                job_details_html = request_support.simple_get(description_url)
                soup = BeautifulSoup(job_details_html, 'html.parser')
                location = self.get_location(soup, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.text.strip()

            relative_url_a = item.find("a")
            if relative_url_a:
                description_url = relative_url_a.get('href')
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find("div", {'class': 'text-body'})
            if description_div:
                for div in description_div.find_all(["p", "ul"]):
                    description += str(div)

        return description

    def get_location(self, soup, job_title):
        location = None
        location_block = soup.find('div', attrs={'class': 'pill blue'})
        if location_block:
            location_text = location_block.text
            location_splited = location_text.split(", ")
            if len(location_splited) == 2:
                location = location_splited[1].strip()

        if not location:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Abb(Scraper):

    def extract_info(self, html):
        # From API
        log_support.log_extract_info(self.client_name)
        jobs = []
        json_dict = json.loads(html)

        for item in json_dict["Items"]:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                if "JobLocation" in item and "AddressLocality" in item["JobLocation"] and item["JobLocation"]["AddressLocality"] and item["JobLocation"]["AddressLocality"] != "":
                    location = item["JobLocation"]["AddressLocality"]
                else:
                    log_support.set_invalid_location(self.client_name, title)
                    location = None

                if "ValidThrough" in item and item["ValidThrough"] and item["ValidThrough"] != "":
                    end_date = self.get_end_date(item["ValidThrough"])
                    if not end_date:
                        log_support.set_invalid_dates(self.client_name, title)
                else:
                    log_support.set_invalid_dates(self.client_name, title)
                    end_date = None

                if "FunctionalArea" in item and "Name" in item["FunctionalArea"] and item["FunctionalArea"]["Name"] and item["FunctionalArea"]["Name"] != "":
                    job_type = item["FunctionalArea"]["Name"]
                else:
                    job_type = None

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "Title" in item:
            title = item["Title"]
            if "Url" in item:
                relative_url = item["Url"]
                description_url = self.url.split("jobs/")[0] + "jobs/details" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            task_item = soup.find("h3", string='Tasks:')
            if task_item:
                for tag in task_item.next_siblings:
                    # remove tag attributes
                    tag.attrs = {}
                    if tag.name and tag.name != "p" and tag.name != "h3":
                        break
                    if tag != "\n":
                        # remove <span> from paragraphs
                        for match in tag.find_all('span'):
                            match.unwrap()
                        description += str(tag)

        return description

    @staticmethod
    def get_end_date(date_field):
        # Formatted as "/Date(1544313600000)/"
        date_string = None
        epoch_splited = date_field.split("(")
        if len(epoch_splited) == 2:
            epoch_splited_2 = epoch_splited[1].split(")")
            if len(epoch_splited_2) == 2:
                epoch = epoch_splited_2[0]
                seconds = int(epoch[:-3])
                date_string = time.strftime('%Y-%m-%d', time.gmtime(seconds))

        return date_string


class Qvik(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", attrs={'class': 'boxes-col'})

        for item in job_divs:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # Qvik has their office in Helsinki but that information does not appear in the HTML tag from their careers.
                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.text.strip()

            url_a = item.find("a")
            if url_a:
                description_url = url_a.get('href')
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find("div", attrs={'class': 'article-container'})
            if description_div:
                for p in description_div.find_all('p'):
                    description += str(p)

        return description


class Blueprint(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        if ul:
            for li in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(li)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(li, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', attrs={'class': 'title'})
        if title_tag:
            title = title_tag.text.strip()

            url_a = item.find("a")
            if url_a:
                relative_url = url_a.get('href')
                if relative_url:
                    description_url = self.url.split("com/")[0] + "com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'body'})
            if description_div:
                for p in description_div.find('p').next_siblings:
                    description += str(p)

        return description

    def get_location(self, li, job_title):
        location = None
        location_block = li.find('span', attrs={'class': 'meta'})
        if location_block:
            location_text = location_block.text
            location_splited = location_text.split("–")
            if len(location_splited) == 2:
                location = location_splited[1].strip()

        if not location:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Eficode(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for job_div in soup.find_all('div', {'class': 'job-ad'}):
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(job_div, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split("com/")[0] + "com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'jd-description'})
            if description_div:
                description_tag = description_div.find('h1')
                if description_tag:
                    for p in description_tag.next_siblings:
                        p.attrs = {}
                        if p != "\n":
                            for match in p.find_all('span'):
                                match.unwrap()
                            description += str(p)

        return description

    def get_location(self, job_div, job_title):
        location = None
        location_block = job_div.find('p')
        if location_block:
            for br in location_block.find_all("br"):
                br.replace_with(", ")

            location_block = location_block.text
            location_block = location_block.replace("Eficode Oy,", "")
            location_block = location_block.replace("Eficode", "")
            location_list = location_block.split(",")
            location_list = map(str.strip, location_list)
            # remove duplicated
            locations = list(dict.fromkeys(location_list))
            location = ", ".join(locations)

        if not location:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Ericsson(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["jobs"]:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                if "city" in item["data"]:
                    location = item["data"]["city"]
                else:
                    log_support.set_invalid_location(self.client_name, title)
                    location = None

                pub_date = self.get_pub_date(item["data"], title)

                job = ScrapedJob(title, description, location, self.client_name, None, pub_date, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "data" in item:
            if "title" in item["data"]:
                title = item["data"]["title"]
            if "meta_data" in item["data"] and "canonical_url" in item["data"]["meta_data"]:
                description_url = item["data"]["meta_data"]["canonical_url"]
            if "description" in item["data"]:
                description = self.get_description(item["data"]["description"])

        return title, description_url, description

    @staticmethod
    def get_description(description_str):
        description = ""
        soup = BeautifulSoup(description_str, 'html.parser')
        description_p = soup.find('p')
        if description_p:
            description += str(description_p)
            for description_p in description_p.next_siblings:
                description_p.attrs = {}
                for match in description_p.find_all('span'):
                    match.unwrap()
                if description_p.text != "\xa0":
                    description += str(description_p)

        return description

    def get_pub_date(self, item, title):
        pub_date = None
        if "create_date" in item:
            try:
                pub_date_datetime = parser.parse(item["create_date"])
                pub_date = pub_date_datetime.strftime('%Y-%m-%d')
            except ValueError:
                log_support.set_invalid_dates(self.client_name, title)

        return pub_date


class Varjo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        job_divs = soup.find_all('a', {'class': 'jobs-position'})
        for job_div in job_divs:
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location_div = job_div.find('span', {'class': 'jobs-position-location'})
                if location_div:
                    location = location_div.text
                else:
                    location = None
                    log_support.set_invalid_location(self.client_name, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', {'class': 'jobs-position-title'})
        if title_tag:
            title = title_tag.text.strip()
            description_url = item.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'jobs-override'})
            if description_div:
                tags = description_div.find_all(['p', 'h3'])
                for tag in tags:
                    if tag.text.strip().lower() == "job description":
                        for p in tag.next_siblings:
                            description += str(p)
                        break

        return description


class Telia(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["vacancies"]:
            if "countries" in item and "Finland" in item["countries"]:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    if "startDate" in item and item["startDate"] != "":
                        pub_date = item["startDate"]
                    else:
                        pub_date = None
                        log_support.set_invalid_dates(self.client_name, title)

                    if "applicationDeadline" in item and item["applicationDeadline"] != "":
                        end_date = item["applicationDeadline"]
                    else:
                        end_date = None
                        log_support.set_invalid_dates(self.client_name, title)

                    if "positionType" in item and item["positionType"] != "":
                        job_type = item["positionType"]
                    else:
                        job_type = None
                        log_support.set_invalid_dates(self.client_name, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, job_type, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
        if "vacancyUrl" in item:
            description_url = item["vacancyUrl"]
        if "additionalJobDescription" in item:
            description = self.get_description(item["additionalJobDescription"])

        return title, description_url, description

    @staticmethod
    def get_description(description_str):
        description = ""
        soup = BeautifulSoup(description_str, 'html.parser')
        description_p = soup.find('p')
        if description_p:
            description += str(description_p)
            for description_p in description_p.next_siblings:
                description_p.attrs = {}
                for match in description_p.find_all('span'):
                    match.unwrap()
                if description_p.text != "\xa0":
                    description += str(description_p)

        return description

    def get_location(self, item, title):
        location = None
        if "locations" in item:
            if len(item["locations"]) > 0:
                location = ', '.join(item["locations"])

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Wartsila(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', {'id': 'searchresults'})
        if table:
            table_body = table.find('tbody')
            if table_body:
                for item in table_body.find_all("tr"):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location_span = item.find('span', {'class': 'jobLocation'})
                        if location_span:
                            location = location_span.text.strip()
                        else:
                            location = None
                            log_support.set_invalid_location(self.client_name, title)

                        pub_date = self.get_pub_date(item.find('span', {'class': 'jobDate'}), title)

                        job = ScrapedJob(title, description, location, self.client_name, None, pub_date, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split("com/")[0] + "com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('span', {'itemprop': 'description'})
            if description_div:
                for p in description_div.children:
                    # remove tag attributes
                    p.attrs = {}
                    if p != "\n" and p.text.strip() != "":
                        for match in p.find_all('span'):
                            match.unwrap()
                        description += str(p)

        return description

    def get_pub_date(self, pub_date_div, title):
        pub_date = None

        if pub_date_div:
            pub_date_text = pub_date_div.text.strip()
            try:
                pub_date = parser.parse(pub_date_text).strftime('%Y-%m-%d')
            except ValueError:
                log_support.set_invalid_dates(self.client_name, title)

        return pub_date


class Nordea(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'class': 'jobs-results'})

        if jobs_div:
            for item in jobs_div.find_all('tr', {'class': 'job-item'}):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split("com/")[0] + "com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    def get_description(self, url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'job--content'})
            if description_div:
                for div in description_div.children:
                    div.attrs = {}
                    if div.name == 'div':
                        items_list = div.find_all(['div', 'ul'])
                        # if div does not contain any div or ul, we get information directly
                        if not items_list:
                            if not div.find('a'):
                                description += self.get_p_tag_from_div(soup, div)
                        else:
                            for elem in items_list:
                                elem.attrs = {}
                                if elem.text != '\xa0':
                                    if elem.name == 'div':
                                        description += self.get_p_tag_from_div(soup, elem)
                                    else:
                                        description += str(elem)
                    elif div.name == "ul":
                        description += str(div)
                    elif div.name == 'h2':
                        if div.text.lower() == "more information" or div.text.lower() == "lisätietoja" or div.text.lower() == "lisätietoja ja hakemuksen lähettäminen":
                            break
                        else:
                            description += str(div)

                description = description.replace('\n', '')

        return description

    @staticmethod
    def get_p_tag_from_div(soup, div):
        if div.text == '\xa0':
            return ""
        new_tag = soup.new_tag('p')
        new_tag.string = div.text.strip()
        div.replace_with(new_tag)
        return str(new_tag)

    def get_location(self, item, title):
        location = None
        location_tag = item.find('td', {'class': 'text--left'})
        if location_tag:
            location_next_tag = location_tag.next_sibling
            if location_next_tag:
                location = location_next_tag.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None
        location_tag = item.find('td', {'class': 'text--left'})
        if location_tag:
            location_next_tag = location_tag.next_sibling
            if location_next_tag:
                date_tag = location_next_tag.next_sibling
                if date_tag:
                    end_date = date_tag.text

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Tieto(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_div = soup.find('div', {'class': 'listingResults'})
        if job_div:
            last_page = False

            while not last_page:
                more_jobs = False
                for item in job_div.find_all('a'):
                    if "jobResultRow" in item.get('class'):
                        title, description_url, description = self.get_mandatory_fields(item)
                        if self.is_valid_job(title, description_url, description):
                            location = self.get_location(item, title)
                            pub_date, end_date = self.get_dates(description_url, title)

                            job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, None, description_url)
                            jobs.append(job)
                    else:
                        if "jobListingPageLoadMore" in item.get("id"):
                            relative_more_jobs_url = item.get('data-url')
                            if relative_more_jobs_url:
                                full_more_jobs_url = self.url.split("com/")[0] + "com" + relative_more_jobs_url
                                more_jobs_html = request_support.simple_get(full_more_jobs_url)
                                if more_jobs_html:
                                    job_div = BeautifulSoup(more_jobs_html, 'html.parser')
                                    more_jobs = True

                if not more_jobs:
                    last_page = True

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', {'class': 'col-md-4'})
        if title_tag:
            title = title_tag.text.strip()

            relative_url = item.get('href')
            if relative_url:
                description_url = self.url.split("com/")[0] + "com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            description_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = description_soup.find('div', {'class': 'infobox'})
            if description_div:
                for p in description_div.next_siblings:
                    if p.name and p.text.lower() == "about tieto":
                        break
                    if p != "\n":
                        description += str(p)

        return description

    def get_location(self, item, title):
        # last div contains the location
        div_list = item.find_all('div', {'class': 'col-md-4'})
        last_div = location = None

        for last_div in div_list:
            pass
        if last_div:
            location = last_div.text.strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_dates(self, url, title):
        pub_date = end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            description_soup = BeautifulSoup(job_details_html, 'html.parser')
            dates_label = description_soup.find('label', string='Appliation period:')
            if dates_label:
                # dates_string is something like "Appliation period: 05 December 2018 - 23 December 2018"
                dates_string = dates_label.parent.text
                dates_fields = dates_string.split(":")
                if len(dates_fields) == 2:
                    dates = dates_string.split(":")[1]
                    pub_date_splited = dates.split(" - ")
                    if len(pub_date_splited) == 2:
                        pub_date_str = dates.split(" - ")[0]
                        end_date_str = dates.split(" - ")[1]
                        try:
                            pub_date = parser.parse(pub_date_str).strftime('%Y-%m-%d')
                            end_date = parser.parse(end_date_str).strftime('%Y-%m-%d')
                        except ValueError:
                            log_support.set_invalid_dates(self.client_name, title)

        return pub_date, end_date


class Rightware(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_div = soup.find_all('div', {'class': 'vacancy-module'})
        for job_div in jobs_div:
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(job_div, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            description_url = title_tag.get('href')
            if description_url:
                if "https://" not in description_url:
                    description_url = self.url.split("com/")[0] + "com" + description_url

                description = self.get_description(description_url)

        return title, description_url, description

    def get_description(self, url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')

            # For jobs which have sequential information
            description_div = soup.find('div', {'class': 'body'})
            if description_div:
                position_h = soup.find(["h2", "h3", "h4"], string='Position')
                if position_h:
                    description += str(position_h)
                    for p in position_h.next_siblings:
                        if self.is_apply_block(p):
                            break
                        if p != "\n" and p.name != "hr":
                            description += str(p)
            else:
                # Job description appears in parallel divs
                description_div = soup.find('div', {'class': 'span12 widget-span widget-type-cell main-content'})
                if description_div:
                    block_tags = description_div.find_all(["h2", "h3", "h4"])
                    for tag in block_tags:
                        if self.is_apply_block(tag):
                            break
                        # Firt paragraph is a definition of the company which we don't want to store.
                        if "team" in tag.text.lower():
                            continue
                        else:
                            description += str(tag)
                            for p in tag.next_siblings:
                                if p != "\n" and p.name != "hr":
                                    description += str(p)

        return description

    def is_apply_block(self, tag):
        return tag.name in self.h_tags and "apply" in tag.text.lower()

    def get_location(self, div, title):
        location = None
        location_p = div.find('p', {'class': 'vacancy-location'})
        if location_p:
            location = location_p.text.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Rovio(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_div = soup.find_all('article', {'class': 'node-vacancy'})

        for job_div in jobs_div:
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(job_div, title)
                end_date = self.get_end_date(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag_h2 = item.find('h2')
        if title_tag_h2:
            title_tag = title_tag_h2.find('a')
            if title_tag:
                title = title_tag.text.strip()
                description_url = title_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'canvas-job-description'})
            if description_div:
                first_paragraph = description_div.find('p')
                if first_paragraph:
                    description += str(first_paragraph)
                    for child in first_paragraph.next_siblings:
                        if child != "\n":
                            description += str(child)

            skills_div = soup.find('div', {'class': 'canvas-skills'})
            if skills_div:
                first_paragraph = skills_div.find('p')
                if first_paragraph:
                    description += str(first_paragraph)
                    for child in first_paragraph.next_siblings:
                        if child != "\n":
                            description += str(child)

        return description

    def get_end_date(self, url, title):
        end_date = None
        expected = False
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            date_ul = soup.find('ul', {'class': 'job-details'})
            if date_ul:
                # first li contains the due date
                date_li = date_ul.find('li')
                if date_li:
                    date_text = date_li.text
                    date_splited = date_text.split(": ")
                    if len(date_splited) == 2:
                        date = date_splited[1].strip()
                        try:
                            end_date_datetime = parser.parse(date)
                            end_date = end_date_datetime.strftime('%Y-%m-%d')
                        except ValueError:
                            log_support.set_invalid_dates(self.client_name, title)
                    else:
                        # Some jobs does not have a due date but "Applications are considered on a rolling basis"
                        expected = True

        if not end_date and not expected:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date

    def get_location(self, div, title):
        location = None
        location_div = div.find('div', {'class': 'field-location-channel'})
        if location_div:
            location_a = location_div.find("a")
            if location_a:
                location = location_a.text.strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Futurice(Scraper):
    """
    Futurice uses javascript to retrieve their list of jobs dynamically so we need to parse the Javascript response from the .js request.
    This response will contains a list of job ids which can be linked to the root_url in order to get a HTML with the job details.
    """

    def extract_info(self, html):
        finnish_offices = ["Helsinki", "Tampere"]
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')
        js_url = self.get_js_url(soup)
        js_response = request_support.simple_get(js_url)
        if js_response:
            js_soup = BeautifulSoup(js_response, 'lxml')
            job_detail_urls = self.get_job_urls(js_soup)

            for job_detail_url in job_detail_urls:
                job_details_html = request_support.simple_get(job_detail_url)
                if job_details_html:
                    soup = BeautifulSoup(job_details_html, 'html.parser')
                    header_div = soup.find('div', {'class': 'hero'})
                    if header_div:
                        title = self.get_title(header_div)
                        description = self.get_description(soup)
                        if self.is_valid_job(title, job_detail_url, description):
                            location = self.get_location(header_div, title)
                            if location in finnish_offices:
                                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, job_detail_url)
                                jobs.append(job)
                    else:
                        log_support.set_invalid_title(self.client_name)

        return jobs

    def get_js_url(self, soup):
        js_url = None
        re_result = re.findall('path---careers-([a-z0-9]+).js', soup.text)
        if len(re_result) > 0:
            js_id = re_result[0]
            js_call = "path---careers-" + js_id + ".js"
            js_url = self.url.split("com/")[0] + "com/" + js_call

        return js_url

    def get_job_urls(self, soup):
        job_detail_urls = []
        root_url = self.url.split("com/")[0] + "com/" + "open-positions/"

        body_text = soup.find('body')
        if body_text:
            text = body_text.text
            # jobs id will be like 'midsenior-product-designer-ux-focus-london' (can include numbers)
            job_ids = re.findall('slug:"([A-Za-z0-9\-]+)",title:', text)
            for job_id in job_ids:
                job_detail_urls.append(root_url + job_id)

        return job_detail_urls

    @staticmethod
    def get_title(header_div):
        title = None
        title_div = header_div.find('h1')

        if title_div:
            title = title_div.text

        return title

    def get_location(self, header_div, title):
        location_div = header_div.find('p')

        if location_div:
            location = location_div.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    @staticmethod
    def get_description(soup):
        description = ""
        description_div = soup.find('div', {'class': 'container src-components----PostText-module---posttext---2vtIL'})
        if description_div:
            for tag in description_div.children:
                if tag != "\n":
                    description += str(tag)

        return description


class Supercell(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        ul = soup.find('ul', {'class': 'job-positions'})
        if ul:
            for item in ul.children:
                if item.name:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

                        job_type_div = item.find('div', {'class': 'views-field-field-position'})
                        if job_type_div:
                            job_type = job_type_div.text.strip()
                        else:
                            job_type = None

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, job_type, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', {'class': 'views-field-title'})
        if title_tag:
            title = title_tag.text.strip().replace('"', '')

            tag_a = item.find('a')
            if tag_a:
                relative_url = tag_a.get('href')
                if relative_url:
                    description_url = self.url.split("com/")[0] + "com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    def get_location(self, item, title):
        location = None
        location_div = item.find('div', {'class': 'views-field-field-location'})

        if location_div:
            location = location_div.text.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'field-name-field-description'})
            if description_div:
                for tag in description_div.children:
                    if tag != "\n":
                        description += str(tag)

        return description


class Nokia(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        last_page = False
        while not last_page:
            for job in soup.find_all('div', {'class': 'job_list_row'}):
                title, description_url, description = self.get_mandatory_fields(job)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(job, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

            if self.is_last_page(soup):
                last_page = True
            else:
                current_page_tag = soup.find('div', {'id': 'jPaginateCurrPage'})
                current_page = int(current_page_tag.text)

                job_details_html = request_support.simple_get(self.url + "/page%d" % (current_page + 1))

                if job_details_html:
                    soup = BeautifulSoup(job_details_html, 'html.parser')
                else:
                    # in case of error, break
                    last_page = True

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_div = soup.find('div', {'class': 'job_description'})
            if description_div:
                for block in description_div.children:
                    block.attrs = {}
                    if block.name:
                        for child in block.find_all(True):
                            child.attrs = {}
                    if block != "\n":
                        description += str(block)

        return description

    def get_location(self, item, title):
        location = None
        location_tag = item.find("span", {"class": "location"})

        if location_tag:
            full_location = location_tag.text.strip()
            cities = geotext.GeoText(full_location).cities
            location = ", ".join(cities)
        if not location or location == "":
            log_support.set_invalid_location(self.client_name, title)

        return location

    def is_last_page(self, soup):
        total_pages = current_page = 0

        total_pages_tag = soup.find('div', {'id': 'jPaginateNumPages'})
        current_page_tag = soup.find('div', {'id': 'jPaginateCurrPage'})

        if total_pages_tag and current_page_tag:
            try:
                total_pages = int(float(total_pages_tag.text))
                current_page = int(current_page_tag.text)
            except (ValueError, TypeError):
                log_support.set_invalid_pagination(self.client_name)
                return True

        return total_pages == current_page


class Verto(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        panel_div = soup.find('div', {'class': 'mk-tabs-panes'})
        if panel_div:
            jobs_div = panel_div.find(self.find_location)
            if jobs_div:
                url_jobs = jobs_div.find_all('a')
                for url_job in url_jobs:
                    url = url_job.get('href')
                    title, description_url, description = self.get_mandatory_fields(url)
                    if self.is_valid_job(title, description_url, description):
                        job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, url):
        title = description_url = None
        description = ""

        if url:
            description_url = self.url + url
            job_details_html = request_support.simple_get(description_url)
            if job_details_html:
                soup = BeautifulSoup(job_details_html, 'html.parser')
                title_tag = soup.find('h2')
                if title_tag:
                    title = title_tag.text
                    description_block = soup.find('div', {'id': 'text-block-4'})
                    if description_block:
                        for tag in description_block.children:
                            if tag != "\n":
                                for child in tag.find_all(True):
                                    child.attrs = {}
                                description += str(tag)

        return title, description_url, description

    @staticmethod
    def find_location(tag):
        return tag.name == 'div' and 'Helsinki' in tag.get_text()


class Efecte(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["data"]:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                if "location" in item and "city" in item["location"] and "name" in item["location"]["city"]:
                    location = item["location"]["city"]["name"]
                else:
                    location = None
                    log_support.set_invalid_location(self.client_name, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "name" in item:
            title = item["name"]
            if "slug" in item and "id" in item:
                description_url = self.url.split(".com/")[0] + ".com/#/jobs/" + item["slug"] + "/" + str(item["id"])
                # check 'description_url' is valid
                description_info = request_support.simple_get(description_url)
                if description_info:
                    description = item["description"]

        return title, description_url, description


class Nets(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        scripts = soup.find_all('script', {'type': 'text/javascript'})
        for script in scripts:
            if "var jsonData" in script.get_text():
                jobs_text = self.get_jobs_text(script)
                if jobs_text != "":
                    try:
                        jobs_json = json.loads(jobs_text)

                        for item in jobs_json:
                            title, description_url, description = self.get_mandatory_fields(item)
                            if self.is_valid_job(title, description_url, description):
                                if "Country" in item:
                                    location = item["Country"]
                                else:
                                    location = None
                                    log_support.set_invalid_location(self.client_name, title)

                                end_date = self.get_end_date(item, title)

                                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                                jobs.append(job)

                    except json.JSONDecodeError:
                        log_support.set_invalid_json(self.client_name)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "JobTitle" in item:
            title = item["JobTitle"]
            if "JobReqId" in item:
                description_url = self.url + "?jobId=" + str(item["JobReqId"])
                # check 'description_url' is valid
                description_info = request_support.simple_get(description_url)
                if description_info:
                    description = item["JobDescription"]

        return title, description_url, description

    @staticmethod
    def get_jobs_text(script):
        try:
            jobs_txt = "[" + script.text.split("[", 1)[1].split("]")[0] + "]"
        except (ValueError, TypeError):
            jobs_txt = ""

        return jobs_txt

    def get_end_date(self, item, title):
        date_string = None
        if "ExpirationDate" in item:
            date_field = item["ExpirationDate"]
            epoch_splited = date_field.split("(")
            if len(epoch_splited) == 2:
                epoch_splited_2 = epoch_splited[1].split(")")
                if len(epoch_splited_2) == 2:
                    epoch = epoch_splited_2[0]
                    seconds = int(epoch[:-3])
                    date_string = time.strftime('%Y-%m-%d', time.gmtime(seconds))

        if not date_string:
            log_support.set_invalid_dates(self.client_name, title)

        return date_string


class Danske(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', {'class': 'datagrid'})
        for row in table.find_all("tr"):
            if self.is_header(row):
                continue
            title, description_url, description, is_finnish = self.get_mandatory_fields(row)
            if is_finnish and self.is_valid_job(title, description_url, description):
                # location has already being checked in get_mandatory_fields()
                location = row.find("span").text
                end_date = self.get_end_date(row, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, row):
        title = description_url = None
        description = ""
        is_finnish = False

        # Check title
        title_tag = row.find('a')
        if title_tag:
            title_raw = title_tag.text
            # title_raw contains multiple consecutive whitespaces in the middle
            title = " ".join(title_raw.split())

            # Since Danske Bank has a lot of jobs and they can not be filtered out, scraper gets the location and will only retrieve job description for those based on Finland
            location_tag = row.find("span")
            if location_tag:
                location = location_tag.text
                if "FI" in geotext.GeoText(location).country_mentions:
                    is_finnish = True
                    url_tag = row.find('a')
                    if url_tag:
                        url_raw = url_tag['onclick']
                        description_url = self.get_url_from_raw(url_raw)
                        description = self.get_full_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def is_header(row):
        header = False
        a_tag = row.find("a")
        if a_tag:
            header = (a_tag.text == "Job title")

        return header

    @staticmethod
    def get_url_from_raw(url_raw):
        url = re.findall(r'(https?://[a-zA-Z0-9/\-_.]+)', url_raw)
        if len(url) > 0:
            return url[0]

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            # It has several identical 'td' but only one has information within a <p> tag.
            blocks = job_details_soup.find_all('td', {'valign': 'top'})
            for block in blocks:
                first_paragraph = block.find(['p', 'br'])
                if first_paragraph:
                    first_paragraph.attrs = {}
                    description += str(first_paragraph)
                    for tag in first_paragraph.next_siblings:
                        tag.attrs = {}
                        description += str(tag)

        return description

    def get_end_date(self, row, title):
        # end date is in the last column (td)
        end_date = None
        columns = row.find_all('td')
        date_tag = columns[len(columns)-1]
        if date_tag:
            date = date_tag.text
            end_date_datetime = parser.parse(date)
            end_date = end_date_datetime.strftime('%Y-%m-%d')

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Nordcloud(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
            if is_finnish and self.is_valid_job(title, description_url, description):
                if "location" in item and "city" in item["location"]:
                    location = item["location"]["city"]
                else:
                    location = None
                    log_support.set_invalid_location(self.client_name, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        finnish = False
        title = description_url = None
        description = ""

        if self.is_finnish(item):
            finnish = True
            if "name" in item:
                title = item["name"]
                if "url" in item:
                    description_url = item["url"]
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description, finnish

    @staticmethod
    def is_finnish(item):
        return "location" in item and "country" in item["location"] and "name" in item["location"]["country"] and "Finland" == item["location"]["country"]["name"]

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'description'})
            if details_block:
                for child in details_block.children:
                    # skip images
                    if not child.find('img'):
                        description += str(child)

        return description


class Nebula(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find("div", attrs={'class': 'o-open-positions'})
        if jobs_div:
            for item in jobs_div.find_all('div', {'class': 'open-position-item'}):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

            return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_span = item.find('div', attrs={'class': 'open-position-item__title'})
        if title_span and title_span.text:
            title = title_span.text.strip()

            # Check description_url
            url_span = item.find('a')
            if url_span:
                if "https://" in url_span.get('href'):
                    description_url = url_span.get('href')
                else:
                    description_url = self.url.split(".fi/")[0] + ".fi" + url_span.get('href')

                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            block_description = job_details_soup.find('div', {'class': 'o-paragraph__container'})
            if block_description:
                title_line = block_description.find('h3')
                if title_line:
                    for sibling in title_line.next_siblings:
                        description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None
        location_span = item.find('span', attrs={'class': 'open-position-item__location'})
        if location_span and location_span.text:
            location = location_span.text.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location
