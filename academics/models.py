from django.db import models
import datetime

# Create your models here.
class User(models.Model):
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
class person (models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_ident_type = models.CharField(max_length=5, default='CC', blank=False, null=False)
    id_ident_number = models.IntegerField( unique=True, blank=False, null=False)
    id_ident_exp_city = models.IntegerField(blank=False, null=False)
    address = models.CharField(max_length= 50, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False) 
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    status = models.BooleanField(default=True)

    