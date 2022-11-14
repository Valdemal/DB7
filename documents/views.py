from datetime import datetime

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


def service_report(request):
    return render(
        request, 'documents/service_report.html', {
            'referrals': Referral.objects
            .values('doctor__name', 'doctor__surname', 'patient__name', 'patient__surname',
                    'service__name', 'cabinet', 'appointment_time')
            .filter(result=Referral.Result.PROVIDED)
            .order_by('-appointment_time')
        }
    )


def hiled_diseases_statistics(request):
    def is_valid_date_string(date_string: str) -> bool:
        return date_string is not None and date_string != ''

    period_start = request.GET.get('period_start')
    if not is_valid_date_string(period_start):
        period_start = datetime.fromtimestamp(0).strftime('%Y-%m-%d')

    period_end = request.GET.get('period_end')
    if not is_valid_date_string(period_end):
        period_end = datetime.now().strftime('%Y-%m-%d')

    return render(
        request, 'documents/hiled_diseases_statistics.html', {
            'conclusions':
                Conclusion.objects
                .filter(registration_time__range=(period_start, period_end))
                .order_by('-registration_time'),

            'period_start': period_start,
            'period_end': period_end,
        }
    )
