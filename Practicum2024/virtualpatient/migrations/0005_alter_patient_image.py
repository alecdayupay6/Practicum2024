# Generated by Django 5.0.6 on 2024-06-30 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualpatient', '0004_patient_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='image',
            field=models.CharField(blank=True, default='images/gpt.jpg/', max_length=50, null=True),
        ),
    ]
