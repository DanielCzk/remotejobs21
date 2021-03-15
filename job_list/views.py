from django.shortcuts import render
from job_form.models import Offer
from .filters import JobFilter
from django.views.generic import ListView


class AllJobs(ListView):

	model = Offer
	template_name = 'index.html'
	success_url = '/'
	paginate_by = 10
	

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['filter'] = JobFilter(self.request.GET, queryset = self.get_queryset())
		return context

	def get_queryset(self):
		queryset = super().get_queryset()
		return JobFilter(self.request.GET, queryset=queryset).qs



