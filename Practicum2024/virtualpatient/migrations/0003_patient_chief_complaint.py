# Generated by Django 5.0.6 on 2024-06-25 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualpatient', '0002_patient_provocation_patient_quality_patient_region_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='chief_complaint',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
