from django.contrib import admin
from .models import ProductCategory, Product

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'is_hot')
    search_fields = 'name', 'category__name',
    list_filter = 'is_hot',
