from django.db import models

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    age = models.IntegerField()

    