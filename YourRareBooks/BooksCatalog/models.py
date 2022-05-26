from django.db import models


class Books(models.Model):
    name = models.CharField('Название', max_length=100)
    phouse = models.CharField('Издательство', max_length=100)
    book_author = models.CharField('Автор книги', max_length=100)
    release_date = models.DateField('Дата выпуска')
    photo = models.ImageField('Фото товара', blank=True)
    available = models.BooleanField('В налии', default=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField('Описание')

    class Meta:
        ordering = ('name',)
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.name


class Orders(models.Model):
    first_name = models.CharField('Имя', max_length=100)
    second_name = models.CharField('Фамилия', max_length=100)
    email = models.EmailField('Электронная почта', max_length=100)
    phone_number = models.CharField('Номер телефона', max_length=100)
    book_name = models.CharField('Название книги', max_length=100)
    book_author = models.CharField('Автор книги', max_length=100)
    phouse = models.CharField('Издательство', max_length=100)
    release_date = models.DateField('Дата выпуска')

    class Meta:
        ordering = ('first_name',)
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'

    def __str__(self):
        return self.first_name
