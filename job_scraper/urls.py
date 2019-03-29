from django.urls import path, re_path
from . import views

app_name = 'job_scraper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('search', views.IndexView.as_view(), name='index'),
    path('job/<int:pk>/<slug:slug>', views.DetailView.as_view(), name='detail'),
]
