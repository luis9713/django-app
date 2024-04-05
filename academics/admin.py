from django.contrib import admin

from .models import User, identification_type, country, department, cities, person, student

# Register your models here.
class UserFields(admin.ModelAdmin):
    list_display = [ 'email','password', 'status', 'created_at' ]
    
    
    
    
admin.site.register(User, UserFields)
admin.site.register(identification_type)
admin.site.register(country)
admin.site.register(department)
admin.site.register(cities)
admin.site.register(person)
admin.site.register(student)
