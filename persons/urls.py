from django.urls import path

from .views import index, patients, doctors, doctors_statistics

app_name = 'persons'

urlpatterns = [
    path('', index, name='index'),
    path('patients/', patients, name='patients'),
    path('doctors/', doctors, name='doctors'),
    path('doctors/statistics/', doctors_statistics, name='doctors_statistics'),
]
