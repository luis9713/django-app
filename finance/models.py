from django.db import models
from django.contrib.auth.hashers import make_password
import datetime

# Create your models here.

class Clientes(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    telefono = models.CharField(max_length=50)
    password = models.CharField(max_length=250)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
   
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(Clientes, self).save(*args, **kwargs)
    
    def __str__(self,):
        return self.nombre + " " + self.apellido + " " + self.email 

class Productos(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    
    def __str__(self):
        return self.nombre + " " + self.abreviacion

class Clientes_Productos(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    id_producto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    numero_cuenta = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return str(self.id) + " " + self.id_cliente.nombre + " " + self.id_producto.nombre + " " + self.numero_cuenta

class Tipos_Transacciones(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    nombre = models.CharField(max_length=50)
    abreviacion = models.CharField(max_length=5)
    descripcion = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return self.nombre + " " + self.abreviacion

class Transacciones(models.Model):
    id = models.AutoField(primary_key=True, unique=True, blank=False, null=False)
    id_cliente_producto = models.ForeignKey(Clientes_Productos, on_delete=models.CASCADE)
    id_tipo_transaccion = models.ForeignKey(Tipos_Transacciones, on_delete=models.CASCADE)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null = False, blank = False)
    updated_at = models.DateTimeField(auto_now=True, null = False, blank = False)
    deleted_at = models.DateTimeField(null=True, blank=True)
    
    
    def __str__(self):
        return str(self.id) + " " + self.id_cliente_producto.id_cliente.nombre + " " + self.id_cliente_producto.id_producto.nombre 