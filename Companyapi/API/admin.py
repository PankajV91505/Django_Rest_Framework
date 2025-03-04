from django.contrib import admin
from api.models import Company, Employee

# Register your models here.

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name' , 'location' , 'ceo' , 'type' )
    search_fields = ('name' , 'location' , 'ceo' , 'type' )
    search_filter = ('name' , 'location' , 'ceo' , 'type' )

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name' , 'email' , 'phone' , 'company' , 'position')
    list_filter = ('company' , 'position')
admin.site.register(Company , CompanyAdmin)
admin.site.register(Employee , EmployeeAdmin)