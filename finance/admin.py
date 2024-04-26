from django.contrib import admin

from .models import Clientes, Productos, Clientes_Productos, Tipos_Transacciones, Transacciones

class ClientesFields(admin.ModelAdmin):
    list_display = [ 'nombre','apellido', 'email', 'telefono' ]

class ProductosFields(admin.ModelAdmin):
    list_display = [ 'nombre','abreviacion', 'descripcion' ]

class Clientes_ProductosFields(admin.ModelAdmin):
    list_display = [ 'id_cliente','id_producto', 'numero_cuenta' ]

class Tipos_TransaccionesFields(admin.ModelAdmin):
    list_display = [ 'nombre','abreviacion', 'descripcion' ]

class TransaccionesFields(admin.ModelAdmin):
    list_display = [ 'id_cliente_producto','id_tipo_transaccion', 'monto' ]
    



# Register your models here.
admin.site.register(Clientes)
admin.site.register(Productos)
admin.site.register(Clientes_Productos)
admin.site.register(Tipos_Transacciones)
admin.site.register(Transacciones)
