from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Report(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    weight = models.IntegerField()
    height = models.IntegerField()
    bmi = models.IntegerField(default=0)
    gender = models.CharField(max_length=10)
    exercise = models.CharField(max_length=10)
    diabetic = models.CharField(max_length=10)
    remark = models.CharField(max_length=50, default='', blank=True)
    mealplan = models.CharField(max_length=50, default='', blank=True)

    def __str__(self):
        return self.name
