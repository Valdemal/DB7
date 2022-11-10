from django.contrib import admin
from django.contrib.staticfiles.views import serve
from django.shortcuts import render
from django.urls import path, include
from django.views.decorators.cache import never_cache

from hostel import settings


def index(request):
    return render(request, 'index.html')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('reference_info/', include('reference_info.urls')),
    path('persons/', include('persons.urls')),
    path('documents/', include('documents.urls'))
]

# отключение кеширования в отладочном режиме
if settings.DEBUG:
    urlpatterns.append(path('static/<path:path>', never_cache(serve)))
