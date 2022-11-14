from django.db.models import Count, F, Q
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


def diagnoses_cases(request):
    return render(
        request, 'reference_info/diagnosis_cases.html', {
            'diagnoses_cases': Diagnosis.objects
            .values('name', 'branch__name')
            # ХЗ как я это сделал, но сделал
            .annotate(count=Count('id', filter=Q(conclusion__diagnosis=F('id'))))
            .filter(count__gt=0).order_by('-count')
        })
