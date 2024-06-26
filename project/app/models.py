from django.db import models
from django.core.validators import MaxValueValidator,MinValueValidator

# Create your models here.


class StudentDetails(models.Model):
    name=models.CharField(max_length=100)
    Subject1=models.IntegerField(null=True)
    Subject2=models.IntegerField(null=True)
    Subject3=models.IntegerField(null=True)
    total=models.IntegerField(null=True)
    percentage=models.FloatField(validators=[MinValueValidator(0.0),MaxValueValidator(90.9)],default=0)