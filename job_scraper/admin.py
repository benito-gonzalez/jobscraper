from django.contrib import admin

from .models import Job
from .models import Company

admin.site.register(Job)
admin.site.register(Company)
