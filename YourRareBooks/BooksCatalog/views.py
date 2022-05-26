from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .models import *
from .forms import OrdersForm


def index(request):  # HttpRequest
    return HttpResponse("Страница приложения BooksCatalog")


def bookSales(request):
    error = ''
    if request.method == 'POST':
        form = OrdersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('BooksCatalog/index.html')
        else:
            error = 'Форма была неверной'

    form = OrdersForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'BooksCatalog/bookSales.html', data)


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
