from django.shortcuts import render


def home_visit(request):
	return render(request, 'home/home.html')
