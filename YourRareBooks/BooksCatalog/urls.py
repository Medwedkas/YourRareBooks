from django.urls import path

from .views import *

urlpatterns = [
    path('', booksList),
    path('bookSales', bookSales),
    path('weSeek', weSeek),
    path('about', about),
    path('basket', basket),


]
