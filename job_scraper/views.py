from rest_framework import generics
from django.views import generic
from django.http import Http404
from django.shortcuts import redirect
from django.db.models import Q
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib import messages
from re import escape
from urllib.parse import unquote

from operator import and_
from operator import or_
import functools
import requests
from collections import OrderedDict
from itertools import chain

from .forms import ContactForm
from job_scraper.models import Job
from job_scraper.serializers import JobSerializer, JobDetailSerializer


class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # reCAPTCHA validation
        recaptcha_response = self.request.POST.get('g-recaptcha-response')
        data = {
            'secret': settings.GOOGLE_RECAPTCHA_SECRET_KEY,
            'response': recaptcha_response
        }
        r = requests.post('https://www.google.com/recaptcha/api/siteverify', data=data)
        result = r.json()
        if result['success']:
            form.send_email()
        else:
            form.add_error(None, "Invalid reCAPTCHA. Please try again.")
            return super().form_invalid(form)

        messages.success(self.request, 'Form has been sent successfully! Thank you!')
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return super().form_invalid(form)


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'jobs_list'

    def get_queryset(self):
        keyword_query = self.request.GET.get('keyword', None)
        location_query = self.request.GET.get('location', None)
        keyword_words = []

        if self.request.get_full_path().startswith("/jobs-in-"):
            location_query = self.request.get_full_path().split("/jobs-in-")[1]
            self.request.GET._mutable = True
            self.request.GET["location"] = location_query

        if self.request.get_full_path().startswith("/jobs-at-"):
            keyword_query_raw = self.request.get_full_path().split("/jobs-at-")[1]
            keyword_query = unquote(keyword_query_raw)
            self.request.GET._mutable = True
            self.request.GET["keyword"] = keyword_query

        if self.request.get_full_path().endswith("-developer"):
            keyword_query_raw = self.request.get_full_path().split("-developer")[0]
            # remove initial "/"
            keyword_query = unquote(keyword_query_raw[1:])
            self.request.GET._mutable = True
            self.request.GET["keyword"] = keyword_query

        if keyword_query:
            keyword_words = keyword_query.split(" ")

        if keyword_query and location_query:
            if "++" in keyword_query:
                # If the search is like "C++", the word boundary '\b' is not valid, we need to remove it in order to return the proper jobs.
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q)) | Q(company__name__iregex=r"\b" + escape(q)) for q in keyword_words])
                                           & Q(is_active=True) & Q(location__icontains=location_query)).order_by('-updated_at')
            else:
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q) + r"\b") | Q(company__name__iregex=r"\b" + escape(q) + r"\b") for q in keyword_words])
                                           & Q(is_active=True) & Q(location__icontains=location_query)).order_by('-updated_at')
            list2 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=q) for q in keyword_words]) & Q(is_active=True) &
                                       Q(location__icontains=location_query)).order_by('-jobtagmap__num_times')
            result_list = list(chain(list1, list2))
            return list(OrderedDict.fromkeys(result_list))

        if keyword_query:
            if "++" in keyword_query:
                # If the search is like "C++", the word boundary '\b' is not valid, we need to remove it in order to return the proper jobs.
                list1 = Job.objects.filter(
                    functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q)) | Q(company__name__iregex=r"\b" + escape(q)) for q in keyword_words]) & Q(is_active=True)).order_by('-updated_at')
            else:
                list1 = Job.objects.filter(
                    functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q) + r"\b") | Q(company__name__iregex=r"\b" + escape(q) + r"\b") for q in keyword_words]) & Q(is_active=True)).order_by(
                    '-updated_at')

            # select j.* from Jobs j inner join JobsTagsMap jt on j.id == jt.job_id inner join Tags t on jt.tag_id == t.id  where t.name like "keyword_query"
            list2 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=q) for q in keyword_words]) & Q(is_active=True)).order_by('-jobtagmap__num_times')
            result_list = list(chain(list1, list2))
            return list(OrderedDict.fromkeys(result_list))

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
            if self.object.get_title_slug != kwargs.get('slug'):
                raise Http404

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
