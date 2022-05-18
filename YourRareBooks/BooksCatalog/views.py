from django.http import HttpResponse
from django.shortcuts import render


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def booksList(request):
    return render(request, 'BooksCatalog/index.html')


def bookSales(request):
    return render(request, 'BooksCatalog/bookSales.html')


def weSeek(request):
    return render(request, 'BooksCatalog/weSeek.html')


def about(request):
    return render(request, 'BooksCatalog/about.html')


def basket(request):
    return render(request, 'BooksCatalog/basket.html')
