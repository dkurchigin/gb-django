from django.contrib import admin
from .models import ShopUser
from basketapp.models import BasketSlot

admin.site.register(ShopUser)


class BasketInline(admin.TabularInline):
    model = BasketSlot
    fields = 'product', 'quantity'
    extra = 1


class UserWithBasket(ShopUser):
    class Meta:
        verbose_name = 'Пользователь с корзиной'
        verbose_name_plural = 'Пользователи с корзиной'
        proxy = True


@admin.register(UserWithBasket)
class UsersWithBasketAdmin(admin.ModelAdmin):
    list_display = 'username', 'get_basket_quantity', 'get_basket_cost',
    fields = 'username',
    readonly_fields = 'username',
    inlines = BasketInline,

    def get_queryset(self, request):
        gs = super(UsersWithBasketAdmin, self).get_queryset(request)
        return gs.filter(basket__quantity__gt=0).distinct()

    def get_basket_quantity(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))

    get_basket_quantity.short_description = 'Общее количество'

    def get_basket_cost(self, instance):
        basket = BasketSlot.objects.filter(user=instance)
        return sum(list(map(lambda basket_slot: basket_slot.product.price * basket_slot.quantity, basket)))

    get_basket_cost.short_description = 'Общая сумма'
