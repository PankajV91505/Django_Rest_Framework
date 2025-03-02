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
    
    
#Creating Employee model