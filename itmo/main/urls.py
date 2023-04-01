from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('index', views.about),
	path('about', views.about),
	path('help', views.help)
]
