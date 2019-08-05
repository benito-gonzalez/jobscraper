from django.contrib import admin

from .models import Job
from .models import Company
from .models import Tag
from .models import JobTagMap
from .models import ClickCounter
from .models import UserSearches


class TagAdmin(admin.ModelAdmin):
    search_fields = (['name'])
    list_display = ('name',)


class CompanyAdmin(admin.ModelAdmin):
    search_fields = (['name'])
    list_display = ('name', 'description')


class JobAdmin(admin.ModelAdmin):
    search_fields = ('title', 'location', 'company__name')
    list_display = ('title', 'company', 'end_date', 'is_active', 'is_new', 'created_at', 'updated_at')
    date_hierarchy = "created_at"
    ordering = ('-updated_at',)


class ClickCounterAdmin(admin.ModelAdmin):
    search_fields = ('job__title',)
    list_display = ('job', 'details', 'apply', 'created_at', 'updated_at')
    date_hierarchy = "created_at"
    ordering = ('-updated_at',)


class JobTagMapAdmin(admin.ModelAdmin):
    search_fields = ('job__title', 'tag__name')
    list_display = ('job', 'tag', 'num_times')
    ordering = ('-id',)


class UserSearchesAdmin(admin.ModelAdmin):
    list_display = ('what_entry', 'where_entry', 'created_at')
    ordering = ('-created_at',)
    date_hierarchy = "created_at"


admin.site.register(Tag, TagAdmin)
admin.site.register(Job, JobAdmin)
admin.site.register(ClickCounter, ClickCounterAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(JobTagMap, JobTagMapAdmin)
admin.site.register(UserSearches, UserSearchesAdmin)
