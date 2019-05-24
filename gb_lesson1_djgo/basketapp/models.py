from django.db import models
from mainapp.models import Product
from authapp.models import ShopUser


class BasketSlot(models.Model):
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

    product = models.ForeignKey(Product, verbose_name='продукт', on_delete=models.CASCADE)
    user = models.ForeignKey(ShopUser, verbose_name='пользователь', on_delete=models.CASCADE, related_name='basket')
    quantity = models.PositiveIntegerField(verbose_name='количество', default=1)
    created = models.DateTimeField(verbose_name='создано', auto_now_add=True)

    def __str__(self):
        return "{} - {}".format(self.product, self.user)


    @property
    def _get_product_cost(self):
        return self.product.price * self.quantity

    product_cost = property(_get_product_cost)
