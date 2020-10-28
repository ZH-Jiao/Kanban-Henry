from django.urls import path
from . import views

urlpatterns = [
    path('get-all-applicants', views.get_all_applicants),
    path('add-applicant', views.add_applicant),
    path('add-rate', views.add_rate),
    path('add-comment', views.add_comment),
    path('update-applicant-status', views.update_applicant_status),
]
