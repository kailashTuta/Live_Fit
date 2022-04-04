from django.db import models

# Create your models here.


class Workout(models.Model):
    exercise = models.CharField(max_length=100)
    equipment = models.CharField(max_length=100)
    exercise_type = models.CharField(max_length=100)
    major_muscle = models.CharField(max_length=100)
    minor_muscle = models.CharField(
        max_length=100, default=None, null=True, blank=True)
    example = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    notes = models.CharField(
        max_length=200, default=None, null=True, blank=True)
    modification = models.CharField(
        max_length=200, default=None, null=True, blank=True)

    def __str__(self):
        return self.exercise
