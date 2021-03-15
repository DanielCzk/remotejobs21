from django.db import models
from django.conf import settings
from django.urls import reverse
from job_company.models import Company

class Offer(models.Model):

	title = models.CharField(max_length=150)
	job_desc = models.CharField(max_length=3000)
	min_salary = models.IntegerField(blank=True, null=True)
	max_salary = models.IntegerField(blank=True, null=True)
	requirements = models.CharField(max_length=2000)
	user =  models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, default=1, related_name='company_offer')
	added_by = models.ForeignKey(Company,
        null=True, blank=True, on_delete=models.SET_NULL)
	
	salary_currency = (
		('USD', 'USD'),
		('EUR', 'EUR'),
		('PLN','PLN')
		)

	salary_type = models.CharField(

		max_length=100, 
		choices=salary_currency, 
		default='PLN',
		blank=True,
		null=True

		)

	contract_details = (
		('Full Time', 'Full Time'),
		('Contract', 'Contract')

		)

	contract_type = models.CharField(

		max_length=100, 
		choices=contract_details, 
		default='Full Time',
		

		)

	experience_level = (
		('Trainee', 'Trainee'),
		('Junior', 'Junior'),
		('Regular', 'Regular'),
		('Senior', 'Senior'),
		('Expert', 'Expert')
		)

	experience_type = models.CharField(

		max_length=100, 
		choices=experience_level, 
		default='Regular',
		

		)

	area_choose = (

		('IT','IT'),
		('Tax','Tax'),
		('Law','Law'), 
		('Accounting','Accounting'),
		('Design','Design'),
		('Video','Video'), 
		('Marketing','Marketing'),
		
		)


	area_type = models.CharField(

		max_length=100, 
		choices=area_choose, 
		default='IT'

		)



	def __str__(self):
		return self.name

	def get_absolute_url(self): 
		return reverse("job-list", kwargs={'pk': self.pk})

	def get_absolute_url(self): 
		return reverse("job-list-user", kwargs={'pk': self.pk})			

	def get_absolute_url(self): 
		return reverse("job-delete", kwargs={'id': self.id})	

	def get_absolute_url(self): 
		return reverse("job-create", kwargs={'id': self.id})

	def get_absolute_url(self): 
		return reverse("job-update", kwargs={'id': self.id})

	def get_absolute_url(self): 
		return reverse("job-detail", kwargs={'id': self.id})


