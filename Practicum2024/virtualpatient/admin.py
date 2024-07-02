from django.contrib import admin
from .models import Patient, Diagnosed

class PatientAdmin(admin.ModelAdmin):
    # Fields to be displayed in the list view
    list_display = ('first_name', 'last_name', 'age', 'sex', 'illness_to_be_diagnosed')
    
    # Fields to filter the list view
    list_filter = ('sex', 'created_by')
    
    # Fields to search in the list view
    search_fields = ('first_name', 'last_name', 'description', 'symptoms', 'notes')
    
    # Default ordering of the list view
    ordering = ('first_name', 'last_name')

# Register the Patient model with the custom PatientAdmin configuration
admin.site.register(Patient, PatientAdmin)

class DiagnosedAdmin(admin.ModelAdmin):
    list_display = ('user', 'patient', 'conversation')

admin.site.register(Diagnosed, DiagnosedAdmin)
