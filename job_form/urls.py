from django.urls import path
from job_form.views import JobList
from job_form.views import JobCreate
from job_form.views import JobDelete
from job_form.views import JobDetail
from job_form.views import JobCompanyList
from job_form.views import JobUpdate
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [

	#path('', views.job_form, name='job_insert'),
	#path('<int:id>/', views.job_form, name='job_update'),

	#path('list/', views.food_list, name='food_list'),
	path('list/<int:pk>', JobDetail.as_view(), name='job-detail'),
	path('list/user/<int:pk>', JobCompanyList.as_view(), name='job-list-user'),
	path('delete/<int:pk>', JobDelete.as_view(), name='job-delete'),
	path('update/<int:pk>', JobUpdate.as_view(), name='job-update'),
	path('create/', login_required(JobCreate.as_view()), name='job-create'),
	path('list/', login_required(JobList.as_view()), name='job-list'),
]