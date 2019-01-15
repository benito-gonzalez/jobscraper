from rest_framework import generics
from django.views import generic
from django.http import Http404
from django.shortcuts import redirect
from django.db.models import Q
from operator import and_
import functools

from job_scraper.models import Job
from job_scraper.serializers import JobSerializer, JobDetailSerializer


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'jobs_list'

    def get_queryset(self):
        search_query = self.request.GET.get('search', None)
        location_query = self.request.GET.get('location', None)
        search_words = []

        if search_query:
            search_words = search_query.split(" ")

        if search_query and location_query:
            return Job.objects.filter(functools.reduce(and_, [Q(title__icontains=q) | Q(company__name=q) for q in search_words])
                                      & Q(is_active=True) & Q(location__icontains=location_query)).order_by('-updated_at')
        if search_query:
            return Job.objects.filter(functools.reduce(and_, [Q(title__icontains=q) | Q(company__name=q) for q in search_words]) & Q(is_active=True)).order_by('-updated_at')
        if location_query:
            return Job.objects.filter(is_active=True, location__icontains=location_query).order_by('-updated_at')
        else:
            return Job.objects.filter(is_active=True).order_by('-updated_at')


class DetailView(generic.DetailView):
    model = Job
    template_name = 'detail.html'

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        except Http404:
            return redirect('job_scraper:index')


class JobListApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApiView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
