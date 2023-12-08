from django.db import models

# Create your models here.
class student(models.Model):
    username=models.CharField(max_length=45)
    email=models.CharField(max_length=50)
    password=models.IntegerField()
    confirm=models.IntegerField()
    # email=models.CharField(max_length=50)
    # salary=models.IntegerField()
    # place=models.CharField(max_length=55)