from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def booksList(request):
    return render(request, 'BooksCatalog/index.html')
