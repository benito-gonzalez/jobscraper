import os
import geotext


current_path = os.path.abspath(os.path.dirname(__file__))
FILENAME = os.path.join(current_path, "cities.txt")


class CityLocator:

    def __init__(self):
        cities = []
        with open(FILENAME) as f:
            for line in f:
                cities.append(line.strip())
        f.close()

        self.finnish_cities = cities

    def has_finnish_cities(self, text):
        result = False

        if text:
            for city in self.finnish_cities:
                if city in text:
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
        is_finnish = False
        cities = geotext.GeoText(text).cities

        for city in cities:
            if "FI" in geotext.GeoText(city).country_mentions:
                is_finnish = True

        return len(cities) > 0 and not is_finnish

    def get_finnish_cities(self, text):
        cities = []
        for city in self.finnish_cities:
            if city in text:
                cities.append(city)

        # If it finds a city, we can remove "Finland"
        if len(cities) > 1 and "Finland" in cities:
            cities.remove("Finland")

        return cities
