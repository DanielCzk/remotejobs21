from django.urls import path
from .views import CompanyCreate
from .views import CompanyUpdate
from .views import CompanyList
from .views import CompanyDelete
from .views import CompanyDetail
from .views import ListofJobs
from django.contrib.auth.decorators import login_required

urlpatterns = [ 

	path('list/<int:pk>', ListofJobs.as_view(), name='company-list-offers'),
	path('create/', login_required(CompanyCreate.as_view()), name='company-create'),
	path('update/<int:pk>', login_required(CompanyUpdate.as_view()), name='company-update'),
	path('data/', login_required(CompanyList.as_view()), name='company-data'),
	path('delete/<int:pk>', CompanyDelete.as_view(), name='company-delete'),
	path('<int:pk>', CompanyDetail.as_view(), name='company-detail'),
]