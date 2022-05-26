from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import OrdersForm
from .forms import WishForm
from .forms import ByersForm


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def bookSales(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'BooksCatalog/about.html')
        else:
            error = 'Форма была неверно заполнена'

    form = OrdersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'BooksCatalog/bookSales.html', data)


def weSeek(request):
    error = ''
    if request.method == 'POST':
        form = WishForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'BooksCatalog/about.html')
        else:
            error = 'Форма была неверно заполнена'

    form = WishForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'BooksCatalog/weSeekForm.html', data)


def basket(request):
    error = ''
    if request.method == 'POST':
        form = ByersForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'BooksCatalog/about.html')
        else:
            error = 'Форма была неверно заполнена'

    form = ByersForm()
    data = {
        'form': form,
        'error': error
    }

    return render(request, 'BooksCatalog/basket.html', data)


def about(request):
    return render(request, 'BooksCatalog/about.html')


class CatalogView(View):
    def get(self, request):
        books = Books.objects.all()
        return render(request, "BooksCatalog/index.html", {"book_list": books})


class WishView(View):
    def get(self, request):
        wish = WishList.objects.all()
        return render(request, "BooksCatalog/weSeek.html", {"wish_list": wish})
