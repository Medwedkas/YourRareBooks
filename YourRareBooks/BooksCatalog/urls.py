from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.CatalogView.as_view()),
    path('bookSales', bookSales),
    path('weSeek', weSeek),
    path('about', about),



]
