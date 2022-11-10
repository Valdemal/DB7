from django.urls import path

from .views import index, diagnoses, services, branches_of_medicine

app_name = 'reference_info'

urlpatterns = [
    path('', index, name='index'),
    path('diagnoses/', diagnoses, name='diagnoses'),
    path('services/', services, name='services'),
    path('branches_of_medicine/', branches_of_medicine, name="branches_of_medicine")
]
