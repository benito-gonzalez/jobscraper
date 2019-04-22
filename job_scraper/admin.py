from django.contrib import admin

from .models import Job
from .models import Company
from .models import Tag
from .models import JobTagMap
from .models import ClickCounter


admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Tag)
admin.site.register(JobTagMap)
admin.site.register(ClickCounter)
