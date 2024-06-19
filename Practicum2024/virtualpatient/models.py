from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    age = models.IntegerField(null=True, blank=True)
    sex = models.CharField(max_length=1, choices=[
        ('M', 'Male'),
        ('F', 'Female'),
    ], null=True)
    height = models.FloatField(help_text="Height in cm", null=True)
    weight = models.FloatField(help_text="Weight in kg", null=True)
    description = models.TextField(blank=True, null=True)
    symptoms = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)
    illness_to_be_diagnosed = models.CharField(max_length=255, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_age(self):
        return self.age

    def get_sex(self):
        return self.sex

    def get_height(self):
        return self.height

    def get_weight(self):
        return self.weight

    def get_description(self):
        return self.description

    def get_symptoms(self):
        return self.symptoms

    def get_notes(self):
        return self.notes

    def get_illness_to_be_diagnosed(self):
        return self.illness_to_be_diagnosed
