from django.db import models

# Create your models here.
class User(models.Model):
    name= models.CharField(max_length=100, default='')
    age= models.IntegerField(default=0)
    gender= models.CharField(max_length=50, default='Male')