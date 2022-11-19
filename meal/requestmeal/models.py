from django.db import models

class Donee(models.Model):
    name = models.CharField(max_length=80)
    netid = models.CharField(max_length=80)
    mealnum = models.IntegerField()

