from django.urls import include, path
from rest_framework import routers
from . import views

urlpatterns = [
    path('', views.home, name='cms-home'),
    path('about/', views.about, name='cms-about'),
    path('create_client/', views.create_client, name='cms-create-client'),
    path('create_clinet_test/', views.create_client_test, name='cms-create-client-test')
]
