from django.db import models
import datetime

# Create your models here.


class dateTimeModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    
    class Meta:
        abstract = True
    
class User(dateTimeModel):
    id= models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    email = models.EmailField(max_length=50, unique=True, blank=False, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return str(self.id) + " " + self.email

class identification_type(dateTimeModel):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    
    
    def __str__(self):
        return str(self.id) + " "+ self.name

class country(dateTimeModel):   
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    
    
    def __str__(self):
        return str(self.id) + " " + self.name
    
class department(dateTimeModel):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    id_country = models.ForeignKey(country, on_delete=models.CASCADE, blank=False, null=False)
    
    
    def __str__(self):
        return str(self.id) + " " + self.name
    
class cities(dateTimeModel):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    name = models.CharField(max_length=50, blank=False, null=False)
    abrebiation = models.CharField(max_length=5, blank=False, null=False)
    description = models.CharField(max_length=100, blank=False, null=False)
    id_department = models.ForeignKey(department, on_delete=models.CASCADE, blank=False, null=False)
    
    
    def __str__(self):
        return str(self.id) + " " + self.name

class person (dateTimeModel):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    id_user= models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)
    id_ident_type = models.ForeignKey(identification_type, on_delete=models.CASCADE, blank=False, null=False)
    id_ident_number = models.IntegerField( unique=True, blank=False, null=False)
    id_ident_exp_city = models.ForeignKey(cities, on_delete=models.CASCADE, blank=False, null=False)
    address = models.CharField(max_length= 50, blank=False, null=False)
    phone = models.CharField(max_length=50, blank=False, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, blank=False, null=False)     
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.id) + " " + self.first_name + " " + self.last_name
    
class student(dateTimeModel):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    code= models.CharField(max_length=50, blank=False, null=False)
    id_person = models.ForeignKey(person, on_delete=models.CASCADE, blank=False, null=False)
    status = models.BooleanField(default=True)
    
    
    def __str__(self):
        return str(self.id) + " " + self.code
    

    