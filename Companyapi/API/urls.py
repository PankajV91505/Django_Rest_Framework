from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet, EmployeeViewSet
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register(r'companies', CompanyViewSet)
routers.register(r'employees', EmployeeViewSet)

urlpatterns = [
    path('', include(routers.urls)),
    
]

