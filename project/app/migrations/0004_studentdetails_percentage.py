# Generated by Django 5.0.6 on 2024-06-04 12:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_studentdetails_subject1_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='percentage',
            field=models.FloatField(default=0, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(90.9)]),
        ),
    ]
