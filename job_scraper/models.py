from django.db import models
from django.utils import timezone
import re
import time


class Region(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Regions"


class City(models.Model):
    name = models.CharField(max_length=64, unique=True)
    swedish_name = models.CharField(max_length=64, blank=True, default=None, null=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Cities"
        verbose_name_plural = "cities"


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    logo100 = models.ImageField(blank=True, null=True)
    description = models.CharField(max_length=5000, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Companies"
        verbose_name_plural = "companies"

    @property
    def get_name_slug(self):
        """
        Returns the company title well formatted for URL, changing white spaces by "-" and removing all special characters
        :return: Company title splited by "-" and lower
        """
        title_no_spaces = "-".join(self.name.split())
        return re.sub(r'[^A-Za-z-0-9]', '', title_no_spaces).lower()


class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_new = models.BooleanField(default=True)
    description = models.CharField(max_length=5000)
    salary = models.FloatField(blank=True, default=None, null=True)
    pub_date = models.DateField(blank=True, null=True, default='')
    end_date = models.DateField(blank=True, null=True, default='')
    job_type = models.CharField(max_length=500, blank=True, null=True)
    is_highlighted = models.BooleanField(default=False)
    job_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)  # UTC time by default
    updated_at = models.DateTimeField(default=timezone.now)  # UTC time by default
    tags = models.ManyToManyField('Tag', through='JobTagMap')
    cities = models.ManyToManyField('City', through='JobCityMap')

    def __str__(self):
        return self.title

    @property
    def get_title_slug(self):
        """
        Returns the job title well formatted for URL, changing white spaces by "-" and removing all special characters
        :return: Job title splited by "-" and lower
        """
        title_no_spaces = "-".join(self.title.split())
        return re.sub(r'[^A-Za-z-0-9]', '', title_no_spaces).lower()

    @property
    def get_initial_description(self):
        """
        Gets the description removing all HTML tags.
        :return: String
        """
        reg_exp = re.compile('<.*?>')
        description = re.sub(reg_exp, ' ', self.description)

        return description

    @property
    def is_recent_job(self):
        return self.is_new and int(self.created_at.timestamp()) > self.get_epoch_by_day(-7)

    @property
    def is_published_again(self):
        return not self.is_new and int(self.updated_at.timestamp()) > self.get_epoch_by_day(-7)

    @property
    def posted_date_details(self):
        month = 30
        difference = (timezone.now() - self.updated_at).days

        if difference < 1:
            return "Today"
        elif difference < 2:
            return "Yesterday"
        elif difference < 7:
            return " %d" % difference + " days ago"
        elif difference < 13:
            return "a week ago"
        elif difference < 20:
            return "2 weeks ago"
        elif difference < 26:
            return "3 weeks ago"
        elif difference < month * 2:
            return "a month ago"
        elif difference < month * 3:
            return "2 months ago"
        elif difference < month * 4:
            return "3 months ago"
        elif difference < month * 5:
            return "4 months ago"
        elif difference < month * 6:
            return "5 months ago"
        elif difference < month * 7:
            return "6 months ago"
        elif difference < month * 8:
            return "7 months ago"
        elif difference < month * 9:
            return "8 months ago"
        elif difference < month * 10:
            return "9 months ago"
        elif difference < month * 11:
            return "10 months ago"
        elif difference < month * 12:
            return "11 months ago"
        else:
            return "more than one year ago"

    @property
    def posted_date(self):
        date_str = self.posted_date_details
        if date_str != "Today" and date_str != "Yesterday":
            date_str = "Posted " + date_str

        return date_str

    @staticmethod
    def get_epoch_by_day(days):
        current_epoch = int(time.time())
        offset = 60 * 60 * 24 * days
        return current_epoch + offset

    def __get_keywords(self, size):
        max_size = size
        tags_list = []
        job_tags_map = self.tags.through.objects.filter(job_id=self).order_by('-num_times')
        for i, item in enumerate(job_tags_map):
            if i == max_size:
                break
            else:
                i += 1
                tags_list.append(item.tag.name)

        return tags_list

    @property
    def get_keywords(self):
        return self.__get_keywords(5)

    @property
    def get_keywords_mobile(self):
        return self.__get_keywords(4)

    def update_details_counter(self):
        try:
            click_counter_instance = ClickCounter.objects.get(job=self)
        except ClickCounter.DoesNotExist:
            click_counter_instance = ClickCounter(job=self)

        click_counter_instance.details += 1
        click_counter_instance.updated_at = timezone.now()
        click_counter_instance.save()

    def update_apply_counter(self):
        try:
            click_counter_instance = ClickCounter.objects.get(job=self)
        except ClickCounter.DoesNotExist:
            click_counter_instance = ClickCounter(job=self)

        click_counter_instance.apply += 1
        click_counter_instance.updated_at = timezone.now()
        click_counter_instance.save()

    @property
    def get_meta_keywords(self):
        meta_keywords = self.title

        cities = self.cities.through.objects.filter(job_id=self)
        if cities:
            for _, item in enumerate(cities):
                meta_keywords += ", Jobs in {0}, Avoimet työpaikat {1}, ".format(item.city.name, item.city.name)
        else:
            meta_keywords += ", Jobs in Finland, Avoimet työpaikat, "

        return meta_keywords

    @property
    def get_locations(self):
        cities = City.objects.filter(job=self)

        cities_str = ", ".join(c.name for c in cities)
        if cities_str == "":
            cities_str = None

        return cities_str

    class Meta:
        db_table = "Jobs"


class JobCityMap(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

    class Meta:
        db_table = "JobCityMap"

    def __str__(self):
        return "'" + self.job.title + "' located in " + self.city.name


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Tags"


class JobTagMap(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    num_times = models.PositiveSmallIntegerField(default=0)

    class Meta:
        db_table = "JobsTagsMap"

    def __str__(self):
        return "'" + self.job.title + "' linked to tag: '" + self.tag.name + "' %d" % self.num_times + " time(s)"


class ClickCounter(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    details = models.PositiveSmallIntegerField(default=0)
    apply = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "ClickCounter"

    def __str__(self):
        return "'" + self.job.title + "'\tDetail job clicks: %d" % self.details + "\tApply job clicks: %d" % self.apply


class UserSearches(models.Model):
    what_entry = models.CharField(max_length=500, blank=True, null=True)
    where_entry = models.CharField(max_length=500, blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "UserSearches"
        verbose_name_plural = "UserSearches"

    @staticmethod
    def add_entry(what_entry=None, where_entry=None):
        entry = UserSearches()
        entry.what_entry = what_entry
        entry.where_entry = where_entry
        entry.save()
