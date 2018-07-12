from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from . import views

app_name = 'blog2'

urlpatterns = [
	path('', views.post_list, name='post_list'),
	path('<int:pk>/', views.post_detail, name='post_detail'),
]