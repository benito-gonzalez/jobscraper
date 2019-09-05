from bs4 import Tag, BeautifulSoup
import re
import dateutil.parser as parser
import urllib.parse
from dateutil import tz
from datetime import datetime, timedelta
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
    if client_name.lower() == "signant health":
        return SignantHealth(client_name, url)
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
    if client_name == "Oura":
        return Oura(client_name, url)
    if client_name == "Matchmade":
        return Matchmade(client_name, url)
    if client_name == "ultimate.ai":
        return Ultimate(client_name, url)
    if client_name == "Yousician":
        return Yousician(client_name, url)
    if client_name == "Leadfeeder":
        return Leadfeeder(client_name, url)
    if client_name == "ZenRobotics":
        return ZenRobotics(client_name, url)
    if client_name == "Callstats.io":
        return Callstats(client_name, url)
    if client_name == "Bitbar":
        return Bitbar(client_name, url)
    if client_name == "Aiven":
        return Aiven(client_name, url)
    if client_name == "SSH Communications Security":
        return SSHCommunicationsSecurity(client_name, url)
    if client_name == "Vizor":
        return Vizor(client_name, url)
    if client_name == "Frosmo":
        return Frosmo(client_name, url)
    if client_name == "Supermetrics":
        return Supermetrics(client_name, url)
    if client_name == "Taiste":
        return Taiste(client_name, url)
    if client_name == "Autori Oy":
        return Autori(client_name, url)
    if client_name == "720 Degrees Oy":
        return Degrees(client_name, url)
    if client_name == "Umbra":
        return Umbra(client_name, url)
    if client_name == "Lumoame Oy":
        return Lumoame(client_name, url)
    if client_name == "Screenful Oy":
        return Screenful(client_name, url)
    if client_name == "Sujuwa Group":
        return Sujuwa(client_name, url)
    if client_name == "Vaana":
        return Vaana(client_name, url)
    if client_name == "IWA":
        return Iwa(client_name, url)
    if client_name == "Nico":
        return Nico(client_name, url)
    if client_name == "Bitwise":
        return Bitwise(client_name, url)
    if client_name == "Solteq":
        return Solteq(client_name, url)
    if client_name == "Alphasense":
        return Alphasense(client_name, url)
    if client_name == "University of Turku":
        return UniversityTurku(client_name, url)
    if client_name == "University of Helsinki":
        return UniversityHelsinki(client_name, url)
    if client_name == "University of Jyväskylä":
        return UniversityJyvaskyla(client_name, url)
    if client_name == "Aalto University":
        return UniversityAalto(client_name, url)
    if client_name == "Tampere University":
        return UniversityTampere(client_name, url)
    if client_name == "University of Oulu":
        return UniversityOulu(client_name, url)
    if client_name == "Teleste Corporation":
        return Teleste(client_name, url)
    if client_name == "Visma":
        return Visma(client_name, url)
    if client_name == "Forenom":
        return Forenom(client_name, url)
    if client_name == "Bitville":
        return Bitville(client_name, url)
    if client_name == "Varian Medical Systems":
        return VarianMedicalSystems(client_name, url)
    if client_name == "Valmet":
        return Valmet(client_name, url)
    if client_name == "Metso":
        return Metso(client_name, url)
    if client_name == "Nokian Tyres":
        return NokianTyres(client_name, url)
    if client_name == "Meyer Turku":
        return MeyerTurku(client_name, url)
    if client_name == "Elomatic":
        return Elomatic(client_name, url)
    if client_name == "Almaco":
        return Almaco(client_name, url)
    if client_name == "Vapo":
        return Vapo(client_name, url)
    if client_name == "Alma Media":
        return AlmaMedia(client_name, url)
    if client_name == "Pöyry":
        return Poyry(client_name, url)
    if client_name == "UPM":
        return UPM(client_name, url)
    if client_name == "Mirum":
        return Mirum(client_name, url)
    if client_name == "Krogerus":
        return Krogerus(client_name, url)
    if client_name == "Siemens":
        return Siemens(client_name, url)
    if client_name == "Posti":
        return Posti(client_name, url)
    if client_name == "Attendo":
        return Attendo(client_name, url)
    if client_name == "Caverion":
        return Caverion(client_name, url)
    if client_name == "Canter":
        return Canter(client_name, url)
    if client_name == "Gapps":
        return Gapps(client_name, url)
    if client_name == "Profit Software":
        return ProfitSoftware(client_name, url)
    if client_name == "Innokas medical":
        return InnokasMedical(client_name, url)
    if client_name == "Tikkurila":
        return Tikkurila(client_name, url)
    if client_name == "Frogmind":
        return Frogmind(client_name, url)
    if client_name == "Zynga":
        return Zynga(client_name, url)
    if client_name == "Thermofisher":
        return Thermofisher(client_name, url)
    if client_name == "SAP SE":
        return Sap(client_name, url)
    if client_name == "Here":
        return Here(client_name, url)
    if client_name == "AGCO":
        return Agco(client_name, url)
    if client_name == "Open text":
        return OpenText(client_name, url)
    if client_name == "Danfoss":
        return Danfoss(client_name, url)
    if client_name == "Accountor":
        return Accountor(client_name, url)
    if client_name == "Iceye":
        return Iceye(client_name, url)
    if client_name == "Digia":
        return Digia(client_name, url)
    if client_name == "BDS-Bynfo":
        return BdsBynfo(client_name, url)
    if client_name == "BookIT":
        return BookIt(client_name, url)
    if client_name == "Enfuce":
        return Enfuce(client_name, url)
    if client_name == "Giosg":
        return Giosg(client_name, url)
    if client_name == "Inderes":
        return Inderes(client_name, url)
    if client_name == "LVS Brokers":
        return LvsBrokers(client_name, url)
    if client_name == "OpusCapita Solutions":
        return OpusCapitaSolutions(client_name, url)
    if client_name == "Poolia":
        return Poolia(client_name, url)
    if client_name == "SuoraTyö":
        return SuoraTyo(client_name, url)
    if client_name == "Tomorrow Tech":
        return TomorrowTech(client_name, url)
    if client_name == "Vauraus":
        return Vauraus(client_name, url)
    if client_name == "Nixu":
        return Nixu(client_name, url)
    if client_name == "Terveystalo":
        return Terveystalo(client_name, url)
    if client_name == "Zervant":
        return Zervant(client_name, url)
    if client_name == "Helvar":
        return Helvar(client_name, url)
    if client_name == "VTT":
        return VTT(client_name, url)
    if client_name == "Metsa":
        return Metsa(client_name, url)
    if client_name == "M-Files":
        return MFiles(client_name, url)
    if client_name == "U-Blox":
        return UBlox(client_name, url)
    if client_name == "Ubisecure":
        return Ubisecure(client_name, url)
    if client_name == "Fluent":
        return Fluent(client_name, url)
    if client_name == "Nortal":
        return Nortal(client_name, url)
    if client_name == "UL":
        return Ul(client_name, url)
    if client_name == "Fira":
        return Fira(client_name, url)
    if client_name == "GE":
        return GE(client_name, url)
    if client_name == "IQVIA":
        return IQVIA(client_name, url)
    if client_name == "Intel":
        return Intel(client_name, url)
    if client_name == "Oracle":
        return Oracle(client_name, url)
    if client_name == "Documill":
        return Documill(client_name, url)
    if client_name == "Elektrobit":
        return Elektrobit(client_name, url)
    if client_name == "Vainu.io":
        return Vainu(client_name, url)
    if client_name == "Dear Lucy":
        return DearLucy(client_name, url)
    if client_name == "Electronic Arts":
        return ElectronicArts(client_name, url)
    if client_name == "Sniffie":
        return Sniffie(client_name, url)
    if client_name == "Wolt":
        return Wolt(client_name, url)
    if client_name == "Santapark":
        return Santapark(client_name, url)
    if client_name == "Northern Lights Village":
        return NorthernLightsVillage(client_name, url)
    if client_name == "Kakslauttanen":
        return Kakslauttanen(client_name, url)
    if client_name == "Keysight Technologies":
        return KeysightTechnologies(client_name, url)
    if client_name == "Nipromec Group":
        return NipromecGroup(client_name, url)
    if client_name == "Sellforte":
        return Sellforte(client_name, url)
    if client_name == "Dazzle Rocks":
        return DazzleRocks(client_name, url)
    if client_name == "Codemate":
        return Codemate(client_name, url)
    if client_name == "Kamp Collection hotels":
        return KampCollection(client_name, url)
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
                                  "women who code",
                                  "harjoittelu / opinnäytetyö",
                                  "harjoittelu- ja opinnäytetyöt sekä tet-harjoittelu",
                                  "avoimia työpaikkoja kouvolassa"]
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

    @staticmethod
    def get_end_date_by_regex(pattern, description, day_first=True):
        """
        Gets end_date from description which matches with a specific pattern
        :param pattern:
        :param description:
        :param day_first:
        :return:
        """
        end_date = None
        min_end_date = None
        yesterday = datetime.today() - timedelta(days=1)

        matches = re.finditer(pattern, description)

        for match in matches:
            try:
                end_date_aux = parser.parse(match.group(), dayfirst=day_first)
                # if dates is from the past, we skip it
                if end_date_aux < yesterday:
                    continue
                if not min_end_date or end_date_aux < min_end_date:
                    min_end_date = end_date_aux
            except ValueError:
                # Since we use a regex, we don't log the errors
                pass

        if min_end_date:
            end_date = min_end_date.strftime('%Y-%m-%d')

        return end_date


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
            details_block = soup.find('div', attrs={'class': 'column_attr clearfix'})
            if details_block:
                for tag in details_block.find("h1").next_siblings:
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
        jobs_block = soup.find('div', class_='career-list')

        if jobs_block:
            for item in jobs_block.find_all("li", class_="item clearfix"):
                title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                if is_finnish and self.is_valid_job(title, description_url, description):
                    location_tag = item.find('div', class_='city')
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
        is_finnish = False
        locator = CityLocator()

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.get_text().strip()

            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split("com/")[0] + "com" + relative_url

                city_tag = item.find('div', class_='city')
                if city_tag:
                    city = city_tag.get_text()
                    if locator.has_finnish_cities(city):
                        is_finnish = True
                        description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(full_url):
        description = ""
        job_details_html = request_support.simple_get(full_url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            for description_parent in soup.find_all('div', class_='content'):
                if description_parent.has_attr('class') and len(description_parent['class']) == 1:
                    for child in description_parent.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            description += str(child)
                    break

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
                    end_date = self.get_end_date(description)
                    job = ScrapedJob(title, description, None, self.client_name, None, None, end_date, None, description_url)
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

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        return self.get_end_date_by_regex(pattern, description)


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
                    location = self.get_location(li, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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

    def get_location(self, item, job_title):
        location = None
        location_tag = item.find('span', class_='meta')
        if location_tag:
            location_text = location_tag.get_text()
            location_splited = location_text.split("-")
            if len(location_splited) == 2:
                location = location_splited[1].strip()

        if not location:
            log_support.set_invalid_location(self.client_name, job_title)

        return location

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}((st)|(nd)|(rd)|(th)),?\s+\d{4}"
        pattern2 = r"\d{1,2}((st)|(nd)|(rd)|(th))\s+(of)\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)"
        patterns = [pattern1, pattern2]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description, day_first=False)
            if end_date:
                break

        return end_date


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

                end_date = self.get_end_date(description, title)

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
                description_url = self.url.split("/jobs")[0] + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            containers = soup.find_all('div', class_='oneabb-external-careers-Typography')
            for container in containers:
                for child in container.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.name == "h2":
                            child.name = "h3"

                        if child.get_text().strip() != "":
                            child.string = child.get_text().replace("\n", " ").strip()
                            description += str(child)

        return description

    def get_end_date(self, description, title):
        pattern = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},?\s+\d{4}"

        end_date = self.get_end_date_by_regex(pattern, description)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Qvik(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        job_divs = soup.find_all("div", class_="l-simple-listing__item")

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

        url_a = item.find("a")
        if url_a:
            title = url_a.get_text().strip()

            description_url = url_a.get('href')
            if description_url:
                if "http" not in description_url:
                    description_url = self.url.split(".com/")[0] + ".com" + description_url

                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            article = soup.find("article", class_="h-wysiwyg-html")
            if article:
                for child in article.children:
                    if isinstance(child, Tag):
                        # If apply button
                        if child.find('a', class_="c-btn"):
                            break

                        Scraper.clean_attrs(child)
                        description += str(child)

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
            location_splited = location_text.split("-")
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
            for item in ul_jobs.children:
                if isinstance(item, Tag):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

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
                location = second_span.get_text().strip()

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
                end_date = self.get_end_date(description)

                job = ScrapedJob(title, description, location, self.client_name, None, pub_date, end_date, None, description_url)
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
            description_p.attrs = {}
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

    def get_end_date(self, description):
        pattern = r"\d{1,2}((st)|(nd)|(rd)|(th))(\s+of)?\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)"
        return self.get_end_date_by_regex(pattern, description)


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
                        end_date = self.get_end_date(description)

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
            soup = BeautifulSoup(job_details_html, 'html5lib')
            description_div = soup.find('span', class_='jobdescription')
            if description_div:
                for child in description_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child != "\n" and child.text.strip() != "":
                            for match in child.find_all('span'):
                                match.unwrap()
                            description += str(child)

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

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"\d{1,2}((st)|(nd)|(rd)|(th))(\s+of)?\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?),?\s+\d{4}"
        pattern2 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern3 = r"[0-9]{1,2}/[0-9]{1,2}/[0-9]{4}"
        patterns = [pattern1, pattern2, pattern3]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

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
        is_enabled = True

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.text.strip()

            description_url = title_tag.get('href')
            if description_url:
                if "https://" not in description_url:
                    description_url = self.url.split("com/")[0] + "com" + description_url

                description, is_enabled = self.get_description(description_url)

        return title, description_url, description, is_enabled

    def get_description(self, url):
        description = ""
        is_enabled = True

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')

            # If it has an apply button, job is enabled
            if soup.find('div', class_='apply'):
                # For jobs which have sequential information
                description_div = soup.find('div', {'class': 'body'})
                if description_div:
                    for child in description_div.children:
                        if child.name:
                            self.clean_attrs(child)
                            description += str(child)
            else:
                is_enabled = False

        return description, is_enabled

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
                if self.is_finnish(job):
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

    def is_finnish(self, item):
        # It will skip those jobs which are not located in Finland. Due to that, if we can not get a job location, we will not store it. It needs to raise an error in that case.
        finnish = False
        location_tag = item.find("span", {"class": "location"})

        if location_tag:
            finnish = "Finland" in location_tag.get_text()
        else:
            log_support.set_error_message(self.client_name, "Could not filter by jobs located in Finland")

        return finnish

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
        locator = CityLocator()

        if location_tag:
            full_location = location_tag.text.strip()
            cities = locator.get_finnish_cities(full_location)
            if cities:
                location = ", ".join(c.name for c in cities)
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

        helsinki_jobs = soup.find('div', {'class': 'title-mobile'}, string="Finland")
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
            jobs_txt = "[" + script.text.split("[", 1)[1].split("];")[0] + "]"
        except (ValueError, TypeError):
            jobs_txt = ""

        return jobs_txt

    def get_end_date(self, item, title):
        date_string = None
        if "ExpirationDate" in item:
            date_field = item["ExpirationDate"]
            if date_field:
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
        if table:
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
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}(\.[0-9]{4})?"
        return self.get_end_date_by_regex(pattern, description)


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

        for item in soup.find_all("a", class_=lambda value: value and "BoxGridItem__" in value):
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
        title_tag = item.find("div", class_=lambda value: value and "sc-bdVaJa sc-htpNat" in value)
        if title_tag:
            title = title_tag.get_text()

            # Check description_url
            relative_url = item.get('href')
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

            description_block = job_details_soup.find("div", class_=lambda value: value and "Content__Body-" in value)
            if description_block:
                parent = description_block.find('div')
                for child in parent.children:
                    Scraper.clean_attrs(child)
                    # Last description block called "Next steps" includes information to apply
                    if child.text.strip() == "Next steps":
                        break

                    description += str(child)

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


