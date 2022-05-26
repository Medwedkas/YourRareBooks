from .models import Orders
from django.forms import ModelForm, TextInput, EmailInput, DateTimeInput


class OrdersForm(ModelForm):
    class Meta:
        model = Orders
        fields = ['first_name', 'second_name', 'email', 'phone_number', 'book_name', 'book_author',
                  'phouse', 'release_date']

        widgets = {
            'first_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Имя'
            }),
            'second_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Фамилия'
            }),
            'email': EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Элктронная почта'
            }),
            'phone_number': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Номер телефона'
            }),
            'book_name': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название книги'
            }),
            'book_author': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Автор книги'
            }),
            'phouse': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Издевательство'
            }),
            'release_date': DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата выпуска'
            })
        }