from django.contrib import admin

from .models import BranchOfMedicine, Diagnosis, Service

admin.site.register(BranchOfMedicine)
admin.site.register(Diagnosis)
admin.site.register(Service)
