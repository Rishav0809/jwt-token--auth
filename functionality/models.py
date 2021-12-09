from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class Details(models.Model):
    user=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default="Enter your Email",blank=True)
    address=models.TextField(default="Enter your Address",blank=True)