class SignantHealth(Scraper):

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
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        return self.get_end_date_by_regex(pattern, description)


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
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_block = soup.find('article', {'class': 'db_career'})
            if details_block:
                for tag in details_block.children:
                    if isinstance(tag, Tag):
                        if tag.find("script"):
                            continue
                        Scraper.clean_attrs(tag)
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
                finnish = self.is_finnish(item)
                if finnish:
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

    @staticmethod
    def is_finnish(item):
        finnish = True

        if "location" in item and "country" in item["location"] and "city" in item["location"]:
            finnish = "Finland" == item["location"]["country"] or "Finland" in item["location"]["city"]

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "hosted_url" in item:
                description_url = item["hosted_url"]
                if "description" in item:
                    description_raw = item["description"]
                    description_soup = BeautifulSoup(description_raw, "html.parser")
                    for tag in description_soup.children:
                        if isinstance(tag, Tag):
                            Scraper.clean_attrs(tag)
                            if tag.name == "h1":
                                continue
                            if tag.name == "h3":
                                tag.name = "h4"
                            if tag.name == "h2":
                                tag.name = "h3"
                            if tag.get_text().strip() != "":
                                description += str(tag)

        return title, description_url, description


class FSecure(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_finnish(item) and self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)
                end_date = self.get_end_date(item, title)
                if "employment_type" in item:
                    job_type = item["employment_type"]
                else:
                    job_type = None

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, description_url)
                jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = False

        if "locations" in item:
            for location in item["locations"]:
                if "location" in location and "country" in location["location"] and "Finland" in location["location"]["country"]:
                    finnish = True
                    break

        return finnish

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
                        end_date = self.get_end_date(description)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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
                children = json_dict["body"]["children"][1]["children"][0]["children"]
                for child in children:
                    if "text" in child:
                        description_raw = child["text"]
                        description_soup = BeautifulSoup(description_raw, "html.parser")
                        for tag in description_soup.children:
                            if isinstance(tag, Tag):
                                Scraper.clean_attrs(tag)
                                if tag.text != "\xa0" and tag.text.strip() != "":
                                    description += str(tag)

                        break
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

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}((st)|(nd)|(rd)|(th)),?\s+\d{4}"
        pattern3 = r"\d{1,2}((st)|(nd)|(rd)|(th))\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{4}"
        patterns = [pattern1, pattern2, pattern3]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

        return end_date


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
                    Scraper.clean_attrs(div)
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
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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
                first_p = details_block.find("p")
                if first_p:
                    Scraper.clean_attrs(first_p)
                    description += str(first_p)
                    for sibling in first_p.next_siblings:
                        Scraper.clean_attrs(sibling)
                        if sibling.find('img'):
                            continue
                        if sibling.name == "h3" and sibling.find('a'):
                            continue

                        if sibling.name:
                            description += str(sibling)

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

    def get_end_date(self, description):
        pattern = r"\d{1,2}\.\d{1,2}\.\d{4}"
        return self.get_end_date_by_regex(pattern, description)


