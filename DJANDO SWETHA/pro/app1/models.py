from django.db import models

# Create your models here.
class student(models.Model):
    name=models.CharField(max_length=25)
    rollno=models.IntegerField()
    place=models.CharField(max_length=35)

    # def __str__(self):
    #      return self.rollno
