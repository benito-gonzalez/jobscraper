from django.urls import path, re_path
from . import views
from django.views.generic.base import RedirectView


app_name = 'job_scraper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.IndexView.as_view(), name='index'),
    path('companies', views.CompanyIndexView.as_view(template_name='companies.html')),
    path('locations', views.LocationIndexView.as_view(template_name='locations.html')),
    path('tags', views.TagIndexView.as_view(template_name='tags.html')),
    path('job/apply-to-<int:pk>/<slug:slug>', views.ApplyView.as_view(), name='apply'),
    path('job/<int:pk>/<slug:slug>', views.DetailView.as_view(), name='detail'),
]
