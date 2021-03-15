from django.urls import path
from .views import AllJobs
from . import views

urlpatterns = [
   path(r'', AllJobs.as_view()),
]