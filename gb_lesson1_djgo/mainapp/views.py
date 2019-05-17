from django.shortcuts import render
from .models import Product, ProductCategory
from basketapp.models import BasketSlot

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'products:index', 'name': 'Продукты'},
    {'href': 'contacts', 'name': 'Контакты'},
]


def main(request):
    context = {"links_menu": links_menu, 'empty_array': [], 'array': [number for number in range(1, 6)]}
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    basket = []
    if request.user.is_authenticated:
        basket = BasketSlot.objects.filter(user=request.user)
    total_quantity = sum(list(map(lambda basket_slot: basket_slot.quantity, basket)))
    total_price = sum(list(map(lambda basket_slot: basket_slot.product.price * basket_slot.quantity, basket)))

    if pk:
        filter_products = Product.objects.filter(category=pk)
    else:
        filter_products = Product.objects.all()

    category_menu = ProductCategory.objects.all()
    context = {"links_menu": links_menu, "category_menu": category_menu, "products": filter_products, "basket_quantity": total_quantity, "total_price": total_price}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {"links_menu": links_menu}
    return render(request, 'mainapp/contacts.html', context)