class Enfo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_='grid__item'):
            if self.is_finnish(item):
                title, description_url, description, end_date = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True
        country_tag = item.find('div', class_='field__item')
        if country_tag:
            country = country_tag.get_text()
            finnish = "Finland" == country

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        end_date = None

        # Check title
        title_tag = item.find('h4', class_='node__title')
        if title_tag:
            title = title_tag.get_text().strip()

            # Check description_url
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description, end_date = self.get_full_description(description_url, title)

        return title, description_url, description, end_date

    def get_full_description(self, url, title):
        description = ""
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            # Two kind of HTML: one with a div id="job-description" and other
            details_block = job_details_soup.find('div', class_='group-right')
            if details_block:
                first_p = details_block.find('p')
                if first_p:
                    Scraper.clean_attrs(first_p)
                    description += str(first_p)

                    for sibling in first_p.next_siblings:
                        if isinstance(sibling, Tag):
                            Scraper.clean_attrs(sibling)
                            description += str(sibling)

            end_date = self.get_end_date(job_details_soup, title)

        return description, end_date

    def get_location(self, item, title):
        location = None
        location_div = item.find('div', class_='field_city')
        if location_div:
            location_tags = location_div.find_all('div', class_='field__item')
            for tag in location_tags:
                if location:
                    location += tag.get_text() + ", "
                else:
                    location = tag.get_text() + ", "

        if location:
            # remove comma
            location = location.strip()[0:-1]
        else:
            log_support.set_invalid_location(self.client_name, title)
            location = None

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_block = item.find('div', class_='field_last_application_date')
        if end_date_block:
            end_date_tag = end_date_block.find('div', class_='field__item')
            if end_date_tag:
                try:
                    end_date = parser.parse(end_date_tag.get_text(), dayfirst=True).strftime('%Y-%m-%d')
                except ValueError:
                    log_support.set_invalid_location(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


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
            location = ", ".join(c.name for c in cities)
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
            location = ", ".join(c.name for c in cities)
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
                title = details_block.find(['h1', 'h2'])
                if title:
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
            location = ", ".join(c.name for c in cities)
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
                    # Nitor has a unique office located in Helsinki
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
            location = ", ".join(c.name for c in cities)
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
            location = ", ".join(c.name for c in cities)
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
            location = ", ".join(c.name for c in cities)
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
                title, description_url, description, location, is_valid = self.get_mandatory_fields(item)
                if is_valid and self.is_valid_job(title, description_url, description):
                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""
        description_url = location = None

        # Remedy has a job called "Software Developer for DevOps" which points to an invalid description URL (HTTP 404). It must be skipped
        is_valid = True

        title = item.text.strip()
        if title == "Software Developer for DevOps":
            is_valid = False
        else:
            description_url = item.get('href')
            if description_url:
                description, location = self.get_full_description(description_url, title)

        return title, description_url, description, location, is_valid

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
                location = location_split[1].strip()

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
                        end_date = self.get_end_date(description)
                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
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

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        return self.get_end_date_by_regex(pattern, description)


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
            title = url_tag.text.rstrip(".")  # remove last '.' from the jobs
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
                title, description_url, description, is_enabled = self.get_mandatory_fields(row)
                if is_enabled and self.is_valid_job(title, description_url, description):
                    location = self.get_location(description_url, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        is_enabled = True

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.text
            description_url = url_tag.get('href')
            if description_url:
                description, is_enabled = self.get_full_description(description_url)

        return title, description_url, description, is_enabled

    @staticmethod
    def get_full_description(url):
        description = ""
        is_enabled = True

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            # Holvi has some jobs which are no longer valid. Those invalid jobs do not have '<section class="section section--header">'
            is_enabled = job_details_soup.find('section', class_='section section--header')
            if is_enabled:
                sections = job_details_soup.find_all('section', class_='section section--text')
                for section in sections:
                    for child in section.children:
                        Scraper.clean_attrs(child)
                        if child.name:
                            if child.name == "h2":
                                child.name = "h4"
                            description += str(child)

        return description, is_enabled

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
                title, description_url, description, is_enabled = self.get_mandatory_fields(row)
                if is_enabled and self.is_valid_job(title, description_url, description):
                    location = self.get_location(description_url, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        enabled = True

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
                # job 'DATA SCIENTIST' no longer exists but its link still appears in the website. Must be skipped in order to avoid a knonwn error
                if "vacancies/4715" in description_url:
                    enabled = False
                else:
                    description = self.get_full_description(description_url)

        return title, description_url, description, enabled

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
            location = ", ".join(c.name for c in cities)
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
                    if "https://" not in description_url:
                        description_url = self.url.split(".com/")[0] + ".com" + description_url
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
        # From API
        log_support.log_extract_info(self.client_name)
        jobs = []
        json_dict = json.loads(html)
        if "jobs" in json_dict:
            for item in json_dict["jobs"]:
                if self.is_finnish(item):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        # All its jobs are located in Helsinki, besides this has already being checked in "is_finnish()"
                        job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

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
            location = ", ".join(c.name for c in cities)
        else:
            location = None

        return location


class RedhillGames(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        block = soup.find('div', {"id": "comp-joer0a86"})
        if block:
            for item in block.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    # only one office located in Helsinki
                    location = "Helsinki"
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
            containers = job_details_soup.find_all('div', class_=['canvas-job-description', 'canvas-skills'])
            for container in containers:
                for row in container.find_all('div', class_='row'):
                    # Skips button apply link
                    if row.find('a', class_='btn'):
                        continue

                    for child in row.children:
                        if isinstance(child, Tag):
                            # Skips hidden texts
                            if child.find('span', class_='placeholder hidden') and child.find('span', class_='placeholder hidden').parent.name == "h2":
                                child.find('span', class_='placeholder hidden').parent.decompose()

                            if child.name == "h2":
                                child.name = "h3"
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
            if end_date_raw:
                try:
                    end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
                except (ValueError, TypeError) as e:
                    log_support.set_error_message(self.client_name, "Invalid date string in job " + title + " " + str(e))

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

        containers = soup.find_all('div', class_="contents")
        for container in containers:
            for item in container.find_all('div'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location, end_date = self.get_job_details(description_url, title)

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
            block = job_details_soup.find('div', class_='jobs_body')
            if block:
                for child in block.children:
                    if isinstance(child, Tag):
                        if child.name == "a" and child.has_attr('class') and "like_button" in child['class']:
                            break

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child).strip()

        return description

    def get_job_details(self, url, title):
        location = end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            job_details = job_details_soup.find('div', class_='jobs_details')
            if job_details:
                date_label = job_details.find(lambda tag: tag.name == "label" and "Last apply date:" in tag.text)
                location_label = job_details.find(lambda tag: tag.name == "label" and "Location:" in tag.text)

                if date_label:
                    date_tag = date_label.next_sibling
                    if date_tag:
                        try:
                            date_raw = date_tag.strip()
                            end_date = parser.parse(date_raw, dayfirst=True).strftime('%Y-%m-%d')
                        except (ValueError, TypeError) as e:
                            log_support.set_error_message(self.client_name, "Invalid date string " + str(e))

                if location_label:
                    location_tag = location_label.next_sibling
                    if location_tag:
                        location = location_tag.strip()

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location, end_date


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

        html = request_support.simple_post(post_url, body=body)
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


class Oura(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_="item-container"):
            title, description_url, description, location = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        location = None

        # Description page shows a better job title than the main page so we get the title from description
        url_tag = item.find('a')
        if url_tag:
            description_url = url_tag.get('href')
            if description_url:
                job_details_html = request_support.simple_get(description_url)

                if job_details_html:
                    job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

                    title_tag = job_details_soup.find('h1')
                    if title_tag:
                        title = title_tag.get_text()
                        description = self.get_description(job_details_soup)

                    # since we are in the description page, we get also the location here
                    header_section = job_details_soup.find('section', class_='section--header')
                    if header_section:
                        location_tag = header_section.find('p', class_='meta')
                        if location_tag:
                            location = location_tag.get_text()

        return title, description_url, description, location

    @staticmethod
    def get_description(job_details_soup):
        description = ""

        for section in job_details_soup.find_all('section', class_='section--text'):
            for child in section.children:
                if isinstance(child, Tag):
                    Scraper.clean_attrs(child)
                    if child.name == "h2":
                        child.name = "h3"
                    if child.text != "":
                        description += str(child)

        return description


class Matchmade(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        html_str = html.decode('utf-8')
        json_html = re.findall(r'\((.*)\)', html_str)
        if len(json_html) == 1:
            html = json_html[0]
            json_dict = json.loads(html)
            if "results" in json_dict:
                for item in json_dict["results"]:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        if "location" in item:
                            location = item["location"]
                        else:
                            location = None

                        if "typeOfEmployment" in item:
                            job_type = item["typeOfEmployment"]
                        else:
                            job_type = None

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, job_type, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "vacancyName" in item:
            title = item["vacancyName"]
            if "companyName" in item and "publicationId" in item and "urlJobName" in item:
                description_url = self.url.split(".com/")[0] + ".com/" + item["companyName"] + "/" + item["publicationId"] + "/" + item["urlJobName"]
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            for section in job_details_soup.find_all('section', class_='job-section'):
                if section.has_attr('id') and ("st-additionalInformation" in section['id'] or "st-embed-map" in section['id']):
                    break

                for child in section.children:
                    if isinstance(child, Tag):
                        if child.name == "h2":
                            child.name = "h3"
                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description


class Ultimate(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li', class_="careers-list-item"):
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
        title_tag = item.find('h1', class_="careers-heading")
        if title_tag:
            title = title_tag.get_text().strip().capitalize()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".ai/")[0] + ".ai" + relative_url
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_container = job_details_soup.find('div', class_='w-container')

            for child in job_container.children:
                if isinstance(child, Tag):
                    Scraper.clean_attrs(child)

                    if child.name == "ul":
                        description += str(child)
                    else:
                        for ch in child.children:
                            if ch.name == "h2":
                                ch.name = "h3"
                            if ch.text != "\u200d":
                                description += str(ch)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_='careers-description')
        if location_tag:
            location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Yousician(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "offices" in json_dict:
            if "departments" in json_dict["offices"][0]:
                for department in json_dict["offices"][0]["departments"]:
                    if "jobs" in department:
                        for item in department["jobs"]:
                            title, description_url, description = self.get_mandatory_fields(item)
                            if self.is_valid_job(title, description_url, description):
                                if "location" in item and "name" in item["location"]:
                                    location = item["location"]["name"]
                                else:
                                    location = None

                                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "absolute_url" in item:
                description_url = item["absolute_url"]
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            job_container = job_details_soup.find('div', {'id': 'content'})

            # skip the first h3
            first_tag = job_container.find('h3')
            if first_tag:
                for sibling in first_tag.next_siblings:
                    if isinstance(sibling, Tag):
                        if sibling.name == "h3" and sibling.text == "HOW TO APPLY":
                            break
                        if sibling.name == "h3":
                            sibling.string = sibling.text.capitalize()

                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description


class Leadfeeder(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_="row jobs__listing"):
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
        title_tag = item.find('h3', class_="jobs__title")
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a', class_='jobs__button')
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
            section = job_details_soup.find('section', class_='layout')

            if section:
                parent_div = section.find('div', class_="columns")
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        if child.find('a', class_='button--apply'):
                            break

                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('h4', class_='accordion__location')
        if location_tag:
            location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class ZenRobotics(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_ul = soup.find('ul', class_='jobs')
        if jobs_ul:
            for item in jobs_ul.find_all('li'):
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
        title_tag = item.find('span', class_="title")
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
            parent_div = job_details_soup.find('div', class_='body')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Callstats(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='btn-item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description_url, title)
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('h4')
        if title_tag:
            title = title_tag.get_text(separator=' ')
            url_tag = item.find('a')
            if url_tag:
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
            header = job_details_soup.find('h3', {'id': 'job-description'})

            # Some jobs do not have a h3 <job-description> tag but h3 with text "The role"
            if not header:
                header2 = job_details_soup.find('h3', string="The Role")
                if header2:
                    header = header2

            if header:
                for sibling in header.next_siblings:
                    if isinstance(sibling, Tag):
                        if sibling.name == "blockquote":
                            break

                        Scraper.clean_attrs(sibling)
                        description += str(sibling).strip()

        return description

    def get_location(self, url, title):
        location = None

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            location_tag = job_details_soup.find('div', class_='jobs-desc-inner')
            if location_tag:
                location_label = location_tag.find('p')
                if location_label:
                    location = location_label.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Bitbar(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='b-listing__item'):
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
        title_tag = item.find('h4')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
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

            parent_div = job_details_soup.find('article', class_='c-article')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('p', class_='c-media__label')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Aiven(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('div', class_='open-positions')
        if jobs_div:
            for item in jobs_div.find_all('div', class_='career'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    # Some jobs are remote and they define it as European Union
                    if "European Union" in location:
                        location = location + ", Remote"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
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

            parent_div = job_details_soup.find('div', class_='text-body')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_='location')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class SSHCommunicationsSecurity(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('ul', class_='at-jobs-list')
        if jobs_div:
            for item in jobs_div.find_all('li', class_='at-jobs-list-item'):
                # Skip header line
                if item.has_attr('class') and "at-joblist-header" in item['class']:
                    continue

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
        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            container = job_details_soup.find('div', class_='at-job-body')
            if container:
                for child in container.children:
                    if isinstance(child, Tag):
                        if child.find("img"):
                            continue
                        if child.name == "h2":
                            child.name = "h3"
                        elif child.name == "h3":
                            child.name = "h4"

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        # location is in the second div
        first_div = item.find('div')
        if first_div:
            location_tag = first_div.find_next_sibling('div')
            if location_tag:
                location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        # end_date is in the last div
        div_list = item.find_all('div')
        last_div = None

        for last_div in div_list:
            pass

        if last_div:
            end_date = last_div.get_text().strip()

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Vizor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='post-item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', class_='post-body')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        if child.find('a', string="Apply now"):
                            break

                        Scraper.clean_attrs(child)
                        description += str(child).strip()

        return description

    def get_location(self, url, title):
        location = None

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            location_tag = job_details_soup.find('div', class_='location')
            if location_tag:
                location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Frosmo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('a', class_='fcom--collection__list-item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # location can be hard-coded since we don't have information in the description about it
                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = None
        description = ""

        title_tag = item.find('div', class_='title')
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

            job_title = job_details_soup.find('h1', class_='fcom--article__title')
            if job_title:
                for sibling in job_title.next_siblings:
                    if isinstance(sibling, Tag):
                        if sibling.find('a', string="Apply now"):
                            break

                        Scraper.clean_attrs(sibling)
                        description += str(sibling).strip()

        return description


class Supermetrics(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        open_positions_tag = soup.find('div', {'id': 'open-positions'})
        if open_positions_tag:
            for item in open_positions_tag.next_siblings:
                # last elements from siblings - no jobs
                if item.name == "div" and item.get('id') in ["sm-trial", "sm-footer"]:
                    break

                if item.name == "div" and item.has_attr('class') and "et_pb_section" in item['class']:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(description_url, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)
        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a', class_='button')
            if url_tag:
                description_url = url_tag.get('href')

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', {'id': 'content'})
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.text != "\xa0":
                            description += str(child).strip()

        return description

    def get_location(self, url, title):
        location = None

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            location_tag = job_details_soup.find('div', class_='location')
            if location_tag:
                location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Taiste(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('a', class_='teaser'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description_url, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', class_='teaser-text')
        if title_tag:
            title_div = title_tag.find('h3')
            if title_div:
                title = title_div.get_text().strip()

                relative_url = item.get('href')
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

            first_p = job_details_soup.find('p')

            if first_p:
                Scraper.clean_attrs(first_p)
                description += str(first_p)

                for sibling in first_p.next_siblings:
                    if isinstance(sibling, Tag):
                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description

    def get_location(self, url, title):
        location = None

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            location_tag = job_details_soup.find('div', class_='teaser-text')
            if location_tag:
                location_div = location_tag.find('div')
                if location_div:
                    location = location_div.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Autori(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='open-position'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # It has a unique office in Oulu
                location = "Oulu"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.get_text().strip()
            # Autori does not have a specific job description page but everything is in the root
            description_url = self.url

            description_parent = item.find('div', class_='open-position-details')
            if description_parent:
                for child in description_parent.children:
                    Scraper.clean_attrs(child)
                    description += str(child)

        return title, description_url, description


class Degrees(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='toggleBlueBox')
        if container:
            ul = container.find('ul')
            if ul:
                for item in ul.children:
                    if isinstance(item, Tag) and item.name == 'li':
                        title, description_url, description, is_enabled = self.get_mandatory_fields(item)
                        if is_enabled and self.is_valid_job(title, description_url, description):
                            job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                            jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        is_enabled = True

        title_tag = item.find('a')
        if title_tag:
            title = title_tag.get_text().strip()
            # job called 'Business Developer (Finnish speaking)' does not have description_url. Instead of returning an error, we skip it
            if title == "Business Developer (Finnish speaking)":
                is_enabled = False
            else:
                description_block = item.find('div', class_='content')
                if description_block:
                    for child in description_block.children:
                        if isinstance(child, Tag):
                            apply = child.find('a', class_="btn")
                            if apply:
                                description_url = apply.get('href')
                                break

                            Scraper.clean_attrs(child)
                            description += str(child)

        return title, description_url, description, is_enabled


class Umbra(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='card-clickable'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()

            relative_url = url_tag.get('href')
            description_url = self.url + relative_url

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='jobdesciption')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta-job-location-city')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Lumoame(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        # Get the mandatory fields from description url
        for item in soup.find_all('a', class_='sqs-block-button-element--small sqs-block-button-element'):
            # skip email link
            if "mailto" in item.get('href'):
                continue
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # A unique office located in Helsinki
                location = "Helsinki"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        relative_url = item.get('href')
        if relative_url:
            description_url = self.url.split(".me/")[0] + ".me" + relative_url

            job_details_html = request_support.simple_get(description_url)
            if job_details_html:
                job_details_soup = BeautifulSoup(job_details_html, 'lxml')
                title_div = job_details_soup.find('div', class_='sqs-block-content')
                if title_div:
                    title = title_div.get_text()

                    description = self.get_description(job_details_soup)

        return title, description_url, description

    @staticmethod
    def get_description(job_details_soup):
        description = ""

        # There are several 'sqs-block html-block sqs-block-html' in the HTML. The first one that contains a p tag has the description
        for section in job_details_soup.find_all('div', class_='sqs-block html-block sqs-block-html'):
            first_p = section.find('p')
            if first_p:
                for sibling in first_p.next_siblings:
                    if isinstance(sibling, Tag):
                        # skip HTML comments
                        if sibling.get_text() != "":
                            Scraper.clean_attrs(sibling)
                            description += str(sibling)
                break

        return description


class Screenful(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # It has a unique office in Helsinki
                location = "Helsinki"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')

            # some jobs have relative url
            if "https" not in description_url:
                description_url = self.url.split(".com/")[0] + ".com" + description_url

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='sqs-block-content')
            if description_parent:
                first_h1 = description_parent.find('h1')
                if first_h1:
                    for sibling in first_h1.next_siblings:
                        if isinstance(sibling, Tag):
                            if sibling.find('a', {'href': 'https://screenful.com/jobs/'}):
                                break

                            Scraper.clean_attrs(sibling)
                            description += str(sibling)

        return description


class Sujuwa(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        ul = soup.find('ul', class_='jobs')
        if ul:
            for item in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()

        url_tag = item.find('a')
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

            description_parent = job_details_soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        if child.has_attr('class') and "apply" in child['class']:
                            break

                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Vaana(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='elementor-text-editor elementor-clearfix')
        if container:
            for item in container.find_all('p'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    # it has a unique office located in Helsinki
                    location = "Helsinki"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='elementor-text-editor elementor-clearfix')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description


class Iwa(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', {'id': 'x-section-3'})
        if container:
            job_blocks = container.find_all('div', class_='x-container max width')
            if len(job_blocks) > 1:
                for job_section in job_blocks[1].find_all('h5', class_='h-custom-headline'):
                    # It has jobs in Finland, Vietnam and Thailand. This info appears in a header so we need to get first that header and then move to the next sibling
                    if "FINLAND" in job_section.get_text():
                        sibling = job_section.find_next_sibling('div')
                        if sibling:
                            for item in sibling.find_all('a'):
                                title, description_url, description = self.get_mandatory_fields(item)
                                if self.is_valid_job(title, description_url, description):
                                    # it has a unique office located in Helsinki
                                    location = "Helsinki"

                                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""

        title = item.get_text().strip()
        description_url = item.get('href')

        # some jobs have relative url
        if "http" not in description_url:
            description_url = self.url.split(".fi/")[0] + ".fi" + description_url

        if description_url:
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='x-text cs-ta-left mtn mbl')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description


class Nico(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='feedzy-rss')
        if container:
            for item in container.find_all('li', class_='rss_item'):
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

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip().capitalize()
            url_tag = title_tag.find('a')
            if url_tag:
                description_url = url_tag.get('href')

                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='job_description')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        # some jobs have a video at the end. If so, breaks
                        if child.find('iframe'):
                            break

                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_='rss_content')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, url, title):
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            dates_block = job_details_soup.find('div', class_='job_start_end_times')
            if dates_block:
                dates_list = dates_block.find_all('span', class_='se_date')
                if len(dates_list) == 2:
                    end_date_raw = dates_list[1].get_text()
                    try:
                        end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
                    except (ValueError, TypeError) as e:
                        log_support.set_error_message(self.client_name, "Invalid date string " + str(e))

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Bitwise(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='open-position'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')

                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='entry-content')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('p', class_='tagline')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Solteq(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')
        ul = soup.find('ul', class_='jobs')
        if ul:
            for item in ul.children:
                if isinstance(item, Tag):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, description)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
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
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    @staticmethod
    def get_location(item, description):
        """
        It tries to get a Finnish city from the item, if it fails it tries  from job description
        :param item: item
        :param description: job description
        :return: Finnish cities as a String
        """
        cities = None
        locator = CityLocator()

        location_tag = item.find('span', 'meta')
        if location_tag:
            location_raw = location_tag.get_text()

            if locator.has_finnish_cities(location_raw):
                cities = locator.get_finnish_cities(location_raw)

        if cities:
            location = ", ".join(c.name for c in cities)
        else:
            cities = locator.get_finnish_cities(description)
            if cities:
                location = ", ".join(c.name for c in cities)
            else:
                location = None

        return location


class Alphasense(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')
        scripts = soup.find_all('script')
        for script in scripts:
            if script.get_text().startswith("var _state"):
                value = script.get_text().split(" = ")
                if len(value) > 1:
                    json_str = value[1]
                    json_dict = json.loads(json_str)

                    if "jobs" in json_dict:
                        for item in json_dict["jobs"]:
                            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                            if is_finnish and self.is_valid_job(title, description_url, description):
                                # Location has already being checked in get_mandatory_fields
                                location = "Helsinki"

                                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        is_finnish = False

        if "title" in item:
            title = item["title"]
            if "url" in item:
                description_url = item["url"]
                if "office" in item and "title" in item["office"] and "Helsinki" in item["office"]["title"]:
                    is_finnish = True
                    description = self.get_description(description_url)

        return title, description_url, description, is_finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', {'id': 'content'})
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description


class UniversityTurku(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', class_='leipis')
        if table:
            for item in table.find_all("tr"):
                # if it is the header, skip
                if item.find('th'):
                    continue

                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Turku"
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
                description_url = self.url.split("certiahome/")[0] + "certiahome/" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_div = soup.find('table', class_='leipis')
            # it has two <tr>, first one is the title, second one is the description
            tr_list = description_div.find_all('tr')
            if tr_list and len(tr_list) > 1:
                td = tr_list[1].find('td')
                if td:
                    for child in td.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            description += str(child)

        return description

    def get_end_date(self, item, title):
        end_date = None

        # end_date is in the last td
        td_list = item.find_all('td')
        last_td = None

        for last_td in td_list:
            pass

        end_date_raw = last_td.get_text().strip()
        try:
            end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
        except (ValueError, TypeError):
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UniversityHelsinki(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        # Define a max number of iterations
        max_pg = 10
        pg = 1
        last_page = False
        while not last_page and pg < max_pg:
            container = soup.find('div', class_='panel')
            if container:
                for item in container.find_all('article', class_='box-story'):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = "Helsinki"
                        end_date = self.get_end_date(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)

            else:
                break

            if container.find('li', class_='pager__next'):
                new_url = self.url + "?page=" + str(pg)
                html = request_support.simple_get(new_url)
                if html:
                    soup = BeautifulSoup(html, 'lxml')
                pg += 1
            else:
                last_page = True

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3', class_='box-story__title')
        if title_tag:
            title = title_tag.get_text().strip().title()
            url_tag = title_tag.find('a')
            if url_tag:
                description_url = url_tag.get('href')

                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            description_parent = job_details_soup.find('div', class_='textarea')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_end_date(self, item, title):
        end_date = None

        end_date_div = item.find('div', class_='box-story__meta')
        if end_date_div:
            end_date_span = end_date_div.find('span')
            if end_date_span:
                end_date_raw = end_date_span.get_text()
                try:
                    end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
                except (ValueError, TypeError):
                    log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UniversityJyvaskyla(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        ul = soup.find("ul", class_='item-listing')
        if ul:
            for item in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Jyväskylä"
                    end_date = self.get_end_date(description_url)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
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
            description_parent = soup.find('div', class_='normal')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    @staticmethod
    def get_end_date(url):
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')

            # Latest <p> contains the end_date
            last_p = None
            all_p = soup.find_all('p')
            for p in all_p:
                if p.get_text() != "\xa0":
                    last_p = p

            if last_p:
                segments = last_p.get_text().split('\xa0')
                for segment in segments:
                    try:
                        end_date = parser.parse(segment).strftime('%Y-%m-%d')
                        break
                    except (ValueError, TypeError):
                        pass

        return end_date


class UniversityAalto(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        # Define a max number of iterations
        max_pg = 10
        pg = 1
        last_page = False
        while not last_page and pg < max_pg:
            container = soup.find('div', class_='aalto-rows')
            if container:
                for item in container.find_all('div', class_='aalto-listing__section'):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = "Espoo"
                        pub_date = self.get_pub_date(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, pub_date, None, None, description_url)
                        jobs.append(job)

            else:
                break

            if container.find('li', class_='aalto-pager__item--last'):
                new_url = self.url + "?page=" + str(pg)
                html = request_support.simple_get(new_url)
                if html:
                    soup = BeautifulSoup(html, 'lxml')
                pg += 1
            else:
                last_page = True

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h2', class_='aalto-listing__item-title')
        if title_tag:
            title = title_tag.get_text().strip().title()
            url_tag = title_tag.find('a')
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

            description_parent = job_details_soup.find('div', class_='aalto-user-generated-content')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_pub_date(self, item, title):
        end_date = None

        end_date_div = item.find('time')
        if end_date_div:
            end_date_raw = end_date_div.get_text()
            try:
                end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UniversityTampere(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', class_='results')
        if table:
            for item in table.find_all("tr"):
                # if it is the header, skip
                if item.find('th'):
                    continue

                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Tampere"
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
                description_url = self.url.split(".com/")[0] + ".com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='job_description')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_end_date(self, item, title):
        end_date = None

        td = item.find('td', class_='col_ApplyEndDate')
        end_date_raw = td.get_text().strip()
        try:
            end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
        except (ValueError, TypeError):
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UniversityOulu(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('div', class_='texts'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Oulu"
                end_date = self.get_end_date(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
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
            description_parent = soup.find('td', class_='normal')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_end_date(self, item, title):
        end_date = None

        spans = item.find_all('span', class_='visible-inline-block')
        for span in spans:
            end_date_tag = span.find('div', class_='field-content')
            if end_date_tag:
                end_date_raw = end_date_tag.get_text().strip()
                try:
                    end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
                except (ValueError, TypeError):
                    log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Teleste(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('div', class_='field-item even')
        if container:
            for item in container.find_all('a'):
                title, description_url, description, email_link = self.get_mandatory_fields(item)
                if not email_link and self.is_valid_job(title, description_url, description):
                    location = "Turku"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = None
        description = ""
        email_link = False

        description_url = item.get('href')
        if "mailto:" in description_url:
            email_link = True
        else:
            title = item.get_text().strip()
            if title.startswith("-"):
                # removes "-" at the beginning
                title = title.split("-", 1)[1].strip()

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description, email_link

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='field-item even')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description


class Visma(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'xml')

        return_val = soup.find("return_val")
        if return_val:
            for item in return_val.find_all('vacancy'):
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

        title_tag = item.find("vacancy_name")
        if title_tag:
            title = title_tag.get_text().title()

            description_tag = item.find('job_url')
            if description_tag:
                description_url = description_tag.get_text()
                description = self.get_description(item)

        return title, description_url, description

    @staticmethod
    def get_description(item):
        description = ""

        vacancy_text = item.find('vacancy_text')
        if vacancy_text:
            description_soup = BeautifulSoup(vacancy_text.get_text(), 'html.parser')
            for child in description_soup.children:
                if isinstance(child, Tag):
                    if child.name == "img" or child.find('img'):
                        continue
                    if child.text == "":
                        continue

                    Scraper.clean_attrs(child)
                    description += str(child)
                else:
                    p_tag = description_soup.new_tag('p')
                    p_tag.string = child
                    description += str(p_tag)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('vacancy_area')
        if location_tag:
            location_raw = location_tag.find('vacancy_area_name')
            if location_raw:
                location = location_raw.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('vsble_dt')
        if end_date_tag:
            end_date_raw = end_date_tag.get_text().strip()
            try:
                end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Forenom(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        containers = soup.find_all('div', class_='siteorigin-widget-tinymce textwidget')
        for container in containers:
            if container.find('a'):
                for item in container.find_all('a'):
                    title, description_url, description, end_date, is_valid = self.get_mandatory_fields(item)
                    if is_valid and self.is_valid_job(title, description_url, description):
                        location = self.get_location(item)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)
                break

        return jobs

    def get_mandatory_fields(self, item):
        description = ""
        end_date = None
        valid = True
        locator = CityLocator()

        title = item.get_text().strip()

        # If title contains a Finnish city (Helsinki), we remove it
        title_split = title.split("(")
        if len(title_split) > 1 and locator.has_finnish_cities(title_split[1]):
            title = title_split[0].strip()

        description_url = item.get('href')
        if description_url:
            match = re.search(r"/(\d)+\?", description_url)
            if match:
                job_id = match.group(0)
                job_id = job_id[1:-1]
                json_url = "https://paikat.te-palvelut.fi/tpt-api/tyopaikat/" + job_id + "?kieli=fi"
                description, end_date = self.get_description(json_url, title)
            else:
                valid = False

        return title, description_url, description, end_date, valid

    def get_description(self, url, title):
        description = ""
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            json_dict = json.loads(job_details_html)

            if "response" in json_dict and "docs" in json_dict["response"] and len(json_dict["response"]["docs"]) == 1:
                if "kuvaustekstiHTML" in json_dict["response"]["docs"][0]:
                    description_raw = json_dict["response"]["docs"][0]["kuvaustekstiHTML"]
                    job_details_soup = BeautifulSoup(description_raw, 'html.parser')
                    for child in job_details_soup.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            if child.get_text().strip() != "":
                                description += str(child)
                        else:
                            new_tag = job_details_soup.new_tag('p')
                            new_tag.string = child
                            description += str(new_tag)

                if "viimeinenHakupaivamaara" in json_dict["response"]["docs"][0]:
                    end_date_raw = json_dict["response"]["docs"][0]["viimeinenHakupaivamaara"]
                    try:
                        end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
                    except (ValueError, TypeError):
                        log_support.set_invalid_location(self.client_name, title)

        return description, end_date

    def get_location(self, item):
        location = None
        locator = CityLocator()

        title = item.get_text().strip()

        locations = locator.get_finnish_cities(title)
        if locations:
            location = ", ".join(locations)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_job_info(self, url, title):
        # This method is no longer called by any function. It could be removed if all jobs are pointing to paikat.te-palvelut.fi
        location = end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')

            end_date_tag = job_details_soup.find('p', class_='application-ends')
            if end_date_tag:
                pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
                end_date = self.get_end_date_by_regex(pattern, end_date_tag.get_text())

            location_tag = job_details_soup.find('span', class_='city')
            if location_tag:
                location = location_tag.get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return location, end_date


class Bitville(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('div', class_='container ad-list')
        if container:
            for item in container.find_all("a"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    # A unique office in Espoo
                    location = "Espoo"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description_url = None
        description = ""

        title_raw = item.get_text().strip()
        title = title_raw.replace("\n", " ").replace("  ", "")
        relative_url = item.get('href')
        if relative_url:
            description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_block = job_details_soup.find('section', class_='job-ad')
            if description_block:
                for child in description_block.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.name != "h3":
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


class VarianMedicalSystems(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []

        post_url = "https://sjobs.brassring.com/TgNewUI/Search/Ajax/PowerSearchJobs"

        body = {"partnerId": "25044", "siteId": "5224", "keyword": "", "location": "", "keywordCustomSolrFields": "JobTitle,FORMTEXT1,FORMTEXT3,FORMTEXT2,FORMTEXT4", "turnOffHttps": False,
                "Latitude": 0, "Longitude": 0, "facetfilterfields": {"Facet": []},
                "powersearchoptions": {"PowerSearchOption": [{"VerityZone": "FORMTEXT1", "Type": "single-select", "OptionCodes": []},
                                                             {"VerityZone": "FORMTEXT9", "Type": "single-select", "OptionCodes": ["FI"]},
                                                             {"VerityZone": "FORMTEXT4", "Type": "single-select", "OptionCodes": []},
                                                             {"VerityZone": "FORMTEXT2", "Type": "single-select", "OptionCodes": []},
                                                             {"VerityZone": "LastUpdated", "Type": "date", "Value": None}]},
                "encryptedsessionvalue": "^DhsnDFWj5cD_slp_rhc_RDUy6mN1QQbQMHgB_slp_rhc_kY_slp_rhc_yIC0W/b_slp_rhc_9O5lqe4nV9X1RiO/R_slp_rhc_QbQeSgW0AvJXgsm9XFEifaEoadsQq/zJzdOGGCE7OrofGWFlA="}

        html = request_support.simple_post(post_url, body=body)
        if html:
            json_dict = json.loads(html)
            if "Jobs" in json_dict and "Job" in json_dict["Jobs"]:
                for item in json_dict["Jobs"]["Job"]:
                    title, description_url, description, location = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = location = None
        description = ""

        if "Questions" in item:
            for question in item["Questions"]:
                if question["QuestionName"] == "jobtitle":
                    title = question["Value"]

                # we get the location here so we save a HTML call then
                if question["QuestionName"] == "formtext3":
                    location = question["Value"]

        if "Link" in item:
            description_url = item["Link"]
            description = self.get_description(description_url)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return title, description_url, description, location

    @staticmethod
    def get_description(url):
        description = ""
        desc1 = desc2 = None
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            description_soup = BeautifulSoup(job_details_html, 'html.parser')
            script = description_soup.find('input', {'id': 'preLoadJSON'})
            if script:
                if script.has_attr("value"):
                    json_dict = json.loads(script["value"])
                    if "Jobdetails" in json_dict and "JobDetailQuestions" in json_dict["Jobdetails"]:
                        for question in json_dict["Jobdetails"]["JobDetailQuestions"]:
                            if "QuestionName" in question and "AnswerValue" in question:
                                if question["QuestionName"] == "Job Description":
                                    desc1 = question["AnswerValue"]
                                if question["QuestionName"] == "Job Requirements":
                                    desc2 = question["AnswerValue"]

                    if desc1 and desc2:
                        full_description = desc1 + desc2
                        description_soup = BeautifulSoup(full_description, "html.parser")
                        for child in description_soup.children:
                            if child.name == "style":
                                continue
                            Scraper.clean_attrs(child)
                            description += str(child)

        return description


class Valmet(Scraper):
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
                        end_date = self.get_end_date(description)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)

                current_page, current_offset = self.get_next_page(current_page, Valmet.page_offset)
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
        description = description_raw = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                for child in json_dict["body"]["children"][1]["children"][0]["children"]:
                    if "text" in child:
                        description_raw = child["text"]
            except (ValueError, KeyError, IndexError, AttributeError):
                # Error message will be handled by "is_valid_job()" method
                pass

        if description_raw != "":
            description_soup = BeautifulSoup(description_raw, "html.parser")
            Scraper.clean_attrs(description_soup)
            for child in description_soup.children:
                if isinstance(child, Tag):
                    if child.name == "h1":
                        child.name = "h3"
                    elif child.name == "h2":
                        child.name = "h4"
                    elif child.name == "h3":
                        child.name = "h5"
                    description += str(child)

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

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}((st)|(nd)|(rd)|(th))?,?(\s+\d{4})?"
        pattern3 = r"\d{1,2}((st)|(nd)|(rd)|(th))\s+(of\s+)?(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{4}"
        patterns = [pattern1, pattern2, pattern3]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

        return end_date


class Metso(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('div', class_='career-search')
        if container and container.has_attr('ng-init'):
            text_raw = container["ng-init"]
            try:
                text_formatted = text_raw.split("(", 1)[1]
                json_text = text_formatted.split("name")[0].rsplit(',', 1)[0]
                json_dict = json.loads(json_text)

                for item in json_dict:
                    title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                    if is_finnish and self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)
                        end_date = self.get_end_date(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)

            except IndexError as e:
                log_support.set_error_message(self.client_name, "Error genereting jobs json " + str(e))

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        locator = CityLocator()
        finnish = False

        if "Title" in item:
            title = item["Title"]
            if "Url" in item:
                description_url = item["Url"]

                # check if it is finnish to avoid not-needed calls
                if "Locations" in item and len(item["Locations"]) > 0:
                    location = ", ".join(item["Locations"])
                    finnish = locator.has_finnish_cities(location)

                if finnish:
                    description = self.get_description(description_url)

        return title, description_url, description, finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html5lib')
            description_block = job_details_soup.find('div', class_='joqReqDescription')
            if description_block:
                for child in description_block.children:
                    if isinstance(child, Tag):
                        if child.find('img') or child.text == "\xa0" or child.text.strip() == ".":
                            continue
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        if "Locations" in item and len(item["Locations"]) > 0:
            location = ", ".join(item["Locations"])

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "PostingEndDate" in item:
            end_date_raw = item["PostingEndDate"]
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                # Exception error is logged later on
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class NokianTyres(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        scripts = soup.find_all('script')
        for script in scripts:
            if "window.vacancies" in script.get_text():
                jobs_text = self.get_jobs_text(script)
                if jobs_text != "":
                    try:
                        jobs_json = json.loads(jobs_text)

                        for item in jobs_json:
                            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                            if is_finnish and self.is_valid_job(title, description_url, description):
                                end_date = self.get_end_date(item, title)
                                # Only one office located in Nokia
                                location = "Nokia"
                                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                                jobs.append(job)

                    except json.JSONDecodeError:
                        log_support.set_invalid_json(self.client_name)
                break

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        finnish = False

        if "title" in item:
            title = item["title"]
            if "link" in item:
                description_url = item["link"]
                # check 'description_url' is valid only for jobs located in Finland
                if "country_english_name" in item and item["country_english_name"] == "Finland":
                    finnish = True
                    description_info = request_support.simple_get(description_url)
                    if description_info and "description" in item:
                        description_raw = item["description"]
                        description_soup = BeautifulSoup(description_raw, 'html.parser')
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                description += str(child)

        return title, description_url, description, finnish

    @staticmethod
    def get_jobs_text(script):
        try:
            jobs_txt = "[" + script.text.split("[", 1)[1].split("]")[0] + "]"
        except (ValueError, TypeError):
            jobs_txt = ""

        return jobs_txt

    def get_end_date(self, item, title):
        end_date = None

        if "enddate" in item:
            end_date_raw = item["enddate"]
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class MeyerTurku(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('a', class_='job-row'):
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
        title_tag = item.find('span', class_="title")
        if title_tag:
            title = title_tag.get_text()

            # Check description_url
            description_url = item.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = job_details_soup.find('div', class_="main-desc")
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location_tag = item.find('span', class_='location')
        if location_tag:
            location = location_tag.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('span', class_='date')
        if end_date_tag:
            end_date_raw = end_date_tag.get_text()
            try:
                end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
            except ValueError:
                log_support.set_invalid_dates(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Elomatic(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_header = soup.find('h3', string="Avoimet työpaikat")
        if jobs_header:
            jobs_parent = jobs_header.parent

            for item in jobs_parent.find_all('a'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description_url, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""

        # Check title
        title_tag = item.get_text()
        title = title_tag.split("/")[0].strip()

        # Check description_url
        description_url = item.get('href')
        if description_url:
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            for tag in job_details_soup.find_all('p', class_='MsoNormal'):
                Scraper.clean_attrs(tag)
                description += str(tag)

        return description

    def get_location(self, item, title):
        location_tag = item.find('span')
        if location_tag:
            location = location_tag.text
        else:
            location = None
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, url, title):
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            end_date_tag = job_details_soup.find(lambda tag: tag.name == "p" and "Viimeinen hakupäivä" in tag.text)
            if end_date_tag:
                end_date_raw = end_date_tag.get_text()
                end_date_split = end_date_raw.split(":")
                if len(end_date_split) == 2:
                    end_date_str = end_date_split[1]
                    try:
                        end_date = parser.parse(end_date_str, dayfirst=True).strftime('%Y-%m-%d')
                    except ValueError:
                        pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Almaco(Scraper):

    soup = None

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        Almaco.soup = BeautifulSoup(html, 'lxml')

        ul = Almaco.soup.find('ul', {'id': 'tab-nav'})
        if ul:
            for item in ul.find_all('a'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description_url = None
        description = ""

        # Check title
        title_raw = item.get_text().strip()
        title = title_raw.rsplit("|", 1)[0]

        if item.has_attr('data-target'):
            item_id = item["data-target"]
            if item_id:
                description_parent = Almaco.soup.find('div', {'id': item_id})
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        if child.name == "h2" or child.name == "img" or child.find("img"):
                            continue
                        if child.name == "div" and child.has_attr('class') and child["class"] == "contact-details":
                            break

                        Scraper.clean_attrs(child)
                        if child.text != "":
                            description += str(child)

                        # it does not have a specific page for the job descriptions.
                description_url = self.url

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = job_details_soup.find('div', class_="main-desc")
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    @staticmethod
    def get_location(item):

        full_title = item.get_text().strip()
        title_split = full_title.rsplit("|", 1)
        location = title_split[-1]

        return location


class Vapo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('tr'):
            if item.find('th'):
                continue

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

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text()
            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split('smarthome/')[0] + "smarthome/" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')
            first_p = job_details_soup.find('p')
            if first_p:
                for sibling in first_p.next_siblings:
                    if isinstance(sibling, Tag):
                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        first_td = item.find('td')
        if first_td:
            location_tag = first_td.find_next_sibling('td')
            if location_tag:
                location = location_tag.get_text()
            else:
                location = None
                log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        all_td = item.find_all('td')
        end_date_tag = all_td[-1]

        if end_date_tag:
            end_date_raw = end_date_tag.get_text()
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except ValueError:
                log_support.set_invalid_dates(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class AlmaMedia(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        scripts = soup.find_all('script')
        for script in scripts:
            if "dataSource" in script.get_text():
                jobs_text = self.get_jobs_text(script)
                if jobs_text != "":
                    try:
                        jobs_json = json.loads(jobs_text)

                        for item in jobs_json:
                            title, description_url, description = self.get_mandatory_fields(item)
                            if self.is_valid_job(title, description_url, description):
                                location = self.get_location(item, title)
                                end_date = self.get_end_date(item, title)

                                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                                jobs.append(job)

                    except json.JSONDecodeError:
                        log_support.set_invalid_json(self.client_name)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "Title" in item:
            title = item["Title"]
            if "ItemUrl" in item:
                description_url = self.url + "/vacancy/" + item["ItemUrl"]

                # Checks if decription url works
                description_info = request_support.simple_get(description_url)

                if description_info and "Description" in item:
                    description_raw = item["Description"]
                    description_soup = BeautifulSoup(description_raw, 'html.parser')
                    for child in description_soup.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            description += str(child)

        return title, description_url, description

    @staticmethod
    def get_jobs_text(script):
        try:
            jobs_txt = "[" + script.text.split("[", 1)[1].split("]")[0] + "]"
        except (ValueError, TypeError):
            jobs_txt = ""

        return jobs_txt

    def get_location(self, item, title):
        location = None

        if "Location" in item:
            location = item["Location"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "ApplicationDeadline" in item:
            end_date_raw = item["ApplicationDeadline"]
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Poyry(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('tr'):
            title, description_url, description, end_date = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = end_date = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title_raw = url_tag.get_text()
            title = title_raw.rsplit("-", 1)[0].strip()

            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split('.fi/')[0] + ".fi" + relative_url
                description, end_date = self.get_description(description_url, title)

        return title, description_url, description, end_date

    def get_description(self, url, title):
        description = ""
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')
            article = job_details_soup.find('article', class_='article-main__content')
            if article:
                for child in article.children:
                    if isinstance(child, Tag):
                        if child.has_attr("class") and "complementary-header" in child["class"]:
                            continue
                        if child.has_attr("class") and "sub-section share-buttons" in child["class"]:
                            continue
                        if child.name == "h1":
                            continue

                        if child.name == "div" and child.has_attr("class") and "apply" in child["class"]:
                            # Gets here the end_date to save a next request
                            end_date = self.get_end_date(child, title)

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description, end_date

    @staticmethod
    def get_location(item):
        location = None

        url_tag = item.find('a')
        if url_tag:
            title_raw = url_tag.get_text()
            title_split = title_raw.rsplit("-", 1)
            location = title_split[-1].strip()

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_raw = item.get_text()
        try:
            end_date_split = end_date_raw.split(":")[-1]
            end_date = parser.parse(end_date_split, dayfirst=True).strftime('%Y-%m-%d')
        except ValueError:
            log_support.set_invalid_dates(self.client_name, title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UPM(Scraper):

    def extract_info(self, html):
        # From API
        locator = CityLocator()
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "vacancies" in json_dict:
            for item in json_dict["vacancies"]:
                if "location" not in item:
                    log_support.set_error_message(self.client_name, "ERROR getting locations from JSON. Skipping job")
                    continue

                if locator.has_finnish_cities(item["location"]):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = item["location"]

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

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, job_type, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "link" in item:
                description_url = item["link"]
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(description_url):
        description = ""
        job_details_html = request_support.simple_get(description_url, accept_json=True)
        if job_details_html:
            json_dict = json.loads(job_details_html)
            try:
                children = json_dict["body"]["children"][1]["children"][0]["children"]
                for child in children:
                    if "text" in child:
                        description_raw = child["text"]
                        description_soup = BeautifulSoup(description_raw, "html.parser")
                        for tag in description_soup.children:
                            Scraper.clean_attrs(tag)
                            if tag.text != "\xa0":
                                description += str(tag)

                        break
            except (ValueError, KeyError, IndexError, AttributeError):
                description = ""

        return description


class Mirum(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            if "fields" in item and "country" in item["fields"] and item["fields"]["country"] == "Finland":
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        base_url = "https://prod-api.mirum.agency/rest/page/job_posting/"

        if "title" in item["fields"]:
            title = item["fields"]["title"]
            if "alias" in item["fields"]:
                description_url = base_url + item["fields"]["alias"]
                description, description_url = self.get_description(description_url)

        return title, description_url, description

    def get_description(self, description_url):
        """
        description_url contains the JSON response, we need to overwrite that URL with the job description in HTML
        :param description_url:
        :return:
        """
        description_url_txt = None
        description = ""
        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            json_dict = json.loads(job_details_html)

            if len(json_dict) == 1:
                if "fields" in json_dict[0] and "cta" in json_dict[0]["fields"] and "url" in json_dict[0]["fields"]["cta"]:
                    description_url_txt = json_dict[0]["fields"]["cta"]["url"]

                if description_url_txt and "fields" in json_dict[0] and "description" in json_dict[0]["fields"]:
                    description_raw = json_dict[0]["fields"]["description"]
                    description_soup = BeautifulSoup(description_raw, "html.parser")
                    for tag in description_soup.children:
                        if isinstance(tag, Tag):
                            Scraper.clean_attrs(tag)
                            if tag.text != "\xa0":
                                description += str(tag)
            else:
                log_support.set_error_message(self.client_name, "ERROR. JSON from job description URL did not return a unique job.")

        return description, description_url_txt

    def get_location(self, item, title):
        location = None

        if "fields" in item and "city" in item["fields"]:
            location = item["fields"]["city"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Krogerus(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='jobylon-job-list')
        if container:
            for item in container.find_all('div', class_='jobylon-job'):
                title, description_url, description, location = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    end_date = self.get_end_date(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = location = None
        description = ""

        title_tag = item.find('div', class_='jobylon-job-title')
        # remove "- Open Application
        if title_tag:
            title_raw = title_tag.get_text()
            title = re.split("Open Application", title_raw, flags=re.IGNORECASE)[0].strip()
            if title.endswith("-") or title.endswith("–"):
                title = title[0:-1].strip()

            url_tag = item.find('a', class_='jobylon-apply-btn')
            if url_tag:
                description_url = url_tag.get('href')
                if description_url:
                    description, location = self.get_description(description_url)

        return title, description_url, description, location

    @staticmethod
    def get_description(url):
        description = ""
        location = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parents = soup.find_all('div', class_=['canvas-job-description', 'canvas-skills'])
            for parent in description_parents:
                for row in parent.find_all('div', class_='row'):
                    for child in row.children:
                        if isinstance(child, Tag):
                            if child.find('a', class_='btn'):
                                continue

                            Scraper.clean_attrs(child)
                            description += str(child)

            # Gets location here to save a request later
            location_tag = soup.find('li', {'data-toggle': 'tooltip'})
            if location_tag:
                location = location_tag.get_text().strip()

        return description, location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('li', class_='jobylon-application-date')
        if end_date_tag:
            try:
                end_date_split = end_date_tag.get_text().split(":")[-1]
                end_date = parser.parse(end_date_split).strftime('%Y-%m-%d')
            except ValueError:
                log_support.set_invalid_dates(self.client_name, title)

        # Many jobs do not have any date, we don't raise an error for that

        return end_date


class Siemens(Scraper):

    def extract_info(self, html):
        # From API
        log_support.log_extract_info(self.client_name)
        jobs = []
        json_dict = json.loads(html)
        if "jobs" in json_dict:
            for item in json_dict["jobs"]:
                if self.is_finnish(item):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = False
        if "data" in item:
            if "country" in item["data"] and "Finland" == item["data"]["country"]:
                finnish = True
            else:
                if "additional_locations" in item["data"]:
                    for office in item["data"]["additional_locations"]:
                        if "country" in office:
                            if office["country"] == "Finland":
                                finnish = True
                                break

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "data" in item:
            if "title" in item["data"]:
                title = item["data"]["title"]

            if "meta_data" in item["data"] and "canonical_url" in item["data"]["meta_data"]:
                description_url = item["data"]["meta_data"]["canonical_url"]
                if "description" in item["data"]:
                    description_raw = item["data"]["description"]
                    soup = BeautifulSoup(description_raw, 'html.parser')
                    for child in soup.children:
                        Scraper.clean_attrs(child)
                        description += str(child)

        return title, description_url, description

    def get_location(self, item, title):
        location = None
        locations = []
        if "data" in item:
            if "city" in item["data"]:
                locations.append(item["data"]["city"])

            if "additional_locations" in item["data"]:
                for office in item["data"]["additional_locations"]:
                    if "country" in office:
                        if office["country"] == "Finland":
                            locations.append(office["country"])

        if locations:
            location = ", ".join(locations)

        if not locations:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Posti(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        current_pos = 0
        offset = 25
        last_page = False
        i = 0
        max_iteration = 5
        while not last_page and i < max_iteration:
            i += 1

            all_jobs = soup.find_all('li', class_='job-result-card')
            if not all_jobs:
                break

            for item in all_jobs:
                title, description_url, description = self.get_mandatory_fields(item)
                title = self.update_title(title)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

            if not last_page or soup.find('button', class_='see-more-jobs'):
                current_pos += offset
                next_url = self.url.rsplit("=", 1)[0] + "=" + str(current_pos)
                html = request_support.simple_get(next_url)
                if html:
                    soup = BeautifulSoup(html, 'lxml')
                    continue

            # reaching this point would mean some kind of error
            last_page = True

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3', class_='result-card__title')

        if title_tag:
            title = title_tag.get_text()
            url_tag = item.find('a', class_='result-card__full-card-link')

            if url_tag:
                description_url = url_tag.get('href')
                if description_url:
                    description, description_url = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description_url = None
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            # description_url must be updated
            url_tag = job_details_soup.find('a', class_='apply-button--link')
            if url_tag:
                description_url = url_tag.get('href')

                if description_url:
                    parent = job_details_soup.find('div', class_='description__text')
                    if parent:
                        for child in parent.children:
                            Scraper.clean_attrs(child)
                            if child.name and child.text.strip() == "":
                                continue
                            # remove "_________________....._" from description
                            if child.name and child.text.strip().count("_") == len(child.text.strip()):
                                continue

                            description += str(child)

        return description, description_url

    @staticmethod
    def update_title(original_title):
        locator = CityLocator()

        title = original_title.split(", Posti")[0]
        title = title.split(" - ")[0]
        title_comma = title.split(', ')
        if len(title_comma) > 1:
            is_city = False
            for idx, segment in enumerate(title_comma):
                words = segment.split()
                for word in words:
                    if locator.has_finnish_cities(word):
                        is_city = True
                        break
                if is_city:
                    title = " ".join(title_comma[0:idx])
                    break

        return title

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='job-result-card__location')
        if location_tag:
            location = location_tag.get_text()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"\d{1,2}(\s+of)?\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)(\s[0-9]{4})?"
        patterns = [pattern1, pattern2]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description, day_first=True)
            if end_date:
                break

        return end_date


class Attendo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        current_pg = 1

        last_page = False
        while not last_page:
            tbody = soup.find('tbody')
            if not tbody:
                break

            for job in tbody.find_all('tr'):
                title, description_url, description = self.get_mandatory_fields(job)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(job, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

            if self.is_last_page(soup):
                last_page = True
            else:
                current_pg += 1
                next_page_url = self.url.rsplit("#", 1)[0] + "#" + str(current_pg)
                job_details_html = request_support.simple_get(next_page_url)

                if job_details_html:
                    soup = BeautifulSoup(job_details_html, 'html.parser')
                else:
                    # in case of error, break
                    last_page = True

        return jobs

    @staticmethod
    def is_last_page(soup):
        last_page = True

        ul_pagination = soup.find('ul', class_='pager')
        if ul_pagination:
            if ul_pagination.find('li', class_='pager-next'):
                last_page = False

        return last_page

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        title_tag = item.find('p', class_='title')
        if title_tag:
            title = title_tag.get_text()

            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            first_p = soup.find('p', class_='title-meta')
            if first_p:
                for sibling in first_p.next_siblings:
                    if isinstance(sibling, Tag):
                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        return self.get_end_date_by_regex(pattern, description)

    def get_location(self, item, title):
        location = None

        first_td = item.find('td')
        if first_td:
            location_tag = first_td.find_next_sibling('td')
            if location_tag:
                location = location_tag.get_text().strip()
            else:
                log_support.set_invalid_location(self.client_name, title)

        return location


class Caverion(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "Items" in json_dict:
            for item in json_dict["Items"]:
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

        if "Title" in item:
            title = item["Title"]
            if "Link" in item:
                description_url = item["Link"]
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')

            # it has a table where the second <td> of the first <tr> contains the job description
            table = soup.find('table')
            if table:
                tr = table.find('tr')
                if tr:
                    all_td = tr.find_all("td")
                    if len(all_td) == 2:
                        for child in all_td[1].children:
                            Scraper.clean_attrs(child)
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None
        locations = []

        if "Cities" in item and len(item["Cities"]) > 0:
            locations = item["Cities"]

        if locations:
            location = ", ".join(locations)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "EndDate" in item:
            # Formatted as "/Date(1544313600000)/"
            end_date_raw = item["EndDate"]
            epoch = re.findall("[0-9]+", end_date_raw)
            if len(epoch) == 1:
                seconds = int(epoch[0][:-3])
                end_date = time.strftime('%Y-%m-%d', time.gmtime(seconds))

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Canter(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        open_positions = soup.find('h3', string="Open Positions")
        if open_positions:
            previous_section = open_positions.find_parent('section')
            if previous_section:
                section = previous_section.find_next_sibling('section')
                if section:
                    for item in section.find_all("a"):
                        title, description_url, description = self.get_mandatory_fields(item)
                        if self.is_valid_job(title, description_url, description):

                            job = ScrapedJob(title, description, "Espoo", self.client_name, None, None, None, None, description_url)
                            jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""

        title = item.get_text()

        description_url = item.get('href')
        if description_url:
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_block = soup.find('section', class_='av_textblock_section')
            if details_block:
                job_title = details_block.find(["h1", "h2"])
                if job_title:
                    for sibling in job_title.next_siblings:
                        if sibling.name == "h2":
                            sibling.name = "h3"

                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description


class Gapps(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        jobs_div = soup.find('div', class_='row section-columns-wrapper justify-content-center')
        if jobs_div:
            for item in jobs_div.children:
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):

                    job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h3")
        if title_tag:
            title = title_tag.get_text()
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_block = soup.find('div', class_='public-job-description')
            if details_block:
                for child in details_block.children:
                    Scraper.clean_attrs(child)
                    if isinstance(child, Tag) and child.get_text().strip() != "":
                        description += str(child)

        return description


class ProfitSoftware(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all('article', class_='et_pb_post'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):

                job = ScrapedJob(title, description, None, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h2", class_='entry-title')
        if title_tag:
            title = title_tag.get_text()
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_block = soup.find('div', class_='entry-content')
            if details_block:
                for child in details_block.children:
                    if isinstance(child, Tag):
                        if child.name == "img":
                            continue
                        if child.find('img'):
                            child.find('img').decompose()

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class InnokasMedical(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='vc_column_container'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description)
                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find("h2")
        if title_tag:
            title = title_tag.get_text()
            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            # There are two different job descriptions
            details_block = soup.find('span', {'id': 'hs_cos_wrapper_post_body'})
            if not details_block:
                details_block = soup.find('div', class_='theme-content')

            if details_block:
                for child in details_block.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.name == "h2" and child.get_text() == "Read more about Innokas!":
                            break

                        if child.name == "h2":
                            child.name = "h4"
                        if child.name == "h3":
                            child.name = "h5"

                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    @staticmethod
    def get_location(description):
        locator = CityLocator()

        cities = locator.get_finnish_cities(description)
        if cities:
            location = ", ".join(c.name for c in cities)
        else:
            location = None

        return location


class Tikkurila(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='view-open-positions')
        if container:
            for item in container.find_all('div', class_='views-field'):
                title, description_url, description, end_date, is_enabled = self.get_mandatory_fields(item)

                if is_enabled and self.is_valid_job(title, description_url, description):
                    job = ScrapedJob(title, description, "Vantaa", self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = end_date = None
        description = ""
        is_enabled = True

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.get_text()
            description_url = url_tag.get('href')
            if description_url:
                description, end_date, is_enabled = self.get_description(description_url, title)

        return title, description_url, description, end_date, is_enabled

    def get_description(self, url, title):
        description = ""
        end_date = None
        enabled = True

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')

            # some links are pointing to invalid job descriptions
            if soup.find('span', class_='error'):
                enabled = False
            else:
                details_block = soup.find('div', class_='job_description')
                if details_block:
                    for child in details_block.children:
                        if isinstance(child, Tag):
                            if child.name == "img" or child.find('img'):
                                continue

                            Scraper.clean_attrs(child)
                            if child.get_text().strip() != "":
                                description += str(child)

                # we return the end_date from get_description to save a request later
                dates = soup.find_all('span', class_='se_date')
                if len(dates) == 2:
                    end_date_raw = dates[1].get_text()
                    try:
                        end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
                    except ValueError:
                        log_support.set_invalid_dates(self.client_name, title)

        return description, end_date, enabled


class Frogmind(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='job-excerpt'):
            # skip initial block
            if item.find('article'):
                continue

            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                job = ScrapedJob(title, description, "Helsinki", self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            description_url = url_tag.get('href')

            title_tag = item.find('h3')
            if title_tag:
                a = title_tag.find('a')
                if a:
                    a.decompose()
                title = title_tag.get_text()

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            details_block = soup.find('div', class_='entry-content')
            if details_block:
                for child in details_block.children:
                    if isinstance(child, Tag):
                        if child.name == "img" or child.find('img'):
                            continue

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class Zynga(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='listing'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='section section2')
            if container:
                apply_btn = container.find('div', class_='center-align')
                if apply_btn:
                    for sibling in apply_btn.next_siblings:
                        if isinstance(sibling, Tag):
                            if sibling.find('a', class_='btn'):
                                continue

                            Scraper.clean_attrs(sibling)
                            if sibling.get_text().strip() != "":
                                description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_='location')
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Thermofisher(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', class_='JobListTable')
        if table:
            for item in table.find_all("tr"):
                if item.find('th') or item.find('td', class_='job-filter'):
                    continue

                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('td', class_='coloriginaljobtitle')
        if title_tag:
            title = title_tag.text.strip()
            url_tag = title_tag.find('a')
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='jobdescription-row description')
            if container:
                description_parent = container.find('div', class_='jobdescription-value')
                if description_parent:
                    for child in description_parent.children:
                        Scraper.clean_attrs(child)
                        if child.name and child.get_text().strip() == "":
                            continue
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('td', class_='collongtextfield1')
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"\d{1,2}((st)|(nd)|(rd)|(th))(\s+of)?\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)(\s[0-9]{4})?"
        patterns = [pattern1, pattern2]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

        return end_date


class Sap(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', {'id': 'searchresults'})
        if table:
            for item in table.find_all("tr", class_='data-row'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='jobTitle')
        if title_tag:
            title = title_tag.text.strip()
            url_tag = title_tag.find('a')
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_parent = soup.find('span', class_='jobdescription')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='jobLocation')
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Here(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li', class_='row'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Tampere"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', class_='title')
        if title_tag:
            title_spans = title_tag.find_all('span')
            if len(title_spans) == 2:
                title = title_spans[1].get_text().strip()
                title = title.split(" - HERE")[0]
                url_tag = title_tag.find('a')
                if url_tag:
                    description_url = url_tag.get('href')
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        video_found = False

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_parent = soup.find('div', class_='iCIMS_JobContent')
            if description_parent:
                job_summary = description_parent.find('div', class_='iCIMS_JobsTable')
                if job_summary:
                    for sibling in job_summary.next_siblings:
                        if isinstance(sibling, Tag):
                            Scraper.clean_attrs(sibling)

                            if video_found:
                                break

                            if sibling.find('iframe'):
                                sibling.find('iframe').decompose()
                                video_found = True

                            if sibling.name == "h3":
                                sibling.name = "h4"
                            if sibling.name == "h2":
                                sibling.name = "h3"

                            if sibling.get_text().strip() != "":
                                description += str(sibling)

        return description


class Agco(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', {'id': 'searchresults'})
        if table:
            for item in table.find_all("tr", class_='data-row'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='jobTitle')
        if title_tag:
            title = title_tag.text.strip()
            url_tag = title_tag.find('a')
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_parent = soup.find('span', class_='jobdescription')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='jobLocation')
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"\d{1,2}((st)|(nd)|(rd)|(th))(\s+of)?\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)(\s[0-9]{4})?"
        patterns = [pattern1, pattern2]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

        return end_date


class OpenText(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li', class_='jobResultItem'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find("a")
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)

        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='jobDetailDescription')
            if container:
                sibling = container.find_next_sibling('div')
                if sibling:
                    for child in sibling.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            if child.get_text().strip() != "":
                                description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='locationText')
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Danfoss(Scraper):

    # POST request to https://krb-xjobs.brassring.com/TgNewUI/Search/Ajax/PowerSearchJobs

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []

        post_url = "https://krb-xjobs.brassring.com/TgNewUI/Search/Ajax/PowerSearchJobs"
        body = {
            "partnerId": "30033",
            "siteId": "5635",
            "keywordCustomSolrFields": "JobTitle,AutoReq,FORMTEXT19,FORMTEXT17,FORMTEXT23",
            "turnOffHttps": False,
            "Latitude": 0,
            "Longitude": 0,
            "powersearchoptions": {"PowerSearchOption": [{"VerityZone": "FORMTEXT2", "Type": "multi-select", "OptionCodes": ["Finland"]}]}
            }

        html = request_support.simple_post(post_url, body=body)
        if html:
            json_dict = json.loads(html)
            if "Jobs" in json_dict and "Job" in json_dict["Jobs"]:
                for item in json_dict["Jobs"]["Job"]:
                    title, description_url, description, location = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = location = None
        description = ""

        if "Questions" in item:
            for question in item["Questions"]:
                if question["QuestionName"] == "jobtitle":
                    title = question["Value"]

                # we get the location here so we save a HTML call then
                if question["QuestionName"] == "formtext32":
                    location = question["Value"]

        if "Link" in item:
            description_url = item["Link"]
            description = self.get_description(description_url)

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return title, description_url, description, location

    @staticmethod
    def get_description(url):
        description = ""
        desc1 = None
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            description_soup = BeautifulSoup(job_details_html, 'html.parser')
            script = description_soup.find('input', {'id': 'preLoadJSON'})
            if script:
                if script.has_attr("value"):
                    json_dict = json.loads(script["value"])
                    if "Jobdetails" in json_dict and "JobDetailQuestions" in json_dict["Jobdetails"]:
                        for question in json_dict["Jobdetails"]["JobDetailQuestions"]:
                            if "QuestionName" in question and "AnswerValue" in question:
                                if question["QuestionName"] == "Job Description":
                                    desc1 = question["AnswerValue"]
                                    break

                    if desc1:
                        description_soup = BeautifulSoup(desc1, "html.parser")
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)

        return description

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


class Accountor(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        table = soup.find('table', class_='jobs_table')
        if table:
            for item in table.find_all("tr", class_='jobs_row'):
                # if it is the header, skip
                if item.find('td', class_='jobs_cell_top'):
                    continue

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
            title = title.split("- Accountor HR4")[0].strip()
            title = title.split(", Accountor HR4")[0].strip()
            title = title.split(", Accountor Enterprise Solutions Oy")[0].strip()

            description_url = title_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='executer_vacancy_text')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        cells = item.find_all('td', class_='jobs_cell')
        if len(cells) == 3:
            location = cells[1].get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        cells = item.find_all('td', class_='jobs_cell')
        if len(cells) == 3:
            end_date_raw = cells[2].get_text().strip()
            try:
                end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Iceye(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all("li", class_='job'):
            # if it is the header, skip
            if item.find('td', class_='jobs_cell_top'):
                continue

            title, description_url, description, is_finnish = self.get_mandatory_fields(item)
            if is_finnish and self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        finnish = True

        location_tag = item.find('p', class_='meta')
        if location_tag:
            finnish = "Finland" in location_tag.get_text()

        if finnish:
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.text.strip()

                relative_url = title_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description, finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            sections = soup.find_all('section', class_='section section--text')

            for section in sections:
                for child in section.children:
                    if isinstance(child, Tag):
                        if child.name == "h2":
                            child.name = "h3"
                        elif child.name == "h3":
                            child.name = "h4"

                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('p', class_='meta')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Digia(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html.decode('utf-8'), 'html.parser')

        table = soup.find('table', {'id': 'auto_list_table_open_jobs'})
        if table:
            for item in table.find_all("tr"):
                # if it is the header, skip
                if item.find('th'):
                    continue

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
                description_url = self.url.split(".com/")[0] + ".com" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='job_description')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('td', class_='col_City')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('td', class_='col_ApplyEndDate')
        if end_date_tag:
            end_date_raw = end_date_tag.get_text().strip()
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class BdsBynfo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all("div", class_='position column'):
            # if it is the header, skip
            if item.find('th'):
                continue

            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Helsinki, Tampere"  # it has two possible locations and the job description does not say which one.

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.text.strip()

            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find(lambda tag: tag.name == "span" and tag['id'] and "hs_cos_wrapper_widget_" in tag['id'])
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('td', class_='col_City')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class BookIt(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        for item in soup.find_all("div", class_='open-position-item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Helsinki"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('a', class_='position-title')
        if title_tag:
            title = title_tag.get_text().strip()
            description_url = title_tag.get('href')
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('span', {'id': 'hs_cos_wrapper_post_body'})
            if description_parent:
                for child in description_parent.children:
                    Scraper.clean_attrs(child)
                    description += str(child)

        return description


class Enfuce(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('ul', class_='jobs')
        if container:
            for item in container.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
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
            description_parent = soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Giosg(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('ul', class_='jobs')
        if container:
            for item in container.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
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
            description_parent = soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        # skip the video
                        if child.find('iframe'):
                            continue
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Inderes(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('ul', class_='jobs')
        if container:
            for item in container.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Helsinki"  # a unique office located in Helsinki

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class LvsBrokers(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('ul', class_='jobs')
        if container:
            for item in container.find_all("li"):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
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
            description_parent = soup.find('div', class_='body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class OpusCapitaSolutions(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', class_='jobs')
        if table:
            for item in table.find_all("tr"):
                # if it is the header, skip
                if item.find('th'):
                    continue

                title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                if is_finnish and self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        finnish = True

        all_td = item.find_all('td')
        if len(all_td) == 4:
            finnish = "Finland" in all_td[2].get_text()

        if finnish:
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.get_text().strip()

                description_url = title_tag.get('href')
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description, finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_parent = soup.find('div', class_='joqReqDescription')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        all_td = item.find_all('td')
        if len(all_td) == 4:
            location = all_td[1].get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        all_td = item.find_all('td')
        if len(all_td) == 4:
            end_date_raw = all_td[3].get_text()
            try:
                end_date = parser.parse(end_date_raw, dayfirst=True).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Poolia(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "items" in json_dict:
            for item in json_dict["items"]:
                if "company" in item and "Poolia" in item["company"]:
                    title, description_url, description, location = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = location = None
        description = ""

        if "heading" in item:
            title = item["heading"]
            if "friendlyurl" in item:
                description_url = self.url.split('.fi/')[0] + ".fi" + item["friendlyurl"]
                description, location = self.get_description(description_url, title)

        return title, description_url, description, location

    def get_description(self, url, title):
        description = ""
        location = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            first_p = soup.find('p', {'class': 'preamble'})
            if first_p:
                Scraper.clean_attrs(first_p)
                description += str(first_p)

                for sibling in first_p.next_siblings:
                    if isinstance(sibling, Tag):
                        if sibling.name == 'div' and sibling.has_attr("class") and "ad-contact" in sibling["class"]:
                            break
                        if sibling.name == "h3" and "Yhteyshenkilö" in sibling.get_text():
                            break

                        Scraper.clean_attrs(sibling)
                        if sibling.get_text().strip() != "":
                            description += str(sibling)

            location_tag = soup.find('span', {'itemprop': 'address'})
            if location_tag:
                location = location_tag.get_text()
            else:
                log_support.set_invalid_location(self.client_name, title)

        return description, location


class SuoraTyo(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('ul', class_='o-layout')
        if container:
            for item in container.find_all("li", class_='o-layout__item'):
                # skip "Avoin Hakemus" which fails in get_mandatory_fields()
                if item.find('h3'):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3', {'itemprop': 'title'})
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='c-post__body')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.name == "h3":
                            child.name = "h4"
                        if child.name == "h2":
                            child.name = "h3"
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', {'itemprop': 'jobLocation'})
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class TomorrowTech(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        container = soup.find('div', class_='announcements')
        if container:
            for item in container.find_all("h3"):
                title = item.get_text().strip()
                url_item = item.find_next_sibling('a')
                if url_item:
                    description_url = self.url.split(".fi/")[0] + ".fi/" + url_item.get('href')
                    description = self.get_description(description_url)

                    if self.is_valid_job(title, description_url, description):
                        location = "Helsinki"

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'html.parser')
            description_parent = soup.find('div', class_='content')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class Vauraus(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all("div", class_="career-item"):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(description, title)
                end_date = self.get_end_date(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', class_='career-title')
        if title_tag:
            title = title_tag.get_text().strip()

            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_parent = soup.find('div', class_='application-description')
            if description_parent:
                for child in description_parent.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, description, title):
        location = ""

        if "Helsingin" in description or "Helsinki" in description or "Helsingissä" in description:
            location += ", Helsinki"
        if "Tampereelle" in description or "Tampere" in description:
            location += ", Tampere"
        if "Joensuuhun" in description or "Joensuu" in description:
            location += ", Joensuu"
        if "Pohjanmaalle" in description or "Pohjanmaa" in description:
            location += ", Pohjanmaa"
        if "Kuopioon" in description or "Kuopio" in description:
            location += ", Kuopio"

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('div', class_='career-date')
        if end_date_tag:
            pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
            end_date = self.get_end_date_by_regex(pattern, end_date_tag.get_text())

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Nixu(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', class_='table')
        if table:
            for item in table.find_all("tr"):
                # if it is the header, skip
                if item.find('th'):
                    continue

                title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                if is_finnish and self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        finnish = True

        all_td = item.find_all('td')
        if len(all_td) == 4:
            finnish = "Finland" in all_td[1].get_text()

        if finnish:
            title_tag = item.find('a')
            if title_tag:
                title = title_tag.get_text().strip()
                relative_url = title_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".com/")[0] + ".com" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description, finnish

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            description_blocks = soup.find_all('div', {'id': ['ctl00_cphContent_divJobDesc', 'ctl00_cphContent_divReqProfile', 'ctl00_cphContent_divAboutCompany', 'ctl00_cphContent_divApplicationInstructions']})
            for block in description_blocks:
                for child in block.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        all_td = item.find_all('td')
        if len(all_td) == 4:
            location = all_td[2].get_text()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Terveystalo(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "Rows" in json_dict:
            for item in json_dict["Rows"]:
                title, description_url, description, end_date = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = end_date = None
        description = ""

        if "Tehtava" in item:
            title = item["Tehtava"].strip().capitalize()
            if "Link" in item:
                description_url = item["Link"]
                description, end_date = self.get_description(description_url, title)

        return title, description_url, description, end_date

    def get_description(self, url, title):
        description = ""
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')

            parent = soup.find('div', class_='multiline-text')
            for child in parent.children:
                Scraper.clean_attrs(child)
                description += str(child)

            end_date = self.get_end_date(soup, title)

        return description, end_date

    def get_location(self, item, title):
        location = None

        if "RekPaikkakunnat" in item and len(item["RekPaikkakunnat"]) > 0 and "PaikkakunnanNimi" in item["RekPaikkakunnat"][0]:
            location = item["RekPaikkakunnat"][0]["PaikkakunnanNimi"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, soup, title):
        text = ""

        #  we don't have the end_date information in the description, we have to get it
        tags = soup.find_all('div', class_='row')
        for tag in tags:
            text += tag.get_text()

        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        end_date = self.get_end_date_by_regex(pattern, text)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Zervant(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "jobAds" in json_dict:
            for item in json_dict["jobAds"]:
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

        if "title" in item:
            title = item["title"]
            if "slug" in item:
                description_url = self.url.split(".com")[0] + ".com/careers/en/zervant/" + item["slug"]

            if "description" in item:
                description = item["description"]

        return title, description_url, description

    def get_location(self, item, title):
        location = None

        if "location" in item:
            location = item["location"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "endTime" in item:
            end_date_raw = item["endTime"]
            end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Helvar(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', {'id': 'items'})
        if container:
            for item in container.find_all("div", class_="itemList"):
                if self.is_finnish(item):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = "Espoo"
                        end_date = self.get_end_date(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True

        location_tag = item.find('div', class_='tags_location')
        if location_tag:
            finnish = ("Finland" in location_tag.get_text())

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', class_='head')
        if title_tag:
            url_tag = title_tag.find('a')
            if url_tag:
                title = url_tag.get_text()
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".se/")[0] + ".se/" + relative_url
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='job_desc')
            for child in container.children:
                if isinstance(child, Tag):
                    Scraper.clean_attrs(child)
                    if child.get_text().strip() != "":
                        description += str(child)

        return description

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('span', class_='last_apply_date')
        if end_date_tag:
            end_date_raw = end_date_tag.get_text()
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class VTT(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html.decode('utf-8'), 'lxml')

        container = soup.find('div', class_='job-list')
        if container:
            for item in container.find_all("a", class_="list-item"):
                title, description_url, description, location = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    end_date = self.get_end_date(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = location = None
        description = ""

        title_tag = item.find('h2', class_='list-item__title')
        if title_tag:
            title = title_tag.get_text()

            relative_url = item.get('href')
            if relative_url:
                description_url = self.url.split(".fi/")[0] + ".fi" + relative_url
                description, location = self.get_description(description_url, title)

        return title, description_url, description, location

    def get_description(self, url, title):
        description = ""
        location = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            containers = soup.find_all('div', class_='description-group')
            for container in containers:
                for child in container.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

            location = self.get_location(soup, title)

        return description, location

    def get_location(self, item, title):
        location = None

        container = item.find('div', class_='vacancy__basic-info')
        if container:
            location_tag = container.find(lambda tag: tag.name == "p" and "Locations:" in tag.get_text())
            if location_tag:
                location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        end_date_tag = item.find('div', class_='list-item__end-date')
        if end_date_tag:
            end_date_raw = end_date_tag.get_text()
            pattern = r"[0-9]{4}\.[0-9]{1,2}\.[0-9]{1,2}"
            end_date = self.get_end_date_by_regex(pattern, end_date_raw, day_first=False)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class Metsa(Scraper):
    page_offset = 50

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)

        # we need to overwrite html with the JSON response
        html = request_support.simple_get(self.url, accept_json=True)
        json_dict = json.loads(html)

        jobs_list = self.get_jobs_list(json_dict)
        if jobs_list:
            for item in jobs_list:
                title, description_url, description, is_finnish = self.get_mandatory_fields(item)
                if is_finnish and self.is_valid_job(title, description_url, description):
                    # location has already being checked in get_mandatory_fields()
                    location = item["subtitles"][0]["instances"][0]["text"]
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

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
                children = json_dict["body"]["children"][1]["children"][0]["children"]
                for child in children:
                    if "text" in child:
                        description_raw = child["text"]
                        description_soup = BeautifulSoup(description_raw, "html.parser")
                        for tag in description_soup.children:
                            if isinstance(tag, Tag):
                                Scraper.clean_attrs(tag)
                                if tag.text != "\xa0" and tag.text.strip() != "":
                                    description += str(tag)

                        break
            except (ValueError, KeyError, IndexError, AttributeError):
                description = ""

        return description

    def get_end_date(self, description):
        end_date = None
        pattern1 = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        pattern2 = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2}((st)|(nd)|(rd)|(th)),?\s+\d{4}"
        pattern3 = r"\d{1,2}((st)|(nd)|(rd)|(th))\s+(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{4}"
        patterns = [pattern1, pattern2, pattern3]

        for pattern in patterns:
            end_date = self.get_end_date_by_regex(pattern, description)
            if end_date:
                break

        return end_date


class MFiles(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html.decode('utf-8'), 'lxml')

        for item in soup.find_all("div", class_="item"):
            if self.is_finnish(item):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True

        location_tag = item.find('div', class_='item-address')
        if location_tag:
            finnish = ("Finland" in location_tag.get_text())

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('div', class_='item-name')
        if title_tag:
            title = title_tag.get_text().strip()

            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('span', {'id': 'lblPositionDetails'})
            for child in container.children:
                if isinstance(child, Tag):
                    if child.name == 'p' and child.has_attr("class") and "text_header_2" in child["class"]:
                        continue

                    Scraper.clean_attrs(child)
                    if child.get_text().strip() != "":
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_='item-address')
        if location_tag:
            location = location_tag.get_text().strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description, title):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        end_date = self.get_end_date_by_regex(pattern, description)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class UBlox(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for container in soup.find_all(lambda tag: tag.name == "h3" and "Finland" in tag.get_text()):
            block = container.find_next_sibling('p')
            if block:
                for item in block.find_all('a'):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = container.get_text()

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""

        title = item.get_text()
        description_url = item.get('href')
        if description_url:
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='sfdc_richtext')

            for child in container.children:
                if isinstance(child, Tag):
                    Scraper.clean_attrs(child)
                    if child.get_text().strip() != "":
                        description += str(child)
                else:
                    p_tag = soup.new_tag('p')
                    p_tag.string = child
                    if child != "\xa0":
                        description += str(p_tag)

        return description


class Ubisecure(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('section', class_='')
        if container:
            for item in container.find_all('p'):
                # skip email link
                if item.find('a') and "mailto:" in item.find('a').get('href'):
                    continue

                title, description_url, description, valid = self.get_mandatory_fields(item)
                if valid and self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""
        valid = True

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')

            # Some jobs are pointing to indeed.co.uk or indeed.fi. Since we don't scrap indeed portal, we skip those jobs
            valid = "www.indeed." not in description_url

            if valid and description_url:
                description = self.get_description(description_url)

        return title, description_url, description, valid

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('section', class_='')
            if container:
                first_p = container.find('p')

                if first_p:
                    # first p is for the location so we can skip it
                    for sibling in first_p.next_siblings:
                        if isinstance(sibling, Tag):
                            Scraper.clean_attrs(sibling)
                            if sibling.get_text().strip() != "":
                                description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span')
        if location_tag:
            location = location_tag.get_text().split("|")[0].strip()

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Fluent(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='blog-lifts__item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                # It has two offices in Joensuu and Espoo but currently all jobs are based on Joensuu
                location = "Joensuu"

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3')
        if title_tag:
            title = title_tag.get_text()

            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', {'id': 'content'})
            if container:
                block = container.find('div', class_='wrapper-mw-715')
                for child in block.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.name == "h2":
                            child.name = "h3"
                        elif child.name == "h3":
                            child.name = "h4"

                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class Nortal(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            if self.is_finnish(item):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True

        if "categories" in item and "location" in item["categories"]:
            finnish = "Finland" in item["categories"]["location"]

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "text" in item:
            title = item["text"]
            if "hostedUrl" in item:
                description_url = item["hostedUrl"]

            if "description" in item:
                description = self.get_description(item)

        return title, description_url, description

    @staticmethod
    def get_description(item):
        description = ""
        description_raw = item["description"]

        soup = BeautifulSoup("", 'html.parser')

        if "lists" in item:
            for section in item["lists"]:
                if "text" in section:
                    text_tag = soup.new_tag('h4')
                    text_tag.string = section["text"]
                    description_raw += str(text_tag)
                if "content" in section:
                    description_raw += section["content"]

        if "additional" in item:
            description_raw += item["additional"]

        soup = BeautifulSoup(description_raw, 'html.parser')
        for tag in soup.children:
            if isinstance(tag, Tag):
                Scraper.clean_attrs(tag)
                description += str(tag)

        return description

    def get_location(self, item, title):
        location = None

        if "categories" in item and "location" in item["categories"]:
            location = item["categories"]["location"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Ul(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')

        open_positions = soup.find('h2', string="Open positions")
        if open_positions:
            container = open_positions.find_next_sibling('ul')
            if container:
                for item in container.find_all('li'):
                    title, description_url, description, location = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description_url = None
        description = ""
        location = None

        title = item.get_text().strip()
        url_tag = item.find('a')
        if url_tag:
            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url + relative_url
                description, location = self.get_description(description_url)

        return title, description_url, description, location

    @staticmethod
    def get_description(description_url):
        description = ""
        location = None

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')

            # take the name after the #
            name_block = description_url.split("#")[1]
            container = soup.find('a', {'name': name_block})
            if container:
                parent = container.parent
                first_p = parent.find_next_sibling('p')
                if first_p:
                    location = first_p.get_text().split("|")[0]
                    for sibling in first_p.next_siblings:
                        if isinstance(sibling, Tag):
                            # if we finds a h2, it means the next job
                            if sibling.name == "h2" or (sibling.name == "p" and sibling.has_attr('class') and "mt10" in sibling["class"]):
                                break
                            Scraper.clean_attrs(sibling)
                            description += str(sibling)

        return description, location


class Fira(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='c-career'):
            title, description_url, description, end_date = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = end_date = None
        description = ""

        title_tag = item.find('h4')
        if title_tag:
            title = title_tag.get_text()

            url_tag = item.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                description, end_date = self.get_description(description_url, title)

        return title, description_url, description, end_date

    def get_description(self, url, title):
        description = ""
        end_date = None

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', {'id': 'job-description'})
            if container:
                block = container.find('div')
                for child in block.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

            end_date = self.get_end_date(soup, title)

        return description, end_date

    def get_end_date(self, soup, title):
        end_date = None

        end_date_tag = soup.find('div', {'id': 'apply-attributes'})
        if end_date_tag and end_date_tag['data-duedate']:
            end_date_raw = end_date_tag['data-duedate']
            try:
                end_date = parser.parse(end_date_raw).strftime('%Y-%m-%d')
            except (ValueError, TypeError):
                pass

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date

    def get_location(self, item, title):
        location = None

        location_tag = item.find('h5', class_="c-career__location")
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class GE(Scraper):

    # POST request to https://jobs.gecareers.com/widgets

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []

        post_url = "https://jobs.gecareers.com/widgets"
        body = {
                "lang": "en_global",
                "deviceType": "desktop",
                "country": "global",
                "ddoKey": "eagerLoadRefineSearch",
                "sortBy": "Most recent",
                "subsearch": "",
                "from": 0,
                "jobs": True,
                "counts": True,
                "all_fields": [
                    "category",
                    "country",
                    "state",
                    "city",
                    "business",
                    "type"
                ],
                "pageName": "GE Healthcare Jobs",
                "pageType": "landingPage",
                "size": 10,
                "rk": "l-ge-healthcare-jobs",
                "clearAll": False,
                "jdsource": "facets",
                "isSliderEnable": False,
                "keywords": "",
                "global": True,
                "selected_fields": {
                    "country": [
                        "Finland"
                    ]
                },
                "sort": {
                    "order": "desc",
                    "field": "postedDate"
                },
                "rkstatus": True,
                "s": "1"
            }

        html = request_support.simple_post(post_url, body=body)
        if html:
            json_dict = json.loads(html)
            if "eagerLoadRefineSearch" in json_dict and "data" in json_dict["eagerLoadRefineSearch"] and "jobs" in json_dict["eagerLoadRefineSearch"]["data"]:
                for item in json_dict["eagerLoadRefineSearch"]["data"]["jobs"]:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)
                        end_date = self.get_end_date(description, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "title" in item:
            title = item["title"]
            if "applyUrl" in item:
                description_url = item["applyUrl"]
                description = self.get_description(description_url)

        return title, description_url, description

    def get_description(self, description_url):
        description = ""
        desc1 = desc2 = desc3 = desc4 = None

        job_details_html = request_support.simple_get(description_url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            script = soup.find('input', {'id': 'preLoadJSON'})
            if script:
                if script.has_attr("value"):
                    json_dict = json.loads(script["value"])
                    if "Jobdetails" in json_dict and "JobDetailQuestions" in json_dict["Jobdetails"]:
                        for question in json_dict["Jobdetails"]["JobDetailQuestions"]:
                            if "QuestionName" in question and "AnswerValue" in question:
                                if question["QuestionName"] == "Role Summary/Purpose":
                                    desc1 = question["AnswerValue"]
                                if question["QuestionName"] == "Essential Responsibilities":
                                    desc2 = question["AnswerValue"]
                                if question["QuestionName"] == "Qualifications/Requirements":
                                    desc3 = question["AnswerValue"]
                                if question["QuestionName"] == "Desired Characteristics":
                                    desc4 = question["AnswerValue"]

                    if desc1:
                        description_soup = BeautifulSoup(desc1, "html.parser")
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)
                            else:
                                tag = self.create_tag('p', child)
                                description += str(tag)

                    if desc2:
                        description_soup = BeautifulSoup(desc2, "html.parser")
                        tag = self.create_tag('h3', "Essential Responsibilities")
                        description += str(tag)
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)
                            else:
                                tag = self.create_tag('p', child)
                                description += str(tag)

                    if desc3:
                        description_soup = BeautifulSoup(desc3, "html.parser")
                        tag = self.create_tag('h3', "Qualifications/Requirements")
                        description += str(tag)
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)
                            else:
                                tag = self.create_tag('p', child)
                                description += str(tag)

                    if desc4:
                        description_soup = BeautifulSoup(desc4, "html.parser")
                        tag = self.create_tag('h3', "Desired Characteristics")
                        description += str(tag)
                        for child in description_soup.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)
                            else:
                                tag = self.create_tag('p', child)
                                description += str(tag)

        return description

    @staticmethod
    def create_tag(tag_name, text):
        soup = BeautifulSoup("", "html.parser")
        p_tag = soup.new_tag(tag_name)
        p_tag.string = text
        return p_tag

    def get_location(self, item, title):
        location = None

        if "city" in item:
            location = item["city"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description, title):
        pattern = r"(Jan(uary)?|Feb(ruary)?|Mar(ch)?|Apr(il)?|May|Jun(e)?|Jul(y)?|Aug(ust)?|Sep(tember)?|Oct(ober)?|Nov(ember)?|Dec(ember)?)\s+\d{1,2},?\s+\d{4}"
        end_date = self.get_end_date_by_regex(pattern, description)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class IQVIA(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('tr', class_='job-result'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text()
            # Remove "based in" from title
            if "home-based in" in title or "based in" in title or "(R" in title:
                title = title.split("home-based in")[0].split("based in")[0].split("(R")[0].strip()
                if title[-1] == "/" or title[-1] == "-":
                    title = title[:-1].strip()

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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='jdp-job-description-card')
            if container:
                header = container.find('h2', class_='content-card-header')
                if header:
                    for sibling in header.next_siblings:
                        if isinstance(sibling, Tag):
                            Scraper.clean_attrs(sibling)
                            if sibling.get_text().strip() != "":
                                description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('div', class_="job-location-line")
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Intel(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', class_='JobListTable')
        if table:
            for item in soup.find_all('tr'):
                if item.find('th') or item.find('td', class_='job-filter'):
                    continue

                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text()
            title_array = title.split(" - ")
            if len(title_array) > 1:
                title = title_array[1]

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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='jobdescriptiontbl')
            if container:
                header = container.find('h3')
                for sibling in header.next_siblings:
                    if isinstance(sibling, Tag):
                        Scraper.clean_attrs(sibling)
                        if sibling.get_text().strip() != "":
                            description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('td', class_="colcity")
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Oracle(Scraper):

    # POST request to https://oracle.taleo.net/careersection/rest/jobboard/searchjobs?portal=101430233

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []

        post_url = "https://oracle.taleo.net/careersection/rest/jobboard/searchjobs?portal=101430233"
        header = {'tz': 'GMT+02:00'}
        body = {
            "multilineEnabled": True,
            "sortingSelection": {
                "sortBySelectionParam": "3",
                "ascendingSortingOrder": "false"
            },
            "fieldData": {
                "fields": {
                    "KEYWORD": "",
                    "LOCATION": ""
                },
                "valid": True
            },
            "filterSelectionParam": {
                "searchFilterSelections": [
                    {
                        "id": "LOCATION",
                        "selectedValues": [
                            "355040031553"
                        ]
                    }
                ],
                "activeFilterId": "LOCATION"
            },
            "pageNo": 1
        }

        html = request_support.simple_post(post_url, body=body, header=header)
        if html:
            json_dict = json.loads(html)
            if "requisitionList" in json_dict:
                for item in json_dict["requisitionList"]:
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "column" in item and len(item["column"]) > 0:
            title = item["column"][0]

            if "contestNo" in item:
                job_id = item["contestNo"]

                description_url = self.url.split('jobsearch.ftl')[0] + "jobdetail.ftl?job=" + job_id
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container_raw = soup.find('input', {'id': 'initialHistory'})
            if container_raw:
                container_array = container_raw["value"].split("!*!")
                if len(container_array) > 2:
                    description_raw = container_array[1]
                    description_html = urllib.parse.unquote(description_raw)
                    description_soup = BeautifulSoup(description_html, "html.parser")

                    for child in description_soup.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            if child.name == "h2":
                                child.name = "h3"
                            elif child.name == "h3":
                                child.name = "h4"

                            if child.get_text().strip() != "":
                                description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        if "column" in item and len(item["column"]) > 3:
            location = item["column"][3]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Documill(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('ul', class_='jobs-list')
        if jobs_div:
            for item in jobs_div.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Espoo"  # unique office located in Espoo

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            container = job_details_soup.find('div', class_='job-content-wrapper')
            if container:
                parent_div = container.find('div', class_='jobs-container')
                if parent_div:
                    for child in parent_div.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            description += str(child).strip()

        return description


class Elektrobit(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'html.parser')
        current_offset = 0
        offset = 20
        iteration = 0
        max_iteration = 20

        last_page = False
        while not last_page and iteration < max_iteration:
            iteration += 1
            table = soup.find('table', {'id': 'joboffers'})
            if not table or (table and not table.find('th')):
                break

            for item in table.find_all('tr'):
                if item.find('th') or item.find('td', {'id': 'rexx_footer'}):
                    continue

                if self.is_finnish(item):
                    title, description_url, description = self.get_mandatory_fields(item)
                    if self.is_valid_job(title, description_url, description):
                        location = self.get_location(item, title)

                        job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                        jobs.append(job)

            if self.is_last_page(soup):
                last_page = True
            else:
                current_offset += offset
                next_page_url = self.url.split("?start=")[0] + "?start=" + str(current_offset)
                job_details_html = request_support.simple_get(next_page_url)

                if job_details_html:
                    soup = BeautifulSoup(job_details_html, 'html.parser')
                else:
                    # in case of error, break
                    last_page = True

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True

        location_tag = item.find('td', class_='real_table_col2')
        if location_tag:
            finnish = "Finland" in location_tag.get_text()

        return finnish

    @staticmethod
    def is_last_page(soup):
        last_page = True

        ul_pagination = soup.find('ul', class_='path_nav')
        if ul_pagination:
            if ul_pagination.find('li', class_='nav_next') and ul_pagination.find('li', class_='nav_next').find('a'):
                last_page = False

        return last_page

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        # Check title
        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text()

            # Remove (Oulu) from title
            title = title.split("(Oulu)")[0].split("(OULU)")[0].strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            header = soup.find('h2')
            if header:
                for sibling in header.next_siblings:
                    if isinstance(sibling, Tag):
                        if sibling.name == "h3" and "Interested?" in sibling.get_text():
                            break
                        Scraper.clean_attrs(sibling)
                        description += str(sibling)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('td', class_='real_table_col2')
        if location_tag:
            location = location_tag.get_text()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Vainu(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('ul', class_='jobs')
        if jobs_div:
            for item in jobs_div.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".io/")[0] + ".io" + relative_url
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', class_='body')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class DearLucy(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('ul', class_='career-list')
        if jobs_div:
            for item in jobs_div.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Helsinki"

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            description_url = url_tag.get('href')
            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', {'itemprop': 'articleBody'})
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.find('img'):
                            continue

                        if child.get_text().strip() != "":
                            description += str(child)

        return description


class ElectronicArts(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "jobs" in json_dict:
            for item in json_dict["jobs"]:
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
            if "opportunityId" in item:
                job_id = item["opportunityId"]
                description_url = "https://ea.gr8people.com/index.gp?method=cappportal.showJob&opportunityid=" + job_id
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')
            json_tag = job_details_soup.find('script', {'type': 'application/ld+json'})
            if json_tag:
                json_dict = json.loads(json_tag.get_text())
                if "description" in json_dict:
                    description_raw = json_dict["description"]
                    soup = BeautifulSoup(description_raw, 'html.parser')
                    for tag in soup.children:
                        if isinstance(tag, Tag):
                            Scraper.clean_attrs(tag)
                            if tag.get_text().strip() != "":
                                description += str(tag)

        return description

    def get_location(self, item, title):
        location = None

        if "city" in item:
            location = item["city"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Sniffie(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        jobs_div = soup.find('ul', class_='jobs')
        if jobs_div:
            for item in jobs_div.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".io/")[0] + ".io" + relative_url
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', class_='body')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_='meta')
        if location_tag:
            location = location_tag.get_text()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Wolt(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        for item in json_dict:
            if self.is_finnish(item):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    @staticmethod
    def is_finnish(item):
        finnish = True

        if "categories" in item and "location" in item["categories"]:
            finnish = "Finland" in item["categories"]["location"]

        return finnish

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        if "text" in item:
            title = item["text"]
            if "hostedUrl" in item:
                description_url = item["hostedUrl"]

            if "description" in item:
                description = self.get_description(item)

        return title, description_url, description

    @staticmethod
    def get_description(item):
        description = ""
        description_raw = item["description"]

        soup = BeautifulSoup("", 'html.parser')

        if "lists" in item:
            for section in item["lists"]:
                if "text" in section:
                    text_tag = soup.new_tag('h4')
                    text_tag.string = section["text"]
                    description_raw += str(text_tag)
                if "content" in section:
                    description_raw += section["content"]

        if "additional" in item:
            description_raw += item["additional"]

        soup = BeautifulSoup(description_raw, 'html.parser')
        for tag in soup.children:
            if isinstance(tag, Tag):
                Scraper.clean_attrs(tag)
                description += str(tag)

        return description

    def get_location(self, item, title):
        location = None

        if "categories" in item and "location" in item["categories"]:
            location = item["categories"]["location"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Santapark(Scraper):

    def extract_info(self, html):
        # From API
        jobs = []
        log_support.log_extract_info(self.client_name)
        json_dict = json.loads(html)

        if "jobAds" in json_dict:
            for item in json_dict["jobAds"]:
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

        base_url = "https://www.recright.com/careers/fi/santapark-oy/"

        if "title" in item:
            title = item["title"]
            if "slug" in item:
                description_url = base_url + item["slug"]

                # check description_url works well
                request_support.simple_get(description_url)

            if "description" in item:
                description = self.get_description(item["description"])

        return title, description_url, description

    @staticmethod
    def get_description(item):
        description = ""

        soup = BeautifulSoup(item, 'html.parser')
        for tag in soup.children:
            if isinstance(tag, Tag):
                Scraper.clean_attrs(tag)
                description += str(tag)

        return description

    def get_location(self, item, title):
        location = None

        if "location" in item:
            location = item["location"]

        if not location:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, item, title):
        end_date = None

        if "endTime" in item:
            try:
                end_date_datetime = parser.parse(item["endTime"])
                end_date = end_date_datetime.strftime('%Y-%m-%d')
            except (ValueError, KeyError):
                end_date = None

        if not end_date:
            log_support.set_invalid_dates(self.client_name, title)

        return end_date


class NorthernLightsVillage(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li', class_='position transition'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = self.get_location(item, title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h2')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:
                relative_url = url_tag.get('href')
                if relative_url:
                    description_url = self.url.split(".hr/")[0] + ".hr" + relative_url
                    if description_url:
                        description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', class_='description')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('li', class_='location')
        if location_tag:
            location_span = location_tag.find('span')
            if location_span:
                location = location_span.get_text()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class Kakslauttanen(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('li', class_='page_item'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Saariselkä"  # only one hotel in Saariselkä

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            description_url = url_tag.get('href')
            title = url_tag.get_text().split(",")[0]

            if description_url:
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""
        job_details_html = request_support.simple_get(url)

        if job_details_html:
            job_details_soup = BeautifulSoup(job_details_html, 'lxml')

            parent_div = job_details_soup.find('div', class_='content')
            if parent_div:
                for child in parent_div.children:
                    if isinstance(child, Tag):
                        if child.name == "h1":
                            continue
                        Scraper.clean_attrs(child)
                        description += str(child)

        return description


class KeysightTechnologies(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        table = soup.find('table', class_='searchResults')
        if table:
            for item in soup.find_all('tr', class_='data-row'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text()
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('span', class_='jobdescription')
            if container:
                # First div will contain all job description
                first_div = container.find('div')
                if first_div:
                    for child in first_div.children:
                        if child.find('img'):
                            continue
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            if child.get_text().strip() != "":
                                description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_="jobLocation")
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location


class NipromecGroup(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        ul = soup.find('ul', class_='jobs')
        if ul:
            for item in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = self.get_location(item, title)
                    end_date = self.get_end_date(description)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='title')
        if title_tag:
            title = title_tag.get_text().strip()
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
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='body')
            if container:
                for child in container.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_location(self, item, title):
        location = None

        location_tag = item.find('span', class_="meta")
        if location_tag:
            location = location_tag.get_text().strip()
        else:
            log_support.set_invalid_location(self.client_name, title)

        return location

    def get_end_date(self, description):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"
        end_date = self.get_end_date_by_regex(pattern, description)
        return end_date


class Sellforte(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='w-btn-wrapper'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location = "Espoo"  # only one office in Espoo

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('span', class_='w-btn-label')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = item.find('a')
            if url_tag:

                div_id = url_tag.get('href')
                if div_id:
                    description_url = self.url + div_id
                    description = self.get_description(description_url, div_id)

        return title, description_url, description

    @staticmethod
    def get_description(url, div_id):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            job_id = div_id[1:]  # removes the '#'
            container = soup.find('section', {'id': job_id})
            if not container:
                container = soup.find('div', {'id': job_id})

            if container:
                description_blocks = container.find_all("div", class_=lambda value: value and "vc_custom_" in value)
                if description_blocks:
                    parent = description_blocks[-1].find('div', class_='wpb_wrapper')
                    if parent:
                        for child in parent.children:
                            if isinstance(child, Tag):
                                Scraper.clean_attrs(child)
                                if child.get_text().strip() != "":
                                    description += str(child)

        return description


class DazzleRocks(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        ul = soup.find('ul', class_='alt')
        if ul:
            for item in ul.find_all('li'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Helsinki"  # Only one office located in Helsinki

                    job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        url_tag = item.find('a')
        if url_tag:
            title = url_tag.get_text().strip()
            relative_url = url_tag.get('href')
            if relative_url:
                description_url = self.url.split("/positions/")[0] + "/positions/" + relative_url
                description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            header = soup.find('span', class_='image main')
            if header:
                for sibling in header.next_siblings:
                    if isinstance(sibling, Tag):
                        # if we find the hr, break
                        if sibling.name == "hr":
                            break
                        Scraper.clean_attrs(sibling)
                        if sibling.get_text().strip() != "":
                            description += str(sibling)

        return description


class Codemate(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        for item in soup.find_all('div', class_='grid-entry'):
            title, description_url, description = self.get_mandatory_fields(item)
            if self.is_valid_job(title, description_url, description):
                location, title = self.get_location(title)

                job = ScrapedJob(title, description, location, self.client_name, None, None, None, None, description_url)
                jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        title = description_url = None
        description = ""

        title_tag = item.find('h3', class_='entry-title')
        if title_tag:
            title = title_tag.get_text().strip()
            url_tag = title_tag.find('a')
            if url_tag:
                description_url = url_tag.get('href')
                if description_url:
                    description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            for container in soup.find_all('section', class_='av_textblock_section'):
                if container.find('h2', class_='headline'):
                    continue
                inner_div = container.find('div', class_='avia_textblock')
                if inner_div:
                    for child in inner_div.children:
                        if isinstance(child, Tag):
                            Scraper.clean_attrs(child)
                            if child.get_text().strip() != "":
                                description += str(child)

        return description

    @staticmethod
    def get_location(title):
        """
        it receive the title since the city appears there
        :param title:
        :return: location and title in case it has a Finnish city, this city is removed from the title so the title is updated
        """
        location = None
        locator = CityLocator()

        cities = locator.get_finnish_cities(title)
        for city in cities:
            title = title.split(city.name)[0].strip()
            if title[-1] == ",":
                title = title[:-1]

        if cities:
            location = ", ".join(c.name for c in cities)

        return location, title


class KampCollection(Scraper):

    def extract_info(self, html):
        log_support.log_extract_info(self.client_name)
        jobs = []
        soup = BeautifulSoup(html, 'lxml')

        container = soup.find('div', class_='text-default-format')
        if container:
            for item in container.find_all('a'):
                title, description_url, description = self.get_mandatory_fields(item)
                if self.is_valid_job(title, description_url, description):
                    location = "Helsinki"  # all jobs are located in Helsinki area
                    end_date = self.get_end_date(item)

                    job = ScrapedJob(title, description, location, self.client_name, None, None, end_date, None, description_url)
                    jobs.append(job)

        return jobs

    def get_mandatory_fields(self, item):
        description = ""

        title = item.get_text().split("|")[0].strip()
        description_url = item.get('href')
        if description_url:
            description = self.get_description(description_url)

        return title, description_url, description

    @staticmethod
    def get_description(url):
        description = ""

        job_details_html = request_support.simple_get(url)
        if job_details_html:
            soup = BeautifulSoup(job_details_html, 'lxml')
            container = soup.find('div', class_='text-default-format')
            if container:
                for child in container.children:
                    if isinstance(child, Tag):
                        Scraper.clean_attrs(child)
                        if child.get_text().strip() != "":
                            description += str(child)

        return description

    def get_end_date(self, item):
        pattern = r"[0-9]{1,2}\.[0-9]{1,2}\.[0-9]{4}"

        full_title = item.get_text()
        end_date = self.get_end_date_by_regex(pattern, full_title)

        if not end_date:
            log_support.set_invalid_dates(self.client_name, full_title)

        return end_date
