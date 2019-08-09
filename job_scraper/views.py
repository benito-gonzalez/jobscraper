from rest_framework import generics
from django.views import generic
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.views.generic.edit import FormView
from django.conf import settings
from django.contrib import messages
from re import escape
from re import search
from urllib.parse import unquote
from datetime import datetime

from operator import and_
from operator import or_
import functools
import requests
from collections import OrderedDict
from itertools import chain

from .forms import ContactForm
from job_scraper.models import Job
from job_scraper.models import Company
from job_scraper.models import UserSearches
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

        messages.success(self.request, 'Message has been sent successfully! Thank you!')
        return self.render_to_response(self.get_context_data(form=form))

    def form_invalid(self, form):
        return super().form_invalid(form)


class IndexView(generic.ListView):
    template_name = 'index.html'
    paginate_by = 20
    context_object_name = 'jobs_list'
    company = None

    def get_context_data(self, **kwargs):
        ctx = super(IndexView, self).get_context_data(**kwargs)
        ctx['company'] = self.company
        return ctx

    @staticmethod
    def filter_by_location(location_query):
        # Gets those active jobs for a specific location when the end_date is either greater than today or end_date is None
        today = datetime.today()
        return Q(is_active=True, end_date__gte=today, cities__name__iexact=location_query) | Q(is_active=True, end_date=None, cities__name__iexact=location_query) |\
               Q(is_active=True, end_date__gte=today, cities__region__name__iexact=location_query) | Q(is_active=True, end_date=None, cities__region__name__iexact=location_query)


    @staticmethod
    def filter_by_active():
        # Gets those active jobs when the end_date is either greater than today or end_date is None
        today = datetime.today()
        return Q(is_active=True, end_date__gte=today) | Q(is_active=True, end_date=None)

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

        if self.request.get_full_path().endswith("-jobs"):
            keyword_query_raw = self.request.get_full_path().split("-jobs")[0]
            # remove initial "/"
            keyword_query = unquote(keyword_query_raw[1:])
            self.request.GET._mutable = True
            self.request.GET["keyword"] = keyword_query

        if keyword_query:
            keyword_words = keyword_query.split(" ")
            try:
                self.company = Company.objects.get(name__iexact=keyword_query)
            except (Company.DoesNotExist, Company.MultipleObjectsReturned):
                pass

        if keyword_query and location_query:
            # If the search has special characters, the word boundary '\b' is not valid, we need to remove it in order to return the proper jobs.
            if search("[^a-zA-Z0-9 ]+", keyword_query):
                # It returns all jobs which title contains all words typed by the user. In any order
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q)) | Q(company__name__iregex=r"\b" + escape(q)) for q in keyword_words]) &
                                           self.filter_by_location(location_query)).order_by('-updated_at')

            else:
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q) + r"\b") | Q(company__name__iregex=r"\b" + escape(q) + r"\b") for q in keyword_words]) &
                                           self.filter_by_location(location_query)).order_by('-updated_at')

            if self.company:
                result_list = list(list1)
            else:
                # Gets jobs which full query matches with a keyword
                list2 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=keyword_query)]) & self.filter_by_location(location_query)).order_by('-jobtagmap__num_times')

                # Gets jobs which any word from user query matches with a keyword
                list3 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=q) for q in keyword_words]) & self.filter_by_location(location_query)).order_by('-jobtagmap__num_times')

                result_list = list(chain(list1, list2, list3))

            UserSearches.add_entry(what_entry=keyword_query, where_entry=location_query)
            return list(OrderedDict.fromkeys(result_list))

        if keyword_query:
            # If the search has special characters, the word boundary '\b' is not valid, we need to remove it in order to return the proper jobs.
            if search("[^a-zA-Z0-9 ]+", keyword_query):
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=escape(q)) | Q(company__name__iregex=escape(q)) for q in keyword_words]) &
                                           self.filter_by_active()).order_by('-updated_at')
            else:
                list1 = Job.objects.filter(functools.reduce(and_, [Q(title__iregex=r"\b" + escape(q) + r"\b") | Q(company__name__iregex=r"\b" + escape(q) + r"\b") for q in keyword_words]) &
                                           self.filter_by_active()).order_by('-updated_at')
            if self.company:
                result_list = list(list1)
            else:
                # Gets jobs which full query matches with a keyword
                # select j.* from Jobs j inner join JobsTagsMap jt on j.id == jt.job_id inner join Tags t on jt.tag_id == t.id  where t.name like "keyword_query"
                list2 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=keyword_query)]) & self.filter_by_active()).order_by('-jobtagmap__num_times')

                # Gets jobs which any word from user query matches with a keyword
                list3 = Job.objects.filter(functools.reduce(or_, [Q(tags__name__iexact=q) for q in keyword_words]) & self.filter_by_active()).order_by('-jobtagmap__num_times')

                result_list = list(chain(list1, list2, list3))

            UserSearches.add_entry(what_entry=keyword_query)
            return list(OrderedDict.fromkeys(result_list))

        if location_query:
            UserSearches.add_entry(where_entry=location_query)
            return Job.objects.filter(self.filter_by_location(location_query)).order_by('-updated_at')
        else:
            return Job.objects.filter(self.filter_by_active()).order_by('-updated_at')


class DetailView(generic.DetailView):
    model = Job
    template_name = 'detail.html'

    def get_object(self, **kwargs):
        job = get_object_or_404(Job, pk=self.kwargs['pk'])
        if job.get_title_slug != self.kwargs.get('slug'):
            raise Http404

        if not job.is_active:
            raise Http404

        job.update_details_counter()
        return job


class ApplyView(generic.RedirectView):
    permanent = False
    query_string = False
    pattern_name = 'apply'

    def get_redirect_url(self, *args, **kwargs):
        job = get_object_or_404(Job, pk=kwargs['pk'])
        job.update_apply_counter()
        return job.job_url


class CompanyIndexView(generic.ListView):
    template_name = 'companies.html'
    context_object_name = 'companies_list'

    def get_queryset(self):
        return Company.objects.all()


class JobListApiView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetailApiView(generics.RetrieveAPIView):
    queryset = Job.objects.all()
    serializer_class = JobDetailSerializer
