from django.shortcuts import render

from .models import Referral, Conclusion

def index(request):
    return render(request, 'documents/index.html')

def referrals(requets):
    return render(requets, 'documents/referrals.html', {
        'referrals': Referral.objects.all()
    })

def consclusions(request):
    return render(request, 'documents/conclusions.html', {
        'conclusions': Conclusion.objects.all()
    })
