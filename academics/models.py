from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    age = models.IntegerField()
    created_at = models.DateTimeField(default= datetime.datetime.now())
    updated_at = models.DateTimeField(default= datetime.datetime.now())
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)
    

    