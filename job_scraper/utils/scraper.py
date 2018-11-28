from bs4 import BeautifulSoup
import dateutil.parser as parser
from dateutil import tz
import json
import time

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

        paragraph = details_block.find("p")
        while True:
            if paragraph is None:
                break
            if paragraph.name and paragraph.name != "p":
                break

            description += str(paragraph)
            paragraph = paragraph.next_sibling

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
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title = item["title"]
            description = item["jobDescription"]

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
        items = section.find_all("a")
        for item in items:
            title = item.find("h4", attrs={'class': 'title'}).text
            # Vala has a list of jobs. Last item from the list is not a job a an applicatin form. Loop must skip here
            if title == "Open Application":
                break
            relative_url = item['href']
            full_url = self.url + relative_url
            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_bock = soup.find('div', attrs={'class': 'column_attr clearfix'})

            description = ""
            for tag in details_bock.find("h1").next_siblings:
                if tag.name == "h4" and tag.text.strip() == "Interested?":
                    break
                if tag != "\n":
                    description += str(tag)

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
            if title == "Open Application":
                continue
            location = item.find("div", attrs={'class': 'job-ad__office--listing'}).text.strip()
            relative_url = item.find("a")['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url

            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description = ""
            job_description = soup.find('div', attrs={'class': 'job-ad__description'}).find_all(["p", "h3"])
            for tag in job_description:
                if tag.name == "h3" and "interested?" in tag.text.lower():
                    break
                if tag != "\n" and tag.text != "":
                    description += str(tag)

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs


class Innofactor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        lis = ul.find_all('li')
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
            description = ""
            description_block = soup.find('div', attrs={'class': 'body'})
            paragraphs = description_block.find_all("p")
            for p in paragraphs:
                if p.name == "p":
                    description += str(p)

            job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs


class Smarp(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        lis = ul.find_all('li')
        for li in lis:
            title = li.find("span", {"class": "title"}).text
            relative_url = li.find('a')['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url

            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            location = self.get_location(soup, title)

            description = ""
            description_block = soup.find('div', attrs={'class': 'body'})
            paragraphs = description_block.find_all("p")
            for p in paragraphs:
                if p.name == "p":
                    description += str(p)

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs

    def get_location(self, soup, job_title):
        location = None
        try:
            location_block = soup.find('h2', attrs={'class': 'byline'}).text
            location = location_block.split("–")[1].strip()
        except:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Silo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", attrs={'class': 'elementor-icon-box-content'})
        for job_div in job_divs:
            title = job_div.find("h3").text.strip()
            url = job_div.find("a")["href"]

            # Get job details
            job_details_html = request_support.simple_get(url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            location = self.get_location(soup, title)

            description = ""
            description_div = soup.find("div", {'class': 'text-body'}).find_all(["p", "ul"])
            for div in description_div:
                description += str(div)

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, url)
            jobs.append(job)

        return jobs

    def get_location(self, soup, job_title):
        location = None
        try:
            location_block = soup.find('div', attrs={'class': 'pill blue'}).text
            location = location_block.split(", ")[1].strip()
        except:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Abb(Scraper):

    def extract_info(self, html):
        # From API
        log_support.log_extract_info(self.client_name)
        jobs = []
        json_dict = json.loads(html)

        for item in json_dict["Items"]:
            title = item["Title"].strip()

            location = None
            if "AddressLocality" in item["JobLocation"] and item["JobLocation"]["AddressLocality"] and item["JobLocation"]["AddressLocality"] != "":
                location = item["JobLocation"]["AddressLocality"]

            end_date = self.get_end_date(item["ValidThrough"])

            job_type = None
            if "Name" in item["FunctionalArea"] and item["FunctionalArea"]["Name"] and item["FunctionalArea"]["Name"] != "":
                job_type = item["FunctionalArea"]["Name"]

            relative_url = item["Url"]
            full_url = self.url.split("jobs/")[0] + "jobs/details" + relative_url

            # Get job details
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description = ""
            task_item = soup.find("h3", string='Tasks:')
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

            job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, full_url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_end_date(date_field):
        # Formatted as "/Date(1544313600000)/"
        epoch = date_field.split("(")[1].split(")")[0]
        seconds = int(epoch[:-3])
        date_string = time.strftime('%Y-%m-%d', time.gmtime(seconds))
        return date_string


class Qvik(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", attrs={'class': 'boxes-col'})

        for job_div in job_divs:
            title = job_div.find('h3').text
            url = job_div.find('a')['href']

            # Get job details
            description = ""
            job_details_html = request_support.simple_get(url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find("div", attrs={'class': 'article-container'})

            for p in description_div.find_all('p'):
                description += str(p)

            # Qvik has their office in Helsinki but that information does not appear in the HTML tag from their careers.
            job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, url)
            jobs.append(job)

        return jobs


class Blueprint(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", attrs={'class': 'jobs'})
        lis = ul.find_all('li')
        for li in lis:
            title = li.find('span', attrs={'class': 'title'}).text
            if "open application" in title.lower():
                continue
            location = self.get_location(li, title)
            relative_url = li.find("a")['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url

            # Get job details
            description = ""
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'body'})

            for p in description_div.find('p').next_siblings:
                description += str(p)

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs

    def get_location(self, li, job_title):
        location = None
        try:
            location_block = li.find('span', attrs={'class': 'meta'}).text
            location = location_block.split("–")[1].strip()
        except:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Eficode(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for job_div in soup.find_all('div', {'class': 'job-ad'}):
            title = job_div.find('a').text
            relative_url = job_div.find('a')['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url
            location = self.get_location(job_div, title)

            # Get job details
            description = ""
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'jd-description'})

            for p in description_div.find('h1').next_siblings:
                p.attrs = {}
                if p != "\n":
                    for match in p.find_all('span'):
                        match.unwrap()
                    description += str(p)

            job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, full_url)
            jobs.append(job)

        return jobs

    def get_location(self, job_div, job_title):
        location = None
        try:
            location_block = job_div.find('p')
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

        except:
            log_support.set_invalid_location(self.client_name, job_title)

        return location


class Ericsson(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["jobs"]:
            title = item["data"]["title"]
            description = item["data"]["description"]
            location = item["data"]["city"]
            pub_date = self.get_pub_date(item["data"]["create_date"])
            url = item["data"]["meta_data"]["canonical_url"]

            job = ScrapedJob(title, description, location, self.client_name, None, pub_date, None, None, url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_pub_date(created_date):
        return parser.parse(created_date).strftime('%Y-%m-%d')


class Varjo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        job_divs = soup.find_all('div', {'class': 'jobs-list'})
        for job_div in job_divs:
            for item in job_div.find_all("a"):
                title = item.find('span', {'class': 'jobs-position-title'}).text
                location = item.find('span', {'class': 'jobs-position-location'}).text
                url = item['href']

                # Get job details
                description = ""
                job_details_html = request_support.simple_get(url)
                soup = BeautifulSoup(job_details_html, 'html.parser')
                description_div = soup.find('div', {'class': 'jobs-override'})

                first_paragraph = description_div.find("p")
                for p in first_paragraph.next_siblings:
                    description += str(p)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, url)
                jobs.append(job)

        return jobs


class Telia(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict["vacancies"]:
            if "Finland" not in item["countries"]:
                continue
            title = item["title"]
            location = self.get_location(item)

            description = item["additionalJobDescription"]
            try:
                pub_date = item["startDate"]
            except KeyError:
                pub_date = None
            try:
                end_date = item["applicationDeadline"]
            except KeyError:
                end_date = None
            try:
                job_type = item["positionType"]
            except KeyError:
                job_type = None

            url = item["vacancyUrl"]

            job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, job_type, url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_location(item):
        location = None
        if len(item["locations"]) > 0:
            location = ', '.join(item["locations"])

        return location


class Wartsila(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', {'id': 'searchresults'})
        table_body = table.find('tbody')
        for item in table_body.find_all("tr"):
            title = item.find('a').text
            relative_url = item.find('a')['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url
            location = item.find('span', {'class': 'jobLocation'}).text.strip()
            pub_date = item.find('span', {'class': 'jobDate'}).text.strip()
            pub_date_formatted = self.get_pub_date(pub_date)

            # Get job details
            description = ""
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('span', {'itemprop': 'description'})
            for p in description_div.children:
                # remove tag attributes
                p.attrs = {}
                if p != "\n" and p.text.strip() != "":
                    for match in p.find_all('span'):
                        match.unwrap()
                    description += str(p)

            job = ScrapedJob(title, description, location, self.client_name, None, pub_date_formatted, None, None, full_url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_pub_date(pub_date):
        return parser.parse(pub_date).strftime('%Y-%m-%d')


class Nordea(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_div = soup.find('div', {'class': 'jobs-results'})

        for item in jobs_div.find_all('tr', {'class': 'job-item'}):
            title = item.find('a').text
            relative_url = item.find('a')['href']
            full_url = self.url.split("com/")[0] + "com" + relative_url
            location_tag = item.find('td', {'class': 'text--left'}).next_sibling
            location = location_tag.text
            end_date_tag = location_tag.next_sibling
            end_date = end_date_tag.text

            # Get job details
            description = ""
            job_details_html = request_support.simple_get(full_url)
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('div', {'class': 'job--content'})
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

            job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, full_url)
            jobs.append(job)

        return jobs

    @staticmethod
    def get_p_tag_from_div(soup, div):
        if div.text == '\xa0':
            return ""
        new_tag = soup.new_tag('p')
        new_tag.string = div.text.strip()
        div.replace_with(new_tag)
        return str(new_tag)


class Tieto(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        job_div = soup.find('div', {'class': 'listingResults'})

        while True:
            for item in job_div.find_all('a'):
                if not item.find('div', {'class': 'col-md-4'}):
                    break
                title = item.find('div', {'class': 'col-md-4'}).text.strip()
                print(title)

                relative_url = item['href']
                full_url = self.url.split("com/")[0] + "com" + relative_url
                location = self.get_location(item)

                # Get job details
                description = ""
                job_details_html = request_support.simple_get(full_url)
                description_soup = BeautifulSoup(job_details_html, 'html.parser')
                description_div = description_soup.find('div', {'class': 'infobox'})
                pub_date, end_date = self.get_dates(title, description_div)

                for p in description_div.next_siblings:
                    if p.name and p.text.lower() == "about tieto":
                        break
                    if p != "\n":
                        description += str(p)

                job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, None, full_url)
                jobs.append(job)

            # Get more jobs
            more_jobs = job_div.find('div', {'class': 'row align-content-center loadingOverlay'})
            if more_jobs:
                try:
                    more_jobs_url = more_jobs.find('a')['data-url']
                    full_more_jobs_url = self.url.split("com/")[0] + "com" + more_jobs_url
                    more_jobs_html = request_support.simple_get(full_more_jobs_url)
                    job_div = BeautifulSoup(more_jobs_html, 'html.parser')
                except Exception:
                    break
            else:
                break

        return jobs

    @staticmethod
    def get_location(item):
        # last div contains the location
        div_list = item.find_all('div', {'class': 'col-md-4'})
        last_div = None
        location = None

        for last_div in div_list:
            pass
        if last_div:
            location = last_div.text.strip()

        return location

    def get_dates(self, title, div):
        try:
            dates_string = div.find('label', string='Appliation period:').parent.text
            dates = dates_string.split(":")[1]
            pub_date = dates.split(" - ")[0]
            pub_date_formatted = parser.parse(pub_date).strftime('%Y-%m-%d')
            end_date = dates.split(" - ")[1]
            end_date_formatted = parser.parse(end_date).strftime('%Y-%m-%d')
            return pub_date_formatted, end_date_formatted
        except IndexError:
            log_support.set_invalid_dates(self.client_name, title)
            return None, None


class Rightware(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_div = soup.find_all('div', {'class': 'vacancy-module'})
        for job_div in jobs_div:
            title = self.get_title(job_div)
            if title:
                url = job_div.find('a')['href']
                if "https://" not in url:
                    url = self.url.split("com/")[0] + "com" + url
                location = self.get_location(job_div, title)
                description = self.get_description(url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, url)
                jobs.append(job)

        return jobs

    def get_title(self, div):
        title = None
        title_div = div.find('a')
        if title_div:
            title = title_div.text.strip()
        else:
            log_support.set_invalid_title(self.client_name)

        return title

    def get_location(self, div, title):
        location = None
        location_p = div.find('p', {'class': 'vacancy-location'})
        if location_p:
            location = location_p.text.strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_description(self, url, title):
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

        if description == "":
            log_support.set_invalid_description(self.client_name, title)

        return description

    @staticmethod
    def is_apply_block(tag):
        h_tags = ["h1", "h2", "h3", "h4", "h5", "h6"]
        return tag.name in h_tags and "apply" in tag.text.lower()
