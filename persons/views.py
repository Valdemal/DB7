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
