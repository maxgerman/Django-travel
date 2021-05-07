from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    context = {'name': 'Maksym'}
    return render(request, 'home.html', context)
