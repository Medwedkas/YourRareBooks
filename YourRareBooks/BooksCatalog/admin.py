from django.contrib import admin
from .models import Books
from .models import Orders
from .models import WishList
from .models import Wish_request


@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'phouse', 'release_date', 'available', 'price']
    list_editable = ['available', 'price']


@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email', 'phone_number', 'book_name', 'state']
    list_editable = ['state']


@admin.register(WishList)
class WishListAdmin(admin.ModelAdmin):
    list_display = ['book_name', 'book_author', 'phouse', 'release_date']


@admin.register(Wish_request)
class WishRequestAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email', 'phone_number', 'book_name', 'state']
    list_editable = ['state']
