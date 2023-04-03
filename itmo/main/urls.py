from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='home'),
	path('about', views.about, name='about'),
	path('base', views.base_home, name='base'),
	path('cont', views.cont, name='cont')
]
