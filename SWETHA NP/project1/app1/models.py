from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=45)
    email=models.CharField(max_length=50)
    password=models.IntegerField()


class stud(models.Model):
    name=models.CharField(max_length=25)
    rollno=models.IntegerField()
    place=models.CharField(max_length=35)
