# Generated by Django 5.0.6 on 2024-06-04 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_remove_studentdetails_rollno_studentdetails_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='Subject1',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='Subject2',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='Subject3',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='studentdetails',
            name='total',
            field=models.IntegerField(null=True),
        ),
    ]
