from django.contrib import admin
from .models import Patient, Diagnosed

class PatientAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'sex', 'illness_to_be_diagnosed')
    list_filter = ('sex', 'created_by')
    search_fields = ('first_name', 'last_name', 'description', 'symptoms', 'notes')
    ordering = ('first_name', 'last_name')

class DiagnosedAdmin(admin.ModelAdmin):
    list_display = ('user', 'patient', 'conversation')
    list_filter = ('user', 'patient')

admin.site.register(Patient, PatientAdmin)
admin.site.register(Diagnosed, DiagnosedAdmin)
