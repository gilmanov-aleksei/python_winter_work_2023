from django.shortcuts import render
from django.http import HttpResponse


def index(request):
	return render(request, 'main/index.htm')


def about(request):
	return render(request, 'main/about.htm')


def help(request):
	return HttpResponse("<h4>Страница помощи</h4>")
