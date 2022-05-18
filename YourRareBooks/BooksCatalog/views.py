from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def booksList(request):
    return HttpResponse("<h1>Список книг в наличии</h1>")
