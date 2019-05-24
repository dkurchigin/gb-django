from django import template

register = template.Library()


@register.filter
def basket_total_quantity(user):
    if user.is_anonymous:
        return 0
    else:
        items = user.basket.all()
        # items = Basket.objects.filter(user=user)
        total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, items)))
        return total_quantity


@register.filter
def basket_total_cost(user):
    if user.is_anonymous:
        return 0
    else:
        items = user.basket.all()
        # items = Basket.objects.filter(user=user)
        total_cost = sum(list(map(lambda basket_slot: basket_slot.product.price * basket_slot.quantity, items)))
        return total_cost
