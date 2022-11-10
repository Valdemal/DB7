from django.urls import path

from .views import index, patients, doctors

app_name = 'persons'

urlpatterns = [
    path('', index, name='index'),
    path('patients/', patients, name='patients'),
    path('doctors/', doctors, name='doctors'),
]
