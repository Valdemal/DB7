from django.shortcuts import render

from .models import Diagnosis, Service, BranchOfMedicine


def index(request):
    return render(request, 'reference_info/index.html')


def diagnoses(request):
    return render(request, 'reference_info/diagnoses.html', context={
        'diagnoses': Diagnosis.objects.order_by('branch')
    })


def services(request):
    return render(request, 'reference_info/services.html', context={
        'services': Service.objects.order_by('branch')
    })


def branches_of_medicine(request):
    return render(request, 'reference_info/brances_of_medicine.html', context={
        'branches_of_medicine': BranchOfMedicine.objects.all()
    })
