from django.urls import path
from django.views.generic.base import RedirectView
from django.conf.urls import url
from . import views

app_name = 'job_scraper'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    url(r'^.*$', RedirectView.as_view(url='/', permanent=False), name='index')
]
