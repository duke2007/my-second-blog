from django.urls import path
from . import views

app_name = 'blog2'

urlpatterns = [
	path('', views.post_list, name='post_list'),
]