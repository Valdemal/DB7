from django.urls import path

from .views import index, referrals, consclusions

app_name = 'documents'

urlpatterns = [
    path('', index, name='index'),
    path('referrals/', referrals, name='referrals'),
    path('conclusions/', consclusions, name='conclusions')
]
