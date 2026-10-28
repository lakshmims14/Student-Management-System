from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Course(models.Model):
    img=models.ImageField((""), upload_to='gallery')
    level=models.CharField(max_length=50)
    name=models.CharField( max_length=50)
    desc=models.TextField()
    year=models.CharField(max_length=50)
    eligibility=models.CharField( max_length=50)

    def __str__(self):
        return self.name
    
class Student(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    img=models.ImageField((""), upload_to='students/')
    name=models.CharField(max_length=50)
    dob=models.CharField(max_length=50)
    branch=models.CharField(max_length=50)
    ph=models.CharField(max_length=50)
    address=models.CharField(max_length=50)

    def __str__(self):
        return self.name
    