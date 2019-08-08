import os
import geotext
from job_scraper.utils import db_support
from re import search
from re import escape

current_path = os.path.abspath(os.path.dirname(__file__))
FILENAME = os.path.join(current_path, "cities.txt")


class CityLocator:

    def __init__(self):
        self.finnish_cities = db_support.get_cities()

    def has_finnish_cities(self, text):
        result = False

        if text:
            for city in self.finnish_cities:
                if city.swedish_name:
                    if search(r"\b" + escape(city.name.lower()) + "|" + escape(city.swedish_name.lower()) + r"\b", text.lower()):
                        result = True
                        break
                else:
                    if search(r"\b" + escape(city.name.lower()) + r"\b", text.lower()):
                        result = True
                        break
        return result

    def is_foreign_job_location(self, text):
        """
        Job location is foreign when is not null and does not have any Finnish city (or Finland)
        :param text: Job location
        :return: True/False
        """
        return text and not self.has_finnish_cities(text)

    @staticmethod
    def is_foreign_job_title(text):
        """
        Job title is foreign when it has cities and none of them are in Finland
        :param text: Job title
        :return: True/False
        """
        # There are some cities around the world which could provoke skipping Finnish jobs. These must be added to valid_cities array
        valid_cities = ["Mobile"]
        is_finnish = False
        cities = geotext.GeoText(text).cities

        for city in cities:
            if "FI" in geotext.GeoText(city).country_mentions:
                is_finnish = True

        if set(cities).issubset(valid_cities):
            is_finnish = True

        return len(cities) > 0 and not is_finnish

    def get_finnish_cities(self, text):
        cities = []
        for city in self.finnish_cities:
            if city.swedish_name:
                if search(r"\b" + escape(city.name.lower()) + "|" + escape(city.swedish_name.lower()) + r"\b", text.lower()):
                    cities.append(city)
            else:
                if search(r"\b" + escape(city.name.lower()) + r"\b", text.lower()):
                    cities.append(city)

        # If it finds a city, we can remove "Finland"
        if len(cities) > 1:
            finland_item = next((c for c in cities if c.name == "Finland"), None)
            if finland_item:
                cities.remove(finland_item)

        return cities
