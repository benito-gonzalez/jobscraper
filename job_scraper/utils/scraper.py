from bs4 import Tag, BeautifulSoup
import re
import dateutil.parser as parser
from dateutil import tz
import json
import time

from job_scraper.utils.job import ScrapedJob
from job_scraper.utils import request_support
from job_scraper.utils import log_support
from job_scraper.utils.locator import CityLocator


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
    if client_name.lower() == "digital goodie":
        return Digital(client_name, url)
    if client_name.lower() == "nightingale health":
        return Nightingale(client_name, url)
    if client_name.lower() == "sandvik":
        return Sandvik(client_name, url)
    if client_name.lower() == "crf health":
        return Crf(client_name, url)
    if client_name.lower() == "op financial group":
        return Op(client_name, url)
    if client_name.lower() == "dream broker":
        return DreamBroker(client_name, url)
    if client_name.lower() == "relex":
        return Relex(client_name, url)
    if client_name.lower() == "f-secure":
        return FSecure(client_name, url)
    if client_name.lower() == "outotec":
        return Outotec(client_name, url)
    if client_name.lower() == "kone":
        return Kone(client_name, url)
    if client_name.lower() == "smartly.io":
        return Smartly(client_name, url)
    if client_name.lower() == "cybercom finland oy":
        return Cybercom(client_name, url)
    if client_name.lower() == "enfo oyj":
        return Enfo(client_name, url)
    if client_name.lower() == "sofigate":
        return Sofigate(client_name, url)
    if client_name.lower() == "blue meteorite":
        return BlueMeteorite(client_name, url)
    if client_name.lower() == "sulava":
        return Sulava(client_name, url)
    if client_name.lower() == "nitor":
        return Nitor(client_name, url)
    if client_name.lower() == "softability":
        return Softability(client_name, url)
    if client_name.lower() == "fleetonomy.ai":
        return Fleetonomy(client_name, url)
    if client_name.lower() == "ubisoft redlynx":
        return Ubisoft(client_name, url)
    if client_name.lower() == "remedy entertainment plc":
        return Remedy(client_name, url)
    if client_name.lower() == "paf":
        return Paf(client_name, url)
    if client_name.lower() == "fluido":
        return Fluido(client_name, url)
    if client_name.lower() == "atea":
        return Atea(client_name, url)
    if client_name.lower() == "if":
        return If(client_name, url)
    if client_name.lower() == "epic games":
        return EpicGames(client_name, url)
    if client_name.lower() == "sanoma":
        return Sanoma(client_name, url)
    if client_name.lower() == "orion":
        return Orion(client_name, url)
    if client_name.lower() == "aktia":
        return Aktia(client_name, url)
    if client_name.lower() == "management events":
        return ManagementEvents(client_name, url)
    if client_name.lower() == "holvi":
        return Holvi(client_name, url)
    if client_name.lower() == "finitec":
        return Finitec(client_name, url)
    if client_name.lower() == "ferratum":
        return Ferratum(client_name, url)
    if client_name.lower() == "bon games":
        return BonGames(client_name, url)
    if client_name.lower() == "lightneer inc":
        return Lightneer(client_name, url)
    if client_name.lower() == "unity technologies":
        return UnityTechnologies(client_name, url)
    if client_name.lower() == "futureplay":
        return FuturePlay(client_name, url)
    if client_name.lower() == "redhill games":
        return RedhillGames(client_name, url)
    if client_name.lower() == "seriously digital entertainment":
        return SeriouslyDigitalEntertainment(client_name, url)
    if client_name.lower() == "housemarque":
        return Housemarque(client_name, url)
    if client_name == "Hatch Entertainment Oy":
        return HatchEntertainmentOy(client_name, url)
    if client_name == "Qentinel":
        return Qentinel(client_name, url)
    if client_name == "Intopalo Digital Oy":
        return Intopalo(client_name, url)
    if client_name == "Reaktor":
        return Reaktor(client_name, url)
    if client_name == "Bittium":
        return Bittium(client_name, url)
    if client_name == "Accenture":
        return Accenture(client_name, url)
    if client_name == "Napa":
        return Napa(client_name, url)
    if client_name == "AJR solutions Oy":
        return AjrSolutions(client_name, url)
    if client_name == "Anders":
        return Anders(client_name, url)
    if client_name == "Small Giant Games":
        return SmallGiantGames(client_name, url)
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
                                  "open applications",
                                  "every tech position at futurice. ever.",
                                  "your title here",
                                  "avoin työharjoitteluhakemus",
                                  "women who code"]
        valid = False

        if not title:
            log_support.set_invalid_title(self.client_name)
        elif not any(s in title.lower() for s in application_job_titles):
            if not description_url:
                log_support.set_invalid_description_url(self.client_name, title)
            elif description == "":
                log_support.set_invalid_description(self.client_name, title)
            else:
                valid = True

        return valid

    @staticmethod
    def clean_attrs(tag):
        if isinstance(tag, Tag):
            tag.attrs = {}
            for child in tag.find_all(True):
                child.attrs = {}


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
                # Find "Task description"
                first_tag = details_block.find("h5", string="Tehtävän kuvaus")
                if first_tag:
                    for p in first_tag.next_siblings:
                        if p.name and p.name == "p" and p.text != '\xa0':
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
        for child in soup.children:
            if isinstance(child, Tag):
                Scraper.clean_attrs(child)
                description += str(child).replace(u'\xa0', "").replace("  ", "")

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
        job_divs = soup.find_all("a", attrs={'class': 'eael-elements-flip-box-flip-card'})
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

        title_tag = item.find("h2")
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

        ul_jobs = soup.find('ul', {'class': 'jobs'})
        if ul_jobs:
            for li in ul_jobs.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(li)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(li, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', {'class': 'title'})
        if title_tag:
            title = title_tag.text.strip()

            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'job'})
            if description_div:
                first_p = description_div.find('p')
                if first_p:
                    description += str(first_p)
                    for p in first_p.next_siblings:
                        if p.name:
                            if 'class' in p.attrs and 'video-container' in p.attrs['class']:
                                continue
                            if p.text != "\xa0":
                                description += str(p)

        return description

    def get_location(self, item, job_title):
        location = None
        first_span = item.find('span', {'class': 'title'})
        if first_span:
            second_span = first_span.find_next_sibling('span')
            if second_span:
                location = second_span.get_text()

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

        positions = soup.find_all('li', {'class': 'block--jobs-list__list__item'})
        for job_div in positions:
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location_div = job_div.find('h6', {'class': 'block--jobs-list__list__item__job-location'})
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

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.text.strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            first_line = soup.find('h1')
            if first_line:
                for tag in first_line.next_siblings:
                    if tag.name:
                        Scraper.clean_attrs(tag)
                        if tag.name == "iframe" or tag.find('iframe'):
                            break
                        description += str(tag)

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
                        end_date = self.get_end_date(title, description)

                        job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, None, description_url)
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
                    Scraper.clean_attrs(p)
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

    def get_end_date(self, title, description):
        end_date = None

        soup = BeautifulSoup(description, "lxml")
        end_date_tag1 = soup.find(lambda tag: tag.name == "p" and "Last application date:" in tag.text)
        end_date_tag2 = soup.find(lambda tag: tag.name == "p" and "Please apply by " in tag.text)
        if end_date_tag1:
            tag_splitted = end_date_tag1.text.split("Last application date:")
            if len(tag_splitted) > 1:
                date_raw = tag_splitted[1]
                try:
                    end_date = parser.parse(date_raw, dayfirst=True).strftime('%Y-%m-%d')
                except ValueError:
                    log_support.set_invalid_dates(self.client_name, title)

        elif end_date_tag2:
            tag_splitted = end_date_tag2.text.split("Please apply by ")
            if len(tag_splitted) > 1:
                date_raw = tag_splitted[1]
                try:
                    end_date = parser.parse(date_raw, dayfirst=True).strftime('%Y-%m-%d')
                except ValueError:
                    log_support.set_invalid_dates(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


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
            description_div = soup.find('div', {'class': 'job-details__content-wrapper'})
            if description_div:
                description_content = description_div.find('div', {'class': 'content'})
                if description_content:
                    for div in description_content.children:
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
            dates_label = description_soup.find('label', string='Application period:')
            if dates_label:
                # dates_string is something like "Application period: 05 December 2018 - 23 December 2018"
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
            title, description_url, description, valid = self.get_mandatory_fields(job_div)
            if valid and self.is_valid_job(title, description_url, description):
                location = self.get_location(job_div, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        valid = True

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            description_url = title_tag.get('href')
            if description_url:
                if "https://" not in description_url:
                    description_url = self.url.split("com/")[0] + "com" + description_url

                # The job "Software Engineer – Student or Recent Graduate" points to "https://rightware.teamtailor.com/connect" which is a form, not a job description
                if "/connect" in description_url:
                    valid = False
                else:
                    description = self.get_description(description_url)

        return title, description_url, description, valid

    def get_description(self, url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')

            # For jobs which have sequential information
            description_div = soup.find('div', {'class': 'body'})
            if description_div:
                for child in description_div.children:
                    if child.name:
                        self.clean_attrs(child)
                        description += str(child)

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
            job_ids = re.findall('slug:"([A-Za-z0-9-]+)",title:', text)
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
        description_div = soup.find('div', {'class': 'src-components----PostText-module---posttext---2vtIL'})
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
                title, description_url, description, is_finnish = self.get_mandatory_fields(job)
                if is_finnish and self.is_valid_job(title, description_url, description):
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
        finnish = False

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

            finnish = self.is_finnish(item, title)

        return title, description_url, description, finnish

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

    def is_finnish(self, item, title):
        # It will skip those jobs which are not located in Finland. Due to that, if we can not get a job location, we will not store it. It needs to raise an error in that case.
        finnish = False
        location_tag = item.find("span", {"class": "location"})
        locator = CityLocator()

        if location_tag:
            full_location = location_tag.text.strip()
            cities = locator.get_finnish_cities(full_location)
            if cities:
                finnish = True
        else:
            log_support.set_error_message(self.client_name, "Could not get location from job " + title)

        return finnish

    def get_location(self, item, title):
        location = None
        location_tag = item.find("span", {"class": "location"})
        locator = CityLocator()

        if location_tag:
            full_location = location_tag.text.strip()
            cities = locator.get_finnish_cities(full_location)
            if cities:
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

        helsinki_jobs = soup.find('div', {'class': 'title-mobile'}, string="Helsinki")
        if helsinki_jobs:
            items = helsinki_jobs.parent.find_all('div', {'class': 'box-holder'})
            for item in items:
                url_tag = item.find('a')
                if url_tag:
                    title, description_url, description = self.get_mandatory_fields(url_tag.get('href'))
                    if self.is_valid_job(title, description_url, description):
                        job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, url):
        title = description_url = None
        description = ""

        if url:
            description_url = self.url.split(".com/")[0] + ".com" + url
            job_details_html = request_support.simple_get(description_url)
            if job_details_html:
                soup = BeautifulSoup(job_details_html, 'html.parser')
                title_tag = soup.find('h2')
                if title_tag:
                    title = title_tag.text
                    description_block = soup.find('div', {'id': 'text-block-7'})
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
        locator = CityLocator()

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
                if locator.has_finnish_cities(location):
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
        date_tag = columns[len(columns) - 1]
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
                        if sibling.name:
                            sibling.attrs = {}
                            for tag in sibling.find_all(True):
                                tag.attrs = {}
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


class Digital(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find_all("div", attrs={'class': 'entry-content-wrapper clearfix'})
        # only one of the divs in jobs_div include the list of jobs, we need to find it
        for div in jobs_div:
            if div.find('h3', {'class': 'av-special-heading-tag'}):
                for child in div.children:
                    if child.name and child.find('h3', {'class': 'av-special-heading-tag'}) and child.find('a'):
                        title, description_url, description = self.get_mandatory_fields(child)
                        if self.is_valid_job(title, description_url, description):
                            location = self.get_location(description_url, title)

                            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                            jobs.append(job)
        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.text

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            first_paragraph = job_details_soup.find('section', {'class': 'av_textblock_section'})
            if first_paragraph:
                first_paragraph.attrs = {}
                for tag in first_paragraph.find_all(True):
                    tag.attrs = {}
                description += str(first_paragraph)
                for sibling in first_paragraph.next_siblings:
                    if sibling.name:
                        sibling.attrs = {}
                        for tag in sibling.find_all(True):
                            tag.attrs = {}
                        description += str(sibling)

        return description

    def get_location(self, description_url, title):
        location = None

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            location_tag = job_details_soup.find('div', {'class': 'av-subheading'})
            if location_tag:
                location = location_tag.text.strip().title()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Nightingale(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("div", attrs={'class': 'box'})
        for item in items:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # All current jobs are located in Helsinki but this information can not be scraped so it is hard-coded
                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.text

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            title_line = job_details_soup.find('h2')
            if title_line:
                # next div to title_line contains all HTML tags description
                description_block = title_line.next_sibling
                for tag in description_block.children:
                    if tag.name and tag.text.strip() != "":
                        # Last description block called "Next steps" includes information to apply
                        if tag.text.strip() == "Next steps":
                            break
                        description += str(tag)

        return description


class Sandvik(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        items = soup.find_all("li", attrs={'class': 'job'})
        for item in items:
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

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text
            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split(".sandvik/")[0] + ".sandvik" + relative_url

            # Check description
            description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'article text'})
            if details_block:
                tag = details_block.find("p")
                if tag:
                    description += str(tag)
                    for tag in tag.next_siblings:
                        if tag.name and (tag.text == "Contact information" or tag.text == "Lisätietoja/yhteydenotot"):
                            break
                        description += str(tag)

        return description

    def get_location(self, item, title):
        location = None
        location_span = item.find('span', string="Location:")
        if location_span:
            location_tag = location_span.next_sibling
            if location_tag:
                location = location_tag.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None
        date_span = item.find('span', string="Deadline:")
        if date_span:
            date_tag = date_span.next_sibling.strip()
            if date_tag:
                date_raw = date_tag.strip()
                end_date_datetime = parser.parse(date_raw)
                end_date = end_date_datetime.strftime('%Y-%m-%d')
        else:
            log_support.set_invalid_location(self.client_name, title)

        return end_date


class Crf(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        iframe = soup.find("iframe")
        if iframe and 'src' in iframe.attrs:
            job_details_html = request_support.simple_get(iframe.attrs['src'])
            if job_details_html:
                iframe_soup = BeautifulSoup(job_details_html, 'lxml')

                items = iframe_soup.find_all("li", attrs={'class': 'row'})
                for item in items:
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
        title_tag = item.find('div', {'class': 'title'})
        if title_tag:
            # title_tag has two span, only the second one contains the title
            first_span = title_tag.find('span', {'class': 'field-label'})
            if first_span:
                second_span = first_span.find_next_sibling('span')
                if second_span:
                    title = second_span.text.strip()
                    url_tag = title_tag.find('a')
                    if url_tag:
                        description_url_raw = url_tag.get('href')
                        description_url = description_url_raw.split("?in_iframe")[0]
                        description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            iframe = job_details_soup.find("iframe")
            if iframe and 'src' in iframe.attrs:
                job_details_html = request_support.simple_get(iframe.attrs['src'])
                if job_details_html:
                    iframe_soup = BeautifulSoup(job_details_html, 'lxml')
                    details_block = iframe_soup.find('div', attrs={'class': 'iCIMS_JobContent'})
                    if details_block:
                        has_skip_title_line = True
                        for block in details_block.children:
                            if block.name:
                                # After the job description, page has a HTML tag with the content "\n\xa0\n", after it, the description is done.
                                if "\n\xa0\n" in block.text:
                                    break

                                # Skip blocks which contains reduntand job information and the line "Role Overview"
                                if block.find('div', {'role': 'list'}) or block.text.strip() == "Role Overview":
                                    continue

                                block.attrs = {}

                                # some title has a large font size, this must be reduced to h4
                                if block.name == "h2":
                                    block.name = "h4"

                                # clean html attributes and remove those that contain \xa0
                                for tag in block.find_all(True):
                                    tag.attrs = {}
                                    if tag.text == "\xa0":
                                        tag.extract()

                                # the first line from the description contains the job title (or similar). It must be removed
                                if has_skip_title_line:
                                    title_line = block.find('p')
                                    if title_line:
                                        title_line.extract()
                                    has_skip_title_line = False

                                description += str(block)

        return description

    def get_location(self, item, title):
        location = None
        # first span from 'row' contain the location block. Location text is in the next span
        first_span = item.find('span', {'class': 'field-label'})
        if first_span:
            second_span = first_span.find_next_sibling('span')
            if second_span:
                location = second_span.text.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Op(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        last_page = False
        while not last_page:
            for job in soup.find_all('tr', {'class': 'data-row clickable'}):
                title, description_url, description = self.get_mandatory_fields(job)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(job, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

            if self.is_last_page(soup):
                last_page = True
            else:
                ul_pagination = soup.find('ul', {'class': 'pagination'})
                if ul_pagination:
                    current_page_tag = ul_pagination.find('li', {'class': 'active'})
                    if current_page_tag:
                        next_page = current_page_tag.find_next_sibling('li')
                        if next_page:
                            url_tag = next_page.find('a')
                            if url_tag and url_tag.get('href'):
                                next_page_url = self.url + url_tag.get('href')

                                job_details_html = request_support.simple_get(next_page_url)

                                if job_details_html:
                                    soup = BeautifulSoup(job_details_html, 'html.parser')
                                else:
                                    # in case of error, break
                                    last_page = True

        return jobs

    def is_last_page(self, soup):
        total_pages = current_page = 0

        ul_pagination = soup.find('ul', {'class': 'pagination'})
        if ul_pagination:
            total_pages_tag = ul_pagination.find_all('li')
            current_page_tag = ul_pagination.find('li', {'class': 'active'})

            if total_pages_tag and current_page_tag:
                try:
                    # pagination block has "<<" and ">>" at the beginning and at the end, the rest of elements are the pages
                    total_pages = len(total_pages_tag) - 2
                    current_page = int(current_page_tag.text)
                    if total_pages < 1:
                        raise ValueError

                except (ValueError, TypeError):
                    log_support.set_invalid_pagination(self.client_name)
                    return True

        return total_pages == current_page

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text

            # Check description_url
            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('span', {'class': 'jobdescription'})
            if description_div:
                for block in description_div.children:
                    if block.name:
                        block.attrs = {}
                        # clean html attributes and remove those that contain \xa0
                        for tag in block.find_all(True):
                            tag.attrs = {}
                            if tag.text == "\xa0":
                                tag.extract()

                        if block.text != "\xa0":
                            description += str(block)

        return description

    def get_location(self, item, title):
        location_span = item.find('span', attrs={'class': 'jobLocation'})
        if location_span:
            location = location_span.text.strip()
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location


class DreamBroker(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        items = soup.find_all("li", attrs={'class': 'career-list-item'})

        for item in items:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h3", attrs={'class': 'career-title'})
        if title_tag:
            title = title_tag.text.strip()

            url_tag = item.find('a', {'class': 'career-link'})
            if url_tag and url_tag.get('href'):
                description_url = url_tag.get('href')
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            details_bock = soup.find('article', {'class': 'db_career'})
            if details_bock:
                for tag in details_bock.children:
                    if tag.name and tag.find("script"):
                        continue
                    if tag != "\n":
                        description += str(tag)

        return description

    def get_location(self, item, title):
        location_span = item.find("h3", attrs={'class': 'career-subtitle'})
        if location_span:
            location = location_span.text.strip()
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location


class Relex(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "objects" in json_dict:
            for item in json_dict["objects"]:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    if "location" in item and "city" in item["location"]:
                        location = item["location"]["city"]
                    else:
                        location = None
                        log_support.set_invalid_location(self.client_name, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "hosted_url" in item:
                description_url = item["hosted_url"]
                if "description" in item:
                    description = item["description"]

        return title, description_url, description


class FSecure(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)
                end_date = self.get_end_date(item, title)
                if "employment_type" in item:
                    job_type = item["employment_type"]
                else:
                    job_type = None

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "urls" in item and "ad" in item["urls"]:
                description_url = item["urls"]["ad"]
                if "descr" in item:
                    description = item["descr"]
                    if "skills" in item:
                        description += item["skills"]

        return title, description_url, description

    def get_location(self, item, title):
        cities = []
        if "locations" in item:
            for location in item["locations"]:
                if "location" in location and "city" in location["location"]:
                    cities.append(location["location"]["city"])

        if cities:
            location = ", ".join(cities)
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "to_date" in item:
            if item["to_date"]:
                end_date_datetime = parser.parse(item["to_date"])
                end_date = end_date_datetime.strftime('%Y-%m-%d')
        else:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Outotec(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find("table", attrs={'id': 'idSortTable'})
        tbody = table.find("tbody")
        if tbody:
            for row in tbody.find_all('tr'):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)
                    end_date = self.get_date(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text

            # Check description_url
            relative_url = title_tag.get('href')
            if relative_url:
                description_url = self.url.split(".nsf/")[0] + ".nsf/" + relative_url
                if description_url:
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'cssPageHeader'})
            if details_block:
                # Description contains an image, we don't want the information before that image since it is related to the company, not to the job
                has_to_save = False
                for tag in details_block.next_siblings:
                    if tag.name:
                        # description ends with a job table information
                        if tag.find('tr'):
                            break
                        if has_to_save:
                            for element in tag.find_all(True):
                                element.attrs = {}
                            description += str(tag)
                        if tag.find('img'):
                            has_to_save = True

        return description

    def get_date(self, item, title):
        end_date = None
        total_columns = len(item.find_all('td'))

        end_date_tag = item.find_all('td')[total_columns - 1]
        if end_date_tag:
            end_date_datetime = parser.parse(end_date_tag.text)
            end_date = end_date_datetime.strftime('%Y-%m-%d')
        else:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date

    def get_location(self, item, title):
        location = None
        first_td = item.find('td')

        if first_td:
            location_tag = first_td.find_next_sibling('td')
            if location_tag:
                location = location_tag.text
            else:
                log_support.set_invalid_location(self.client_name, title)

        return location


class Kone(Scraper):
    page_offset = 50

    def extract_info(self, html):
        # From API
        jobs = []
        last_page = False
        current_page = self.url
        current_offset = 0
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)
        total_jobs = self.get_total_jobs(json_dict)

        while not last_page:
            jobs_list = self.get_jobs_list(json_dict)
            if jobs_list:
                for item in jobs_list:
                    title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                    if is_finnish and self.is_valid_job(title, description_url, description):
                        # location has already being checked in get_mandatory_fields()
                        location = item["subtitles"][0]["instances"][0]["text"]
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

                current_page, current_offset = self.get_next_page(current_page, Kone.page_offset)
                if current_page and current_offset:
                    html = request_support.simple_get(current_page, accept_json=True)
                    json_dict = json.loads(html)
                else:
                    # in case of error, finish
                    last_page = True

            if not jobs_list or current_offset >= total_jobs:
                last_page = True

        return jobs

    def get_total_jobs(self, json_dict):

        try:
            total_jobs = json_dict["body"]["children"][0]["facetContainer"]["paginationCount"]["value"]
            # only the first page contains the proper number of jobs. Rest of them, this value is 0
        except (IndexError, KeyError, ValueError):
            total_jobs = 0
            log_support.set_error_message(self.client_name, "Can not get the total number of jobs")

        return total_jobs

    @staticmethod
    def get_jobs_list(json_dict):
        # Jobs list is in "json_dict["body"]["children"][0]["children"][0]["listItems"]"
        try:
            jobs_list = json_dict["body"]["children"][0]["children"][0]["listItems"]
        except (IndexError, KeyError, ValueError):
            jobs_list = []

        return jobs_list

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        locator = CityLocator()
        is_finnish = False

        if "title" in item and "instances" in item["title"] and len(item["title"]["instances"]) > 0 and "text" in item["title"]["instances"][0]:
            title = item["title"]["instances"][0]["text"]
            if "subtitles" in item and len(item["subtitles"]) > 0 and "instances" in item["subtitles"][0] and \
                    len(item["subtitles"][0]["instances"]) > 0 and "text" in item["subtitles"][0]["instances"][0]:
                location = item["subtitles"][0]["instances"][0]["text"]
                if locator.has_finnish_cities(location):
                    is_finnish = True
                    if "commandLink" in item["title"]:
                        relative_url = item["title"]["commandLink"]
                        description_url = self.url.split(".com/")[0] + ".com" + relative_url
                        description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(description_url):
        description = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                description = json_dict["body"]["children"][1]["children"][0]["children"][2]["text"]
            except (ValueError, KeyError, IndexError, AttributeError):
                try:
                    # Some jobs has the description in the children #3
                    description = json_dict["body"]["children"][1]["children"][0]["children"][3]["text"]
                except (ValueError, KeyError, IndexError, AttributeError):
                    description = ""

        return description

    def get_next_page(self, current_url, offset):
        try:
            result = re.search(r'/([0-9]+)\?clientRequestID', current_url)
            current_offset = result.group(1)
            new_offset = int(current_offset) + offset
            old_pattern = "/" + current_offset + "?clientRequestID"
            new_pattern = "/%d" % new_offset + "?clientRequestID"
            new_page = current_url.replace(old_pattern, new_pattern, 1)
        except Exception as e:
            new_page = new_offset = None
            log_support.set_error_message(self.client_name, "Can not get next page: " + str(e))

        return new_page, new_offset


class Smartly(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
            if is_finnish and self.is_valid_job(title, description_url, description):
                location = item["categories"]["location"]

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        is_finnish = False
        locator = CityLocator()

        if "text" in item:
            title = item["text"]
            if "categories" in item and "location" in item["categories"] and locator.has_finnish_cities(item["categories"]["location"]):
                is_finnish = True
                if "hostedUrl" in item:
                    description_url = item["hostedUrl"]
                    description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(description_url):
        description = ""
        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('div', {'class': 'section-wrapper page-full-width'})
            if description_block:
                for div in description_block.find_all('div'):
                    if div.attrs and 'last-section-apply' in div.attrs.get('class'):
                        break
                    div.attrs = {}
                    description += str(div)

        return description


class Cybercom(Scraper):

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

        # Check title
        title_span = item.find('span', attrs={'class': 'title'})
        if title_span:
            title = title_span.text

            # Check description_url
            url_span = item.find('a')
            if url_span:
                relative_url = url_span.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'body'})
            if details_block:
                p = details_block.find("p")
                if p:
                    p.attrs = {}
                    description += str(p)
                    for p in p.next_siblings:
                        p.attrs = {}
                        if p.find('img'):
                            continue
                        if p.name:
                            description += str(p)

        return description

    def get_location(self, item, title):
        location = None
        title_span = item.find('span', attrs={'class': 'title'})
        if title_span:
            location_span = title_span.find_next_sibling('span')
            if location_span:
                location = location_span.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Enfo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find("div", attrs={'class': 'career-results'})
        if jobs_div:
            for item in jobs_div.find_all('div', {'class': 'career-item'}):
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
        title_tag = item.find('div', attrs={'class': 'name'})
        if title_tag:
            title = title_tag.text

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            # Two kind of HTML: one with a div id="job-description" and other
            details_block = job_details_soup.find('div', attrs={'id': 'job-description'})
            if details_block:
                details_div = details_block.find('div')
                if details_div:
                    for child in details_div.children:
                        if child.name:
                            Scraper.clean_attrs(child)
                            description += str(child)
            else:
                details_block = job_details_soup.find('div', attrs={'class': 'col-xs-12 column'})
                if details_block:
                    Scraper.clean_attrs(details_block)
                    description = str(details_block)

        return description

    def get_location(self, item, title):
        location_div = item.find('div', attrs={'class': 'city'})
        if location_div:
            location = location_div.text
        else:
            log_support.set_invalid_location(self.client_name, title)
            location = None

        return location


class Sofigate(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        for item in soup.find_all('div', {'class': 'l-post-archive__item'}):
            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
            if is_finnish and self.is_valid_job(title, description_url, description):
                location = self.get_location(description)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        is_finnish = False

        location_tag = item.find('div', {'class': 'c-teaser__label'})
        if location_tag and "Finland" == location_tag.text:
            is_finnish = True
            # Check title
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.text

                # Check description_url
                description_url = title_tag.get('href')
                if description_url:
                    description = self.get_full_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'b-single-post__wrapper'})
            first_p = details_block.find('p')
            if first_p:
                Scraper.clean_attrs(first_p)
                description += str(first_p)
                for sibling in first_p.next_siblings:
                    if sibling.name:
                        # Button apply
                        if sibling.attrs and sibling.attrs.get('class') and 'c-btn' in sibling.attrs.get('class'):
                            break
                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class BlueMeteorite(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'class': 'articlelist__items'})
        if jobs_div:
            for item in jobs_div.find_all('div', {'class': 'articlelist__item'}):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text

            # Check description_url
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'entry__content'})
            if details_block:
                first_p = details_block.find('p')
                if first_p:
                    for child in first_p.find_all(True):
                        child.attrs = {}
                    description += str(first_p)

                    for sibling in first_p.next_siblings:
                        if sibling.name:
                            if sibling.attrs and ('getsocial' in sibling.attrs.get('class') or 'yuzo_related_post' in sibling.attrs.get('class')):
                                break
                            for child in sibling.find_all(True):
                                child.attrs = {}
                            description += str(sibling)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Sulava(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'class': 'vc_pageable-slide-wrapper'})
        if jobs_div:
            for item in jobs_div.find_all('div', {'class': 'vc_gitem-post-data-source-post_title'}):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text

            # Check description_url
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', attrs={'class': 'full_section_inner'})
            if details_block:
                title = details_block.find('h1')
                for sibling in title.next_siblings:
                    if sibling.name:
                        if sibling.name == "h3" and sibling.text.strip() == "Lisätietoja antaa":
                            break
                        if sibling.name == "blockquote":
                            continue

                        # Reduce size from paragraphs
                        if sibling.name == "h2":
                            sibling.name = "h4"
                        if sibling.name == "h3":
                            sibling.name = "h5"

                        if sibling.text != "\xa0":
                            description += str(sibling)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Nitor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'class': 'page-list-wrap'})
        if jobs_div:
            for item in jobs_div.find_all('div', {'class': 'section'}):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)
                    if not location:
                        # Nitor has a unique office located in Helsinki. If this information is not in the job description, we can hard-code it
                        location = "Helsinki"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h3', {'class': 'article__title'})
        if title_tag:
            title = title_tag.text.strip()

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                if description_url:
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            sections = job_details_soup.find_all('div', attrs={'class': 'section'})

            for section in sections:
                if section.find('div', {'class': 'row'}):
                    content = section.find('div', {'class': 'content-wrap'})
                    if content:
                        for child in content.children:
                            if child.name:
                                # Skip images
                                if child.find('img'):
                                    continue

                                # break in button
                                if child.find('a', {'class': 'button'}):
                                    break

                                child.attrs = {}
                                description += str(child)
                        # We only wants one iteration
                        break

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Softability(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        section_title = soup.find('h3', {'class': 'section-title'})
        if section_title:
            jobs_row = section_title.find_next_sibling('div', {'class': 'row'})
            if jobs_row:
                for item in jobs_row.children:
                    # First element is not a job but simple text and does not contain any link
                    if item.name and item.find('a'):
                        title, description_url, description = self.get_mandatory_fields(item)
                        if self.is_valid_job(title, description_url, description):
                            location = self.get_location(description)
                            if not location:
                                # Nitor has a unique office located in Vantaa. If this information is not in the job description, we can hard-code it
                                location = "Vantaa"

                            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                            jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # First element contains an image, second one contains the title
        first_p = item.find('p')
        if first_p:
            url_tag = first_p.find('a')
            if url_tag:
                description_url = url_tag.get('href')

            title_tag = first_p.find_next_sibling('p')
            if title_tag:
                title = title_tag.text.strip()

                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_block = job_details_soup.find('aside', attrs={'class': 'row-container'})

            if job_block:
                title_tag = job_block.find('h3')
                if title_tag:
                    if title_tag.name:
                        for sibling in title_tag.next_siblings:
                            if sibling != "\n":
                                description += str(sibling)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Fleetonomy(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        # Jobs appears withing a <p> tag with text "Now we are looking for:"
        p_tag = soup.find(self.find_jobs_tag)
        if p_tag:
            jobs_list = p_tag.find_all('a')
            for item in jobs_list:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    @staticmethod
    def find_jobs_tag(tag):
        return tag.name == 'p' and 'Now we are looking for:' in tag.text

    def get_mandatory_fields(self, item):
        title = None
        description = ""

        relative_url = item.get('href')
        description_url = self.url.split(".ai/")[0] + ".ai" + relative_url

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_block = job_details_soup.find('section', class_='Main-content')

            h2_tags = job_block.find_all('h2')
            # There are two H2 tags, the second one contains the title
            if len(h2_tags) == 2:
                title = h2_tags[1].text
                description = self.get_full_description(job_block)

        return title, description_url, description

    @staticmethod
    def get_full_description(job_block):
        description = ""

        description_blocks = job_block.find_all('div', class_="row")
        for block in description_blocks:
            first_p = block.find('p')
            if first_p:
                first_p.attrs = {}
                description += str(first_p)

                for tag in first_p.next_siblings:
                    tag.attrs = {}
                    description += str(tag)
            # Block #2 has three <h3> tags
            h3_tags = block.find_all('h3')
            for h3_tag in h3_tags:
                h3_tag.attrs = {}
                description += str(h3_tag)

                parent = h3_tag.parent
                if parent:
                    ul = parent.find('ul')
                    if ul:
                        ul.attrs = {}
                        for child in ul.find_all(True):
                            child.attrs = {}
                        description += str(ul)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Ubisoft(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_block = soup.find('div', class_='b-open-positions__content')
        if jobs_block:
            for item in jobs_block.find_all('div', class_="c-accordion__item"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)
                    if not location:
                        # Ubisoft has a unique office located in Helsinki. If this information is not in the job description, we can hard-code it
                        location = "Helsinki"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # First element contains an image, second one contains the title
        title_tag = item.find('div', class_='c-accordion__item-title')

        if title_tag:
            title = title_tag.text

            description_url_item = item.find('div', class_='c-accordion__item-button')
            if description_url_item:
                description_url_tag = description_url_item.find('a')
                if description_url_tag:
                    description_url = description_url_tag.get('href')

            description_tag = item.find('div', class_='c-accordion__item-content')
            if description_tag:
                description = self.get_full_description(description_tag)

        return title, description_url, description

    @staticmethod
    def get_full_description(description_tag):
        description = ""

        for block in description_tag.children:
            if block.name:
                for child in block.find_all(True):
                    child.attrs = {}

                if block.name == "div" and block.has_attr('class') and "c-accordion__item-button" in block['class']:
                    break

                description += str(block)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Remedy(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        positions = soup.find('div', class_='positions')
        if positions:
            for item in positions.find_all('a'):
                title, description_url, description, location = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""
        location = None

        title = item.text
        description_url = item.get('href')
        if description_url:
            description, location = self.get_full_description(description_url, title)

        return title, description_url, description, location

    def get_full_description(self, url, title):
        description = ""
        location = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('div', class_='section-wrapper page-full-width')
            for child in description_block.children:
                if child.name:
                    if child.name == "div" and child.has_attr('class') and "last-section-apply" in child['class']:
                        break

                    child.attrs = {}
                    for tag in child.find_all(True):
                        tag.attrs = {}

                    description += str(child)

            location = self.get_location(job_details_soup, title)

        return description, location

    def get_location(self, item, title):
        location = None
        location_tag = item.find('div', class_='posting-categories')
        if location_tag:
            location_div = location_tag.find('div', class_='sort-by-time')
            if location_div:
                location = location_div.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Paf(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        positions = soup.find_all('div', class_='job-opening')
        for item in positions:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)
                end_date = self.get_end_date(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h2", class_="job-title")
        if title_tag:
            title = title_tag.text

            url_div = item.find("div", class_="job-opening-toggle-meta")
            if url_div:
                url_tag = url_div.find("a")
                if url_tag:
                    description_url = url_tag.get('href')
                    description = self.get_full_description(item)

        return title, description_url, description

    @staticmethod
    def get_full_description(item):
        description = ""

        description_block = item.find('div', class_='job-opening-toggle-content-inner')
        for child in description_block.children:
            if child.name:
                child.attrs = {}
                for tag in child.find_all(True):
                    tag.attrs = {}

                if "Are you interested?" in child.text:
                    break
                if child.text != '\xa0':
                    description += str(child)

        return description

    def get_location(self, item, title):
        location = None
        location_tag = item.find('span', class_='job-location')
        if location_tag:
            # location_text is like "Location: Mariehamn"
            location_text = location_tag.text
            location_split = location_text.split(":")
            if len(location_split) == 2:
                location = location_split[1]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, url, title):
        end_date = None
        expected = True

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            date_div = job_details_soup.find('div', class_="duedate")
            if date_div:
                date_span = date_div.find('span')
                if date_span:
                    date_tag = date_span.find_next_sibling('b')
                    if date_tag:
                        date_raw = date_tag.text
                        try:
                            end_date_datetime = parser.parse(date_raw)
                            end_date = end_date_datetime.strftime('%Y-%m-%d')
                        except ValueError:
                            # Some jobs do not have end_date information  so scraper should not raise an error
                            expected = False

        if expected and not end_date:
            log_support.set_invalid_location(self.client_name, title)

        return end_date


class Fluido(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["posts"]:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "post_title" in item:
            title = item["post_title"]
            if "permalink" in item:
                description_url = item["permalink"]
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('article', class_='c-article')
            if details_block:
                for child in details_block.children:
                    if child.name:
                        child.attrs = {}
                        for tag in child.find_all(True):
                            tag.attrs = {}
                        if child.name == "h3":
                            child.name = "h5"
                        description += str(child)

        return description

    def get_location(self, url, title):
        location = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            location_div = job_details_soup.find('h5', string="Location")
            if location_div:
                location_tag = location_div.find_next_sibling("div")
                if location_tag:
                    location = location_tag.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Atea(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody')
        if table:
            for row in table.find_all("tr"):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)
                    end_date = self.get_end_date(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.text
            description_url = url_tag.get('href')
            description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('div', class_='jobDescription')
            if description_block:
                for child in description_block.children:
                    if child.name:
                        Scraper.clean_attrs(child)
                        if child.text != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location_tag = item.find('td', class_='jobtown')
        if location_tag:
            location = location_tag.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        date_div = item.find('td', class_="publishto")
        if date_div:
            date_span = date_div.find('span')
            if date_span:
                if date_span:
                    date_raw = date_span.text
                    try:
                        end_date_datetime = parser.parse(date_raw)
                        end_date = end_date_datetime.strftime('%Y-%m-%d')
                    except ValueError:
                        log_support.set_invalid_location(self.client_name, title)

        return end_date


class If(Scraper):
    page_offset = 50

    def extract_info(self, html):
        # From API
        jobs = []
        last_page = False
        current_page = self.url
        current_offset = 0
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)
        total_jobs = self.get_total_jobs(json_dict)

        while not last_page:
            jobs_list = self.get_jobs_list(json_dict)
            if jobs_list:
                for item in jobs_list:
                    title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                    if is_finnish and self.is_valid_job(title, description_url, description):
                        # location has already being checked in get_mandatory_fields()
                        location = item["subtitles"][0]["instances"][0]["text"]
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

                current_page, current_offset = self.get_next_page(current_page, If.page_offset)
                if current_page and current_offset:
                    html = request_support.simple_get(current_page, accept_json=True)
                    json_dict = json.loads(html)
                else:
                    # in case of error, finish
                    last_page = True

            if not jobs_list or current_offset >= total_jobs:
                last_page = True

        return jobs

    def get_total_jobs(self, json_dict):

        try:
            total_jobs = json_dict["body"]["children"][0]["facetContainer"]["paginationCount"]["value"]
            # only the first page contains the proper number of jobs. Rest of them, this value is 0
        except (IndexError, KeyError, ValueError):
            total_jobs = 0
            log_support.set_error_message(self.client_name, "Can not get the total number of jobs")

        return total_jobs

    @staticmethod
    def get_jobs_list(json_dict):
        # Jobs list is in "json_dict["body"]["children"][0]["children"][0]["listItems"]"
        try:
            jobs_list = json_dict["body"]["children"][0]["children"][0]["listItems"]
        except (IndexError, KeyError, ValueError):
            jobs_list = []

        return jobs_list

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        locator = CityLocator()
        is_finnish = False

        if "title" in item and "instances" in item["title"] and len(item["title"]["instances"]) > 0 and "text" in item["title"]["instances"][0]:
            title = item["title"]["instances"][0]["text"]
            if "subtitles" in item and len(item["subtitles"]) > 0 and "instances" in item["subtitles"][0] and \
                    len(item["subtitles"][0]["instances"]) > 0 and "text" in item["subtitles"][0]["instances"][0]:
                location = item["subtitles"][0]["instances"][0]["text"]
                if locator.has_finnish_cities(location):
                    is_finnish = True
                    if "commandLink" in item["title"]:
                        relative_url = item["title"]["commandLink"]
                        description_url = self.url.split(".com/")[0] + ".com" + relative_url
                        description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(description_url):
        description = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                description = json_dict["body"]["children"][1]["children"][0]["children"][2]["text"]
            except (ValueError, KeyError, IndexError, AttributeError):
                try:
                    # Some jobs has the description in the children #3
                    description = json_dict["body"]["children"][1]["children"][0]["children"][3]["text"]
                except (ValueError, KeyError, IndexError, AttributeError):
                    try:
                        # Some jobs has the description in the children #4
                        description = json_dict["body"]["children"][1]["children"][0]["children"][4]["text"]
                    except (ValueError, KeyError, IndexError, AttributeError):
                        description = ""

        # Remove <h1> from tag
        description_soup = BeautifulSoup(description, "html.parser")
        h1_tag = description_soup.find('h1')
        if h1_tag:
            h1_tag.extract()
            description = str(description_soup)

        return description

    def get_next_page(self, current_url, offset):
        try:
            result = re.search(r'/([0-9]+)\?clientRequestID', current_url)
            current_offset = result.group(1)
            new_offset = int(current_offset) + offset
            old_pattern = "/" + current_offset + "?clientRequestID"
            new_pattern = "/%d" % new_offset + "?clientRequestID"
            new_page = current_url.replace(old_pattern, new_pattern, 1)
        except Exception as e:
            new_page = new_offset = None
            log_support.set_error_message(self.client_name, "Can not get next page: " + str(e))

        return new_page, new_offset


class EpicGames(Scraper):
    page_offset = 50

    def extract_info(self, html):
        # From API
        jobs = []
        last_page = False
        current_page = self.url
        current_offset = 0
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)
        total_jobs = self.get_total_jobs(json_dict)

        while not last_page:
            jobs_list = self.get_jobs_list(json_dict)
            if jobs_list:
                for item in jobs_list:
                    title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                    if is_finnish and self.is_valid_job(title, description_url, description):
                        # location has already being checked in get_mandatory_fields()
                        location = self.get_location(description_url, title)
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

                current_page, current_offset = self.get_next_page(current_page, EpicGames.page_offset)
                if current_page and current_offset:
                    html = request_support.simple_get(current_page, accept_json=True)
                    json_dict = json.loads(html)
                else:
                    # in case of error, finish
                    last_page = True

            if not jobs_list or current_offset >= total_jobs:
                last_page = True

        return jobs

    def get_total_jobs(self, json_dict):

        try:
            total_jobs = json_dict["body"]["children"][0]["facetContainer"]["paginationCount"]["value"]
            # only the first page contains the proper number of jobs. Rest of them, this value is 0
        except (IndexError, KeyError, ValueError):
            total_jobs = 0
            log_support.set_error_message(self.client_name, "Can not get the total number of jobs")

        return total_jobs

    @staticmethod
    def get_jobs_list(json_dict):
        # Jobs list is in "json_dict["body"]["children"][0]["children"][0]["listItems"]"
        try:
            jobs_list = json_dict["body"]["children"][0]["children"][0]["listItems"]
        except (IndexError, KeyError, ValueError):
            jobs_list = []

        return jobs_list

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        locator = CityLocator()
        is_finnish = False

        if "title" in item and "instances" in item["title"] and len(item["title"]["instances"]) > 0 and "text" in item["title"]["instances"][0]:
            title = item["title"]["instances"][0]["text"]
            if "subtitles" in item and len(item["subtitles"]) > 0 and "instances" in item["subtitles"][0] and \
                    len(item["subtitles"][0]["instances"]) > 0 and "text" in item["subtitles"][0]["instances"][0]:
                location = item["subtitles"][0]["instances"][0]["text"]
                # JSON response can not contain all cities but just one or two and "More...". We need to check those in case some city is from Finland
                if locator.has_finnish_cities(location) or "More" in location:
                    is_finnish = True
                    if "commandLink" in item["title"]:
                        relative_url = item["title"]["commandLink"]
                        description_url = self.url.split(".com/")[0] + ".com" + relative_url
                        description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(description_url):
        description = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                for child in json_dict["body"]["children"][1]["children"][0]["children"]:
                    if "text" in child:
                        description = child["text"]
            except (ValueError, KeyError, IndexError, AttributeError):
                # Error message will be handled by "is_valid_job()" method
                pass

        description_soup = BeautifulSoup(description, "html.parser")
        Scraper.clean_attrs(description_soup)
        description = str(description_soup)

        return description

    def get_location(self, description_url, title):
        location = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                for child in json_dict["body"]["children"][1]["children"][0]["children"]:
                    if "imageLabel" in child:
                        location += child["imageLabel"] + ", "
            except (ValueError, KeyError, IndexError, AttributeError):
                pass

        if location == "":
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_next_page(self, current_url, offset):
        try:
            result = re.search(r'/([0-9]+)\?clientRequestID', current_url)
            current_offset = result.group(1)
            new_offset = int(current_offset) + offset
            old_pattern = "/" + current_offset + "?clientRequestID"
            new_pattern = "/%d" % new_offset + "?clientRequestID"
            new_page = current_url.replace(old_pattern, new_pattern, 1)
        except Exception as e:
            new_page = new_offset = None
            log_support.set_error_message(self.client_name, "Can not get next page: " + str(e))

        return new_page, new_offset


class Sanoma(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        for job_div in soup.find_all('div', class_="single-job"):
            title, description_url, description = self.get_mandatory_fields(job_div)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(job_div, title)
                end_date = self.get_date(job_div, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_div = item.find('h3')
        if title_div:
            title = title_div.text

            # Check description_url
            url_span = item.find('a')
            if url_span:
                description_url = url_span.get('href')
                if description_url:
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('main', class_='page-position')
            if details_block:
                # Find "Task description"
                first_tag = details_block.find("p")
                if first_tag:
                    description += str(first_tag)
                    for p in first_tag.next_siblings:
                        if p.name and p.name == "p" and p.text != '\xa0':
                            description += str(p)

        return description

    def get_date(self, item, title):
        end_date = None
        end_date_div = item.find('div', class_='single-job__deadline')
        if end_date_div:
            end_date_span = end_date_div.find("span", class_="single-job__value")
            if end_date_span:
                end_date_raw = end_date_span.text
                try:
                    pub_date_datetime = parser.parse(end_date_raw)
                    end_date = pub_date_datetime.strftime('%Y-%m-%d')
                except ValueError:
                    pass

        if not end_date:
            log_support.set_invalid_location(self.client_name, title)

        return end_date

    def get_location(self, item, title):
        location = None
        location_div = item.find('div', class_='single-job__location')
        if location_div:
            location_span = location_div.find("span", class_="single-job__value")
            if location_span:
                location = location_span.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Orion(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('tbody')
        if table:
            for row in table.find_all("tr"):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)
                    end_date = self.get_end_date(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.text
            description_url = url_tag.get('href')
            description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('div', class_='jobDescription')
            if description_block:
                for child in description_block.children:
                    if child.name:
                        Scraper.clean_attrs(child)
                        if child.text != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location_tag = item.find('td', class_='jobtown')
        if location_tag:
            location = location_tag.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        date_div = item.find('td', class_="publishto")
        if date_div:
            date_span = date_div.find('span')
            if date_span:
                if date_span:
                    date_raw = date_span.text
                    try:
                        end_date_datetime = parser.parse(date_raw)
                        end_date = end_date_datetime.strftime('%Y-%m-%d')
                    except ValueError:
                        log_support.set_invalid_location(self.client_name, title)

        return end_date


class Aktia(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        json_dict = json.loads(html)

        if "data" in json_dict:
            for item in json_dict["data"]:
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

        if "jobTitle" in item:
            title = item["jobTitle"]
            if "link" in item:
                description_url = item["link"]
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            table_body = soup.find('table')
            if table_body:
                tr_tag = table_body.find('tr')
                if tr_tag:
                    first_td = tr_tag.find('td')
                    if first_td:
                        description_block = first_td.find_next_sibling('td')
                        for child in description_block.children:
                            Scraper.clean_attrs(child)
                            description += str(child)

        return description

    def get_location(self, item, title):
        if "locations" in item and len(item["locations"]) > 0 and "city" in item["locations"][0]:
            location = item["locations"][0]["city"]
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        if "endDate" in item and "year" in item["endDate"] and "month" in item["endDate"] and "day" in item["endDate"]:
            end_date = item["endDate"]["year"] + "-" + str(item["endDate"]["month"] + 1) + "-" + item["endDate"]["day"]
        else:
            end_date = None
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class ManagementEvents(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        article = soup.find('article', class_='jv-page-body')
        if article:
            for row in article.find_all("tr"):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.text
            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split(".com/")[0] + ".com" + relative_url
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('div', class_='jv-job-detail-description')
            if description_block:
                for child in description_block.children:
                    Scraper.clean_attrs(child)
                    if child.name:
                        description += str(child)

        return description

    def get_location(self, item, title):
        location_tag = item.find('td', class_='jv-job-list-location')
        if location_tag:
            location = location_tag.text.strip().replace("\n", " ").replace(" ", "")
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location


class Holvi(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        section = soup.find('section', {'id': 'work-with-us'})
        if section:
            for row in section.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description_url, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.text
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            sections = job_details_soup.find_all('section', class_='section section--text')
            for section in sections:
                for child in section.children:
                    Scraper.clean_attrs(child)
                    if child.name:
                        if child.name == "h2":
                            child.name = "h4"
                        description += str(child)

        return description

    def get_location(self, description_url, title):
        location = None

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            section = job_details_soup.find('section', class_='section section--header')
            if section:
                location_tag = section.find('p', class_='meta')
                if location_tag:
                    location = location_tag.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Finitec(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        section = soup.find('div', {'id': 'vacancies'})
        if section:
            for row in section.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description_url, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title_raw = url_tag.text
            # Title has the published date, it must be removed. For instance "RELEASE MANAGER (06.03.2019)"
            pos = title_raw.rfind("(")
            if pos != "-1":
                title = title_raw[:pos].strip()
            else:
                title = title_raw

            description_url = url_tag.get('href')
            if description_url:
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_div = job_details_soup.find('div', class_='col col_wide')
            if job_div:
                title_tag = job_div.find('h3')
                if title_tag:
                    for sibling in title_tag.next_siblings:
                        Scraper.clean_attrs(sibling)
                        if sibling.name:
                            if sibling.name == "a":
                                continue
                            description += str(sibling)

        return description

    def get_location(self, description_url, title):
        location = None

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            location_tag = job_details_soup.find('p', class_='location')
            if location_tag:
                location = location_tag.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Ferratum(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', class_='section page-centered')
        if jobs_div:
            for row in jobs_div.find_all('div', class_='posting'):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_block = item.find("a", class_="posting-title")
        if url_block:
            url_tag = url_block.find('h5')
            if url_tag:
                title = url_tag.text
                description_url = url_block.get('href')
                if description_url:
                    description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_div = job_details_soup.find('div', class_='section-wrapper page-full-width')
            if job_div:
                for child in job_div.children:
                    if child.name and child.find('div', class_='last-section-apply'):
                        break

                    Scraper.clean_attrs(child)
                    if child.name:
                        description += str(child)

        return description

    def get_location(self, row, title):
        location = None

        location_tag = row.find('span', class_='sort-by-location')
        if location_tag:
            location = location_tag.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class BonGames(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'id': 'jobs-elem'})
        if jobs_div:
            for row in jobs_div.find_all('article', class_='newsfeed-item'):
                title, description_url, description = self.get_mandatory_fields(row)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_div = item.find('div', class_='entry-content')
        if title_div:
            title_tag = title_div.find('h3')
            if title_tag:
                title = title_tag.text
                url_tag = title_div.find('a')
                if url_tag:
                    description_url = url_tag.get('href')
                    if description_url:
                        description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            title_p = job_details_soup.find('h3')
            if title_p:
                for sibling in title_p.next_siblings:
                    if sibling.name and sibling.find('span', class_='date'):
                        continue

                    Scraper.clean_attrs(sibling)
                    if sibling.name:
                        description += str(sibling)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class Lightneer(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        jobs_div = soup.find('div', {'id': 'jobs'})
        if jobs_div:
            for row in jobs_div.find_all('div', class_='wpb_row vc_inner vc_row vc_row-fluid attched-false '):
                title, description_url, description, expected = self.get_mandatory_fields(row)
                if expected and self.is_valid_job(title, description_url, description):
                    location = self.get_location(row, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        # Item will be both valid jobs and divs without any job information. If there is no 'span', scraper must mark it as "not expected".
        expected = True

        title_span = item.find('span')
        if title_span:
            title_p = title_span.find('p')
            if title_p:
                title = title_p.text
                url_tag = item.find('a')
                if url_tag:
                    description_url = url_tag.get('href')
                    if description_url:
                        description = self.get_full_description(description_url)
        else:
            expected = False

        return title, description_url, description, expected

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            title_div = job_details_soup.find('div', class_='mk-page-section-wrapper')
            if title_div:
                for sibling in title_div.next_siblings:
                    Scraper.clean_attrs(sibling)
                    if sibling.name:
                        if sibling.text == "":
                            continue

                        # Remove 'svg' and 'a' tag
                        [s.extract() for s in sibling('svg')]
                        [s.extract() for s in sibling('a')]
                        [s.extract() for s in sibling('style')]

                        h2_tag = sibling.find("h2")
                        if h2_tag:
                            h2_tag.name = "h3"
                            h2_tag.string = h2_tag.text.strip().capitalize()
                        if sibling.name != "style" and sibling.text.replace("\n", "") != "":
                            description += str(sibling)

        description = description.replace("<br/>\n", " ")
        description = description.replace("\xa0", " ")

        return description

    def get_location(self, row, title):
        location = None

        title_span = row.find('span')
        if title_span:
            title_parent = title_span.parent
            if title_parent:
                title_sibling = title_parent.find_next_sibling('h2')
                if title_sibling:
                    location_span = title_sibling.find('span')
                    if location_span:
                        location_p = location_span.find('p')
                        if location_p:
                            location = location_p.text

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class UnityTechnologies(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        script = soup.find("script", {"type": "application/json"})
        if script:
            try:
                json_resp = json.loads(script.text)
                if "jobData" in json_resp and "jobs" in json_resp["jobData"]:
                    jobs_list = json_resp["jobData"]["jobs"]

                    for item in jobs_list:
                        if self.is_finnish(item):
                            title, description_url, description = self.get_mandatory_fields(item)
                            if self.is_valid_job(title, description_url, description):
                                # All its jobs are located in Helsinki, besides this has already being checked in "is_finnish()"
                                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                                jobs.append(job)

            except json.decoder.JSONDecodeError:
                log_support.set_error_message(self.client_name, "Invalid JSON message from HTML response")

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = False
        if "offices" in item and len(item["offices"]) > 0:
            for office in item["offices"]:
                if "name" in office:
                    if office["name"] == "Helsinki":
                        finnish = True
                        break

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "absolute_url" in item:
                description_url = item["absolute_url"]
                if "content" in item:
                    description_raw = item["content"].replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"')
                    soup = BeautifulSoup(description_raw, 'html.parser')
                    Scraper.clean_attrs(soup)
                    description = str(soup)

        return title, description_url, description


class FuturePlay(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        for job_div in soup.find_all('div', class_="positions__post"):
            title, description_url, description, expected = self.get_mandatory_fields(job_div)
            if expected and self.is_valid_job(title, description_url, description):
                location = self.get_location(description)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        expected = True

        # Check title
        title_div = item.find('h3')
        if title_div:
            title = title_div.text

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                if url_tag.text == "Contact us":
                    expected = False
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_full_description(description_url)

        return title, description_url, description, expected

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            details_block = job_details_soup.find('div', class_='content')
            if details_block:
                section = details_block.find("section")
                if section:
                    for tag in section.children:
                        if tag.name:
                            Scraper.clean_attrs(tag)
                            description += str(tag)

        return description

    @staticmethod
    def get_location(description):
        """
        It tries to get a Finnish city from the job description
        :param description: job description
        :return: Finnish cities as a String
        """
        locator = CityLocator()
        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(cities)
        else:
            location = None

        return location


class RedhillGames(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        block = soup.find('div', {"id": "comp-joer0a86"})
        for item in block.find_all('li'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_full_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_full_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            divs = job_details_soup.find_all('div', class_='txtNew')
            for div in divs:
                # There is only one valid div that contains the job description. It's defined by the "data-packed == False"
                if div.get('data-packed') == "false":
                    for tag in div.children:
                        if tag.name:
                            Scraper.clean_attrs(tag)
                            if tag.text != "\n" and tag.text != "\u200b" and tag.text != "\xa0":
                                description += str(tag)
                    break

        return description


class SeriouslyDigitalEntertainment(Scraper):
    base_url = "https://www.seriously.com/careers/"

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                if "location" in item and "city" in item["location"]:
                    location = item["location"]["city"]
                else:
                    location = None
                    log_support.set_invalid_location(self.client_name, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "id" in item:
                description_url = self.base_url + "#op-" + str(item["id"]) + "-" + "-".join(title.split())

                # check description_url is valid
                resp = request_support.simple_get(description_url)
                if resp:
                    description_raw = item["description"]
                    soup = BeautifulSoup(description_raw, "html.parser")
                    Scraper.clean_attrs(soup)
                    description = str(soup)

        return title, description_url, description


class Housemarque(Scraper):
    base_url = "https://housemarque.com/careers/"

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description, expected = self.get_mandatory_fields(item)
            if expected and self.is_valid_job(title, description_url, description):
                if "location" in item and "city" in item["location"]:
                    location = item["location"]["city"]
                else:
                    location = None
                    log_support.set_invalid_location(self.client_name, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        expected = True

        if "team" in item and item["team"] == "Submit Open Application":
            expected = False
        elif "title" in item:
            title = item["title"]
            if "id" in item:
                description_url = self.base_url + "#op-" + str(item["id"]) + "-" + "-".join(title.split())

                # check description_url is valid
                resp = request_support.simple_get(description_url)
                if resp:
                    description_raw = item["description"]
                    soup = BeautifulSoup(description_raw, "html.parser")
                    Scraper.clean_attrs(soup)
                    description = str(soup)

        return title, description_url, description, expected


class HatchEntertainmentOy(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="job"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # Jobs do not show any location information but their office is in Espoo
                location = "Espoo"
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()
            description_url = title_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            block = job_details_soup.find('div', class_='hatch-sp-content')
            if block:
                for child in block.children:
                    if isinstance(child, Tag) and child.has_attr('class') and "career-perks" in child['class']:
                        break

                    Scraper.clean_attrs(child)
                    description += str(child)

        return description


class Qentinel(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "data" in json_dict:
            for item in json_dict["data"]:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    # location information is not in 'data' but in 'included'
                    location = self.get_location(json_dict, title)
                    end_date = self.get_end_date(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "attributes" in item and "title" in item["attributes"]:
            title = item["attributes"]["title"]
            if "links" in item and "careersite-job-url" in item["links"]:
                description_url = item["links"]["careersite-job-url"]

                # check description_url is valid
                request_support.simple_get(description_url)
                description = item["attributes"]["body"]

        return title, description_url, description

    def get_location(self, item, title):
        location = None

        if "included" in item:
            for child in item["included"]:
                if child["type"] == "locations":
                    if "attributes" in child and "city" in child["attributes"]:
                        location = child["attributes"]["city"]
                        break

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "end-date" in item["attributes"]:
            end_date_raw = item["attributes"]["end-date"]
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError) as e:
                log_support.set_error_message(self.client_name, "Invalid date string " + str(e))

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Intopalo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="careers-heading"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # Jobs do not show any location information but their office is in Espoo
                location = "Tampere"
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description_url = None
        description = ""

        # Check title
        title = item.text
        url_tag = item.find_previous_sibling('a')
        if url_tag:
            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')
            block = job_details_soup.find('div', class_='text-primary')
            if block:
                for child in block.children:
                    if isinstance(child, Tag) and child.has_attr('class') and "reference-title" in child['class']:
                        child.name = "h3"

                    Scraper.clean_attrs(child)
                    description += str(child).strip()

        return description


class Reaktor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('a', class_="filter-helsinki"):
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
        title_tag = item.find('h2')
        if title_tag:
            title = title_tag.get_text().strip()

            description_url = item.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            # Two blocks, the first one contains nothing.
            blocks = job_details_soup.find_all('div', class_='blog-copy')
            for block in blocks:
                if block.find('p'):
                    for child in block.children:
                        Scraper.clean_attrs(child)
                        description += str(child).strip()
                    break

        return description

    def get_location(self, item, title):
        location = None

        all_span = item.find_all('span')

        last_span = None
        for last_span in all_span:
            pass

        if last_span:
            location = last_span.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Bittium(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="openjob"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)
                end_date = self.get_end_date(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        url_tag = item.find('a')
        if url_tag:
            description_url = url_tag.get('href')
            title = url_tag.get_text().strip()

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html5lib')

            # Two blocks, the first one contains nothing.
            block = job_details_soup.find('div', {'id': 'left70'})
            if block:
                for child in block.children:
                    Scraper.clean_attrs(child)
                    if isinstance(child, Tag):
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find_previous_sibling('h3')
        if location_tag:
            location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, url, title):
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html5lib')

            date_label = job_details_soup.find(lambda tag: tag.name == "b" and "Last apply date:" in tag.text)
            if date_label:
                date_tag = date_label.next_sibling
                if date_tag:
                    try:
                        date_raw = date_tag.strip()
                        end_date = parser.parse(date_raw, dayfirst=True).strftime('%Y-%m-%d')
                    except (ValueError, TypeError) as e:
                        log_support.set_error_message(self.client_name, "Invalid date string " + str(e))

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Accenture(Scraper):

    # POST request to https://www.accenture.com/fi-en/careers/jobsearchkeywords.query with a specific body (See https://www.accenture.com/fi-en/careers/jobsearch)

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []

        post_url = "https://www.accenture.com/fi-en/careers/jobsearchkeywords.query"
        body = {
            "f": 1,
            "s": 24,
            "k": "",
            "lang": "en",
            "cs": "fi-en",
            "df": "[{\"metadatafieldname\":\"location\",\"items\":[]},"
                  "{\"metadatafieldname\":\"skill\",\"items\":[]},"
                  "{\"metadatafieldname\":\"jobTypeDescription\",\"items\":[]},"
                  "{\"metadatafieldname\":\"orgUnitLevel1Desc\",\"items\":[]},"
                  "{\"metadatafieldname\":\"orgUnitLevel2Desc\",\"items\":[]}]",
            "c": "Finland",
            "sf": 1,
            "syn": False,
            "isPk": False,
            "wordDistance": 0,
            "userId": ""
        }

        html = request_support.simple_post(post_url, body)
        if html:
            json_dict = json.loads(html)
            if "documents" in json_dict:
                for item in json_dict["documents"]:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "jobDetailUrl" in item:
                description_url = item["jobDetailUrl"]
                if "jobDescription" in item:
                    description_raw = item["jobDescription"]
                    soup = BeautifulSoup(description_raw, 'html.parser')
                    Scraper.clean_attrs(soup)

                    font = soup.find('font')
                    if font:
                        soup.font.unwrap()

                    for tag in soup.children:
                        if tag.name and tag.text != "\n" and tag.text != "\xa0" and tag.text != "":
                            description += str(tag)

        return title, description_url, description

    def get_location(self, item, title):
        locations = []
        location = None

        if "location" in item:
            for location in item["location"]:
                locations.append(location)

        if locations:
            location = ", ".join(locations)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Napa(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_="b-open-positions__item"):
            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
            if is_finnish and self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                # it returns also the 'job_details_html' to save an request call in get_job_type()
                end_date, job_details_html = self.get_end_date(description_url, title)
                job_type = self.get_job_type(job_details_html)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        locator = CityLocator()
        is_finnish = False

        title_tag = item.find('h4')
        if title_tag:
            title = title_tag.get_text()
            location_tag = item.find('h5')
            if location_tag:
                is_finnish = locator.has_finnish_cities(location_tag.text)
                if is_finnish:
                    url_tag = item.find('a')
                    if url_tag:
                        description_url = url_tag.get('href')
                        if description_url:
                            description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            # Two blocks, the first one contains nothing.
            block = job_details_soup.find('article', class_="c-article")
            if block:
                for child in block.children:
                    if isinstance(child, Tag):
                        if child.name == "h3" and "how to apply" in child.text.lower():
                            break
                        if child.has_attr('class') and "gform_wrapper" in child['class']:
                            break

                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('h5')
        if location_tag:
            location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, url, title):
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            block = job_details_soup.find("div", class_="c-feature-list")
            if block:
                date_label = block.find("dt", string="Application Deadline")
                if date_label:
                    try:
                        date_tag = date_label.find_next_sibling('dd')
                        if date_tag:
                            date_raw = date_tag.get_text().strip()
                            end_date = parser.parse(date_raw).strftime('%Y-%m-%d')
                    except (ValueError, TypeError) as e:
                        log_support.set_error_message(self.client_name, "Invalid date string " + str(e))

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date, job_details_html

    @staticmethod
    def get_job_type(job_details_html):
        job_type = None

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            block = job_details_soup.find("div", class_="c-feature-list")
            if block:
                job_type_label = block.find("dt", string="Type of Employment")
                if job_type_label:
                    job_type_tag = job_type_label.find_next_sibling('dd')
                    if job_type_tag:
                        job_type = job_type_tag.get_text().strip()

        return job_type


class AjrSolutions(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('article', class_="content-careers"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):

                job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h2', class_="entry-title")
        if title_tag:
            url_tag = title_tag.find('a')
            if url_tag:
                title = url_tag.get_text()
                description_url = url_tag.get('href')

                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            block = job_details_soup.find('div', class_='entry-content')

            if block.find('p'):
                for child in block.children:
                    Scraper.clean_attrs(child)
                    description += str(child).strip()

        return description


class Anders(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_="single-position"):
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
        title_tag = item.find('h3', class_="position-title")
        if title_tag:
            title = title_tag.get_text().strip()
            div_tag = item.find('div', class_='apply-link-container')
            if div_tag:
                url_tag = div_tag.find('a')
                if url_tag:
                    description_url = url_tag.get('href')

                    if description_url:
                        description = self.get_description(item)

        return title, description_url, description

    @staticmethod
    def get_description(item):
        description = ""

        block = item.find('div', class_='position-details-inner')
        if block:
            first_p = block.find('p')
            if first_p:
                for tag in first_p.next_siblings:
                    if isinstance(tag, Tag):
                        if tag.has_attr('class') and "apply-link-container" in tag['class']:
                            break

                        Scraper.clean_attrs(tag)
                        description += str(tag).strip()

        return description

    def get_location(self, item, title):
        locations = []
        location = None

        location_tag = item.find('div', class_='position-location')
        if location_tag:
            for loc in location_tag.find_all('span'):
                locations.append(loc.get_text().strip())

        if locations:
            location = ", ".join(locations)
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class SmallGiantGames(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('div', class_="collection-list-wrapper")
        for item in jobs_div.find_all('div', class_="w-dyn-item"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):

                # Jobs do no have information about the location but the company is based on Helsinki
                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h3', class_="heading-2")
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            block = job_details_soup.find('div', class_='rich-text-block')

            if block:
                for tag in block.children:
                    if isinstance(tag, Tag):
                        if tag.has_attr('class') and "apply-link-container" in tag['class']:
                            break

                        Scraper.clean_attrs(tag)
                        description += str(tag).strip()

        return description
