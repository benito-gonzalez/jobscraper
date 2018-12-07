from rest_framework import generics
from django.views import generic

from job_scraper.models import Job
from job_scraper.serializers import JobSerializer, JobDetailSerializer


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        return Job.objects.filter(is_active=True).order_by('-created_at')


class DetailView(generic.DetailView):
    model = Job
    template_name = 'detail.html'


class JobListApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApiView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
