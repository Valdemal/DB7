from django.urls import path

from .views import index, referrals, consclusions, service_report, hiled_diseases_statistics

app_name = 'documents'

urlpatterns = [
    path('', index, name='index'),
    path('referrals/', referrals, name='referrals'),
    path('conclusions/', consclusions, name='conclusions'),
    path('service_report/', service_report, name='service_report'),
    path('hiled_diseases_statistics', hiled_diseases_statistics,
         name='hiled_diseases_statistics'),
]
