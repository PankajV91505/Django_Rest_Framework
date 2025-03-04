from django.db import models

# Create your models here.


#Creating Company model

class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    ceo = models.CharField(max_length=100)
    about = models.TextField()
    type = models.CharField(max_length=100 , choices = (('MNC', 'MNC'), ('Startup', 'Startup') , ('Service', 'Service') , ('Product', 'Product')))
    founded = models.DateField()
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)
    
    def self(self):
        return self.name + ' ' + self.location
    
    
#Creating Employee model

class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=10)
    address = models.TextField()
    about = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100 , choices = (('Developer', 'Developer'), ('Tester', 'Tester') , ('Manager', 'Manager') , ('HR', 'HR')))
    added_date = models.DateField(auto_now_add=True)
    updated_date = models.DateField(auto_now=True)
    active = models.BooleanField(default=True)