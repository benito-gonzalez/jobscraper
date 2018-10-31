from django.urls import path
from . import views

app_name = 'job_scraper'
urlpatterns = [
    path('jobs/', views.IndexView.as_view(), name='index'),
    path('jobs/<int:pk>/', views.DetailView.as_view(), name='detail')
]

