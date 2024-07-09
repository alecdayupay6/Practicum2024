# Generated by Django 5.0.6 on 2024-07-08 07:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualpatient', '0007_patient_language'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='description',
        ),
        migrations.AddField(
            model_name='patient',
            name='background',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='family_history',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='lifestyle',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='medical_history',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='recent_interactions',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]