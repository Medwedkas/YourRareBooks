from decimal import Decimal
from django.conf import settings
from BooksCatalog.models import Books


class Cart(object):
    def __init__(self, request):
        """Инициализация корзины"""
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)

        # Если корзина пустая
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}

        self.cart = cart

    def __iter__(self):
        """Перебор товаров из корзины, в итоге получаем товары из базы данных"""

        product_ids = self.cart.keys()
        # Получаем товары и добавляем в корзину
        products = Books.objects.filter(id__in=product_ids)
        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        """Считаем сколько товаров в корзине"""
        return sum(item['quanity'] for item in self.cart.value())

    def add(self, product, quantity=1, update_quantity=False):
        """Добавление товара в корзину или обновление количества"""
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0, 'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()

    def save(self):
        # сохраняем товар
        self.session.modified = True

    def remove(self, product):
        """Удаляем товар"""
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()

    def get_total_price(self):
        """Получаем общую стоимость"""
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())

    def clear(self):
        """Очищаем корзину сессии"""
        del self.session[settings.CART_SESSION_ID]
        self.save()
