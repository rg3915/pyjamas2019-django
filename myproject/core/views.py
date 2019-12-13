from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('<h1 style="font-family: sans-serif">Pyjamas Conf 2019</h1>')


def index(request):
    return render(request, 'index.html')
