from django.contrib import admin
from .models import Books


@admin.register(Books)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'phouse', 'release_date', 'available', 'price']
    list_editable = ['available', 'price']
# Register your models here.
