from django.contrib import admin
from .models import Books
from .models import Orders


@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'phouse', 'release_date', 'available', 'price']
    list_editable = ['available', 'price']


# Register your models here.

@admin.register(Orders)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'second_name', 'email', 'phone_number', 'book_name']
# Register your models here.
