from django.db import models
from django.conf import settings
# Create your models here.

class Company(models.Model):

	logo = models.ImageField(default="default_logo.png")
	company_name = models.CharField(max_length=300, default="")
	country = models.CharField(max_length=200,default="")
	city = models.CharField(max_length=200, default="")

	employees_number = (
		('1-10', '1-10'),
		('11-50', '11-50'),
		('51-250','51-250'),
		('250+','250+'),
		)

	company_size = models.CharField(

		max_length=100, 
		choices=employees_number, 
		default='1-10',
		blank=True,
		null=True

		)


	user =  models.ForeignKey(settings.AUTH_USER_MODEL,default=1,on_delete=models.CASCADE, related_name='company_information')
	bio = models.TextField(max_length=1000, default="Company bio")

	def get_absolute_url(self): 
		return reverse("company-create", kwargs={'id': self.id})

	def get_absolute_url(self): 
		return reverse("company-update", kwargs={'id': self.id})

	def get_absolute_url(self): 
		return reverse("company-data", kwargs={'id': self.id})


	def get_absolute_url(self): 
		return reverse("company-detail", kwargs={'id': self.id})

	def get_absolute_url(self): 
		return reverse("company-list-offers", kwargs={'id': self.id})