from django.db import models

# Create your models here.
# Name of the task, Details of the task, Number of people to work on it, Date created.
class Task(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=1000)
    no_people = models.IntegerField()
    # date_created = models.DateField()
    day_of_week = models.CharField(max_length=10)
