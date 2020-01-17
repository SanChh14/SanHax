from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.gamesblog, name='games'),
    path('<str:gamesblog_title>/', views.game_detail, name='game_detail'),

]
