from django.db import models
from django.utils import timezone
import re


class Company(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Companies"


class Job(models.Model):
    title = models.CharField(max_length=500)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    description = models.CharField(max_length=5000)
    location = models.CharField(max_length=100, blank=True, null=True)
    salary = models.FloatField(blank=True, default=None, null=True)
    pub_date = models.DateField(blank=True, null=True, default='')
    end_date = models.DateField(blank=True, null=True, default='')
    job_type = models.CharField(max_length=500, blank=True, null=True)
    is_highlighted = models.BooleanField(default=False)
    job_url = models.URLField(max_length=500)
    created_at = models.DateTimeField(default=timezone.now)  # UTC time by default

    def __str__(self):
        return self.title

    @property
    def get_initial_description(self):
        """
        Gets the first N characters from a description removing all HTML tags and including only the text within the <p></p> tags.
        :return: String
        """
        raw_description = self.description
        description_split = self.description.split('<p>', 1)

        if len(description_split) == 2:
            raw_description = description_split[1]
            raw_description = raw_description.replace('</p>', '\n')

        reg_exp = re.compile('<.*?>')
        description = re.sub(reg_exp, ' ', raw_description)

        return description

    class Meta:
        db_table = "Jobs"
