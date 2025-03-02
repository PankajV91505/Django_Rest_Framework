from django.contrib import admin
from django.urls import path,include
from API.views import CompanyViewSet
from rest_framework.routers import routers


routers = routers.DefaultRouter()
routers.register(r'companies', CompanyViewSet)


urlpatterns = [
    path('', include(routers.urls)),
    
]
