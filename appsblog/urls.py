from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.appsblog, name='apps'),
    path('<str:appsblog_title>/', views.app_detail, name='app_detail'),
]
