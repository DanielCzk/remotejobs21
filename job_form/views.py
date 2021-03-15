from django.shortcuts import render, redirect, get_object_or_404
from .forms import OfferForm
from .models import Offer
from job_company.models import Company
#from django.http import HttpResponse
#from .filters import FoodFilter
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView, CreateView, UpdateView 

#from django.core.paginator import Paginator

# Create your views here.


# Job list

class JobList(ListView):

	model = Offer
	template_name = 'job_form/job_list.html'
	context_object_name = 'job_company_offers'

	def get_queryset(self):
		return self.model.objects.filter(user=self.request.user)

	

# Job form create 

class JobCreate(CreateView):

	model = Offer
	template_name = 'job_form/job_form.html'
	fields = ['title', 'job_desc','min_salary', 'max_salary', 'requirements', 'salary_type', 'contract_type', 'experience_type', 'area_type' ]
	success_url = '/job/list'
	

	def form_valid(self, form, **kwargs):

		instance = form.save(commit=False)
		form.instance.user_id = self.request.user.id
		try:
			form.instance.added_by = Company.objects.get(user_id=self.request.user.id)
		except Company.DoesNotExist:
			form.instance.added_by = None

		return super().form_valid(form)

#update offers 
class JobUpdate(UpdateView):

	model = Offer
	success_url = '/job/list'
	fields = ['title', 'job_desc','min_salary', 'max_salary', 'requirements', 'salary_type', 'contract_type', 'experience_type', 'area_type' ]
	template_name = 'job_form/job_form.html'

	def form_valid(self, form, **kwargs):

		instance = form.save(commit=False)
		#form.instance.user_id = self.request.user.id
		try:
			form.instance.added_by = Company.objects.get(user_id=self.request.user.id)
		except Company.DoesNotExist:
			form.instance.added_by = None

		return super().form_valid(form)

# Deleting chosen created job offer
  
class JobDelete(DeleteView): 

	model = Offer
	success_url ="/job/list"


# Showing details of some job offer

class JobDetail(DetailView): 
	
	model = Offer
	template_name = 'job_form/job_detail.html'
	context_object_name = 'job_list_detail'

	

# Showing a list of all offer created by Company

class JobCompanyList(ListView):

	model = Offer
	template_name = 'job_form/job_list_user.html'
	context_object_name = 'job_offers'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['job_offers'] = Offer.objects.filter(user=self.kwargs['pk'])
		return context




