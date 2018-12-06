from django.db import models
from django.utils import timezone


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

    class Meta:
        db_table = "Jobs"
