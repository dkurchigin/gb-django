from django.shortcuts import render, get_object_or_404
from .models import Product, ProductCategory

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'products:index', 'name': 'Продукты'},
    {'href': 'contacts', 'name': 'Контакты'},
    {'href': 'basket:read', 'name': 'Корзина'},
]


def main(request):
    context = {"links_menu": links_menu, 'empty_array': [], 'array': [number for number in range(1, 6)]}
    return render(request, 'mainapp/index.html', context)


def detail(request, pk=None):
    category_menu = ProductCategory.objects.all()

    detail_product = get_object_or_404(Product, pk=pk)
    context = {
        "links_menu": links_menu,
        "category_menu": category_menu,
        "detail_product": detail_product,
    }
    return render(request, 'mainapp/detail.html', context)


def products(request, pk=None):
    category_menu = ProductCategory.objects.all()

    if pk or pk == 0:
        filter_products = Product.objects.all()
        if pk:
            filter_products = Product.objects.filter(category=pk)
        context = {
            "links_menu": links_menu,
            "category_menu": category_menu,
            "products": filter_products
        }
        return render(request, 'mainapp/products.html', context)
    else:
        hot_product = Product.objects.filter(is_hot=True).first()
        context = {
            "links_menu": links_menu,
            "category_menu": category_menu,
            "hot_product": hot_product
        }
        return render(request, 'mainapp/hot_product.html', context)


def contacts(request):
    context = {"links_menu": links_menu}
    return render(request, 'mainapp/contacts.html', context)
