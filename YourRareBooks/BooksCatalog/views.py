from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from .models import *


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def bookSales(request):
    return render(request, 'BooksCatalog/bookSales.html')


def weSeek(request):
    return render(request, 'BooksCatalog/weSeek.html')


def about(request):
    return render(request, 'BooksCatalog/about.html')


def basket(request):
    return render(request, 'BooksCatalog/basket.html')


class CatalogView(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, "BooksCatalog/index.html", {"book_list": books})
