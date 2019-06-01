from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import HttpResponseRedirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView
from django.views.generic.list import ListView
from mainapp.models import ProductCategory, Product
from authapp.models import ShopUser
from django.shortcuts import render


class IsSuperUserVies(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_superuser


class ProductListView(IsSuperUserVies, ListView):
    model = Product
    template_name = 'adminapp/products.html'

    def get_queryset(self):
        qs = super(ProductListView, self).get_queryset()
        category_pk = self.kwargs.get('pk')
        if category_pk:
            return qs.filter(category__pk=category_pk)
        else:
            return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['title'] = "Админка. Продукты"
        context['category_menu'] = ProductCategory.objects.all()
        return context


class ProductDetailView(IsSuperUserVies, DetailView):
    model = Product
    template_name = 'adminapp/product.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['title'] = "Админка. {}".format(context['product'])
        context['category_menu'] = ProductCategory.objects.all()
        return context


class ProductUpdateView(IsSuperUserVies, UpdateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = ('name', 'short_desc')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Редактирование продукта'
        context['category_menu'] = ProductCategory.objects.all()
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:product_read', kwargs={'pk': self.kwargs.get('pk')})


class ProductCreateView(IsSuperUserVies, CreateView):
    model = Product
    template_name = 'adminapp/product_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin_custom:products')


class ProductDeleteView(IsSuperUserVies, DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    def get_success_url(self):
        return reverse_lazy('admin_custom:products')


# ----------------CATEGORIES----------------
class CategoryListView(IsSuperUserVies, ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Категории'
        return context


class CategoryUpdateView(IsSuperUserVies, UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = ('name', 'description')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CategoryUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Редактирование категории'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:categories')


class CategoryCreateView(IsSuperUserVies, CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin_custom:categories')


class CategoryDeleteView(IsSuperUserVies, DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'

    def get_success_url(self):
        return reverse_lazy('admin_custom:categories')


# ----------------USERS----------------
class UserListView(IsSuperUserVies, ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Пользователи'
        return context


class UserUpdateView(IsSuperUserVies, UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'
    fields = 'first_name', 'last_name', 'email',

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserUpdateView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Редактирование пользователя'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:users')


class UserCreateView(IsSuperUserVies, CreateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('admin_custom:users')


class UserDeleteView(IsSuperUserVies, DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(UserDeleteView, self).get_context_data(**kwargs)
        context['title'] = 'Админка. Удаление пользователя'
        return context

    def get_success_url(self):
        return reverse_lazy('admin_custom:users')

    # def delete(self, request, *args, **kwargs):
    #     deleted_user = super(UserDeleteView, self).delete(**kwargs)
    #     print(deleted_user)
    def delete(self, request, *args, **kwargs):
        deleted_user = self.get_object()
        deleted_user.is_active = False
        deleted_user.save()
        return HttpResponseRedirect(self.get_success_url())
