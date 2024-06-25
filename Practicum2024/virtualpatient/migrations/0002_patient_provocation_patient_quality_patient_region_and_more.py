# Generated by Django 5.0.6 on 2024-06-25 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualpatient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='provocation',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='quality',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='region',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='severity',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='timing',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True),
        ),
    ]
