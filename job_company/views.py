from django.shortcuts import render
from .models import Company
from job_form.models import Offer
from django.views.generic.edit import DeleteView, CreateView, UpdateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import redirect
from django.urls import reverse
# Create your views here.


class CompanyCreate(CreateView):

	model = Company
	template_name = 'job_company/job_company_form.html'
	fields = ['logo', 'company_name','country', 'city', 'company_size','bio']
	success_url = '/job/list'

	def is_limit_reached(self):
		return Company.objects.filter(user=self.request.user).count() >= 1

	def form_valid(self, form):

		instance = form.save(commit=False)
		form.instance.user_id = self.request.user.id
		if self.is_limit_reached():
			return redirect('/job/company/data/')
		else:
			return super().form_valid(form)

	

class CompanyUpdate(UpdateView):

	model = Company
	success_url = '/job/list'
	fields = ['logo', 'company_name','country', 'city', 'company_size','bio']
	template_name = 'job_company/job_company_form.html'



class CompanyList(ListView):

	model = Company
	template_name = 'job_company/job_company_list.html'
	context_object_name = 'job_company_data'
	#paginate_by = 1


	def get_queryset(self):
		return self.model.objects.filter(user=self.request.user)

class CompanyDelete(DeleteView): 

	model = Company
	success_url ="/job/company/data"


class CompanyDetail(DetailView): 
	
	model = Company
	template_name = 'job_company/job_company_detail.html'
	context_object_name = 'job_company_detail'


class ListofJobs(ListView):

	model = Offer
	template_name = 'job_company/job_company_offers.html'
	context_object_name = 'offers'

	def get_context_data(self, **kwargs):

		context = super().get_context_data(**kwargs)
		context['offers'] = Offer.objects.filter(user=self.kwargs['pk'])
		return context