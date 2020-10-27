from django.urls import path
from . import views

urlpatterns = [
    path('get-all-applicants', views.get_all_applicants),
    path('add-applicant', views.add_applicant)
]