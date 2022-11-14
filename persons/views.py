from django.db.models import Count, Q, F
from django.shortcuts import render

from .models import Patient, Doctor


def index(request):
    return render(request, 'persons/index.html')


def patients(request):
    return render(request, 'persons/patients.html', context={
        'patients': Patient.objects.all()
    })


def doctors(request):
    return render(request, 'persons/doctors.html', context={
        'doctors': Doctor.objects.all()
    })


def doctors_statistics(request):
    return render(
        request, 'persons/doctors_statistics.html', {
            'doctors': Doctor.objects
            .values('surname', 'name', 'specialization__name')
            .annotate(referrals_count=Count('id', filter=Q(referral__doctor=F('id'))))
            .order_by('-referrals_count', 'surname', 'name')
            .filter(referrals_count__gt=0)
        })
