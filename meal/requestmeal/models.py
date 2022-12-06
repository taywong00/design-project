from django.db import models
from django.contrib.auth.models import User

from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    SID = models.CharField(max_length= 50)
    MSallotment = models.IntegerField(default = 0)
    DDallotment = models.FloatField(default = 0)
    access = models.IntegerField(default=1)
    
    def __str__(self):
        return f'{self.user.email} Student'

    def changeMS(IDnum, self):
        MS = Student.objects.get(id = IDnum)
        MS.MSallotment = MS.MSallotment + 1
        MS.save()


class NYUEATS(models.Model):
    semester = models.CharField(max_length= 50)
    MSP = models.IntegerField()
    MSU = models.IntegerField()
    DDP = models.FloatField()
    DDU = models.FloatField()

class AvaiableStuff(models.Model):
    MS = models.IntegerField()
    DD = models.FloatField()

class History(models.Model):
    Data = models.OneToOneField(NYUEATS, on_delete=models.CASCADE)

@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(user=instance)

class RequestAmount(models.Model):
    MS = models.IntegerField()
    DD = models.FloatField()

class DonateAmount(models.Model):
    MS = models.IntegerField()
    DD = models.FloatField()
    netid = models.CharField(max_length= 50)