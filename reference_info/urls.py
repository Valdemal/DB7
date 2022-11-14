from django.urls import path

from .views import index, diagnoses, services, branches_of_medicine, diagnoses_cases

app_name = 'reference_info'

urlpatterns = [
    path('', index, name='index'),
    path('diagnoses/', diagnoses, name='diagnoses'),
    path('services/', services, name='services'),
    path('branches_of_medicine/', branches_of_medicine, name="branches_of_medicine"),
    path('diagnoses/cases/', diagnoses_cases, name="diagnoses_cases"),
]
