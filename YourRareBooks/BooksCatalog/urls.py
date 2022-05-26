from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('', views.CatalogView.as_view()),
    path('bookSales', bookSales),
    path('basket', basket),
    path('weSeek', views.WishView.as_view()),
    path('weSeekForm', weSeek),
    path('about', about),
]
