from django.shortcuts import render

# Create your views here.
links_menu = [
    {'href': 'main', 'name': 'Главная'},
    {'href': 'products', 'name': 'Продукты'},
    {'href': 'contacts', 'name': 'Контакты'},
]


def main(request):
    context = {"links_menu": links_menu, 'user': {'name': 'дима'}, 'empty_array': [], 'array': [number for number in range(1, 6)]}
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {"links_menu": links_menu}
    return render(request, 'mainapp/products.html', context)


def contacts(request):
    context = {"links_menu": links_menu}
    return render(request, 'mainapp/contacts.html', context)
