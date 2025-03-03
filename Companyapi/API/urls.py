from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet
from rest_framework import routers


routers = routers.DefaultRouter()
routers.register(r'companies', CompanyViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    
]
