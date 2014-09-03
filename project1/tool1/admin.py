from django.contrib import admin
from models import Medications, Patient


class Medications_Admin(admin.ModelAdmin):
    list_display = ('med_id', 'patient', 'start_date')


class Patient_Admin(admin.ModelAdmin):
    list_display = ('patient_id', 'member_id', 'first_name', 'last_name')


admin.site.register(Medications, Medications_Admin)
admin.site.register(Patient, Patient_Admin)

