from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'main/index.html')


def about(request):
	return HttpResponse("<h4>Страница про нас</h4>")


def help(request):
	return HttpResponse("<h4>Страница помощи</h4>")
