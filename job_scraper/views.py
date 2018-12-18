from rest_framework import generics
from django.views import generic

from job_scraper.models import Job
from job_scraper.serializers import JobSerializer, JobDetailSerializer


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'latest_job_list'

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        location_query = self.request.GET.get('location', None)

        if search_query and location_query:
            return Job.objects.filter(is_active=True, title__icontains=search_query, location__icontains=location_query).order_by('-updated_at')
        if search_query:
            return Job.objects.filter(is_active=True, title__icontains=search_query).order_by('-updated_at')
        if location_query:
            return Job.objects.filter(is_active=True, location__icontains=location_query).order_by('-updated_at')
        else:
            return Job.objects.filter(is_active=True).order_by('-updated_at')


class DetailView(generic.DetailView):
    model = Job
    template_name = 'detail.html'


class JobListApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApiView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
