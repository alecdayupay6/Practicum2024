from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.PositiveIntegerField(null=True)
    sex = models.CharField(null=True, max_length=6, choices=[
        ('Male', 'Male'),
        ('Female', 'Female'),
    ])
    height = models.FloatField(help_text="Height in cm", null=True)
    weight = models.FloatField(help_text="Weight in kg", null=True)
    language = models.CharField(null=True, max_length=7, choices=[
        ('English', 'English'),
        ('Tagalog', 'Tagalog'),
        ('Taglish', 'Taglish'),
    ])
    chief_complaint = models.CharField(max_length=50, null=True)
    provocation = models.CharField(max_length=50, null=True)
    quality = models.CharField(max_length=50, null=True)
    region = models.CharField(max_length=50, null=True)
    severity = models.CharField(max_length=50, null=True)
    timing = models.CharField(max_length=50, null=True)
    background = models.CharField(max_length=200, blank=True, null=True)
    family_history = models.CharField(max_length=200, blank=True, null=True)
    lifestyle = models.CharField(max_length=200, blank=True, null=True)
    recent_interactions = models.CharField(max_length=200, blank=True, null=True)
    medical_history = models.CharField(max_length=200, blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    illness_to_be_diagnosed = models.CharField(max_length=255, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(default='images/gpt.jpg/', max_length=50, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Diagnosed(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    conversation = models.TextField(blank=True, null=True)
