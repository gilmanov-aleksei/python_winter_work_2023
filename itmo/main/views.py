from django.shortcuts import render


def index(request):
	data = {
		'title': 'Главная'
	}
	return render(request, 'main/index.html', data)


def about(request):
	return render(request, 'main/about.html', {'title': 'О нас'})


def base_home(request):
	return render(request, 'base/base_home.html', {'title': 'База'})


def cont(request):
	return render(request, 'main/cont.html', {'title': 'Контанты'})
