"""webapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.views.static import serve
from django.conf.urls import url, include
from django.views.generic.base import TemplateView
from django.shortcuts import render
from job_scraper import views

urlpatterns = [
    url(r'', include('webmaster_verification.urls')),
    path('admin/', admin.site.urls),
    path('about/cookiepolicy', TemplateView.as_view(template_name='cookiepolicy.html')),
    path('about/about-us', TemplateView.as_view(template_name='about.html')),
    path('about/contact-us', views.ContactFormView.as_view()),
    path('donations', TemplateView.as_view(template_name='payment_process.html')),
    re_path(r'jobs-in-\w+', views.IndexView.as_view(), name='index'),
    re_path(r'tags-in-\w+', views.TagIndexView.as_view(), name='tags.html'),
    re_path(r'jobs-at-\w+', views.IndexView.as_view(), name='index'),
    re_path(r'(.*?)-jobs', views.IndexView.as_view(), name='index'),
    path('', include('job_scraper.urls')),
    # path('api/jobs/', views.JobListApiView.as_view()),
    # path('api/jobs/<int:pk>/', views.JobDetailApiView.as_view()),
]


def handler404(request, exception, template_name="404.html"):
    response = render(request, template_name)
    response.status_code = 404
    return response


if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', serve, {
            'document_root': settings.MEDIA_ROOT,
        }),
    ]
