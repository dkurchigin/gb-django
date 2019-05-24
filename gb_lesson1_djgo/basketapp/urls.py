from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
   path('', basketapp.basket, name='read'),
   path('add/product/<int:pk>/', basketapp.add, name='add'),
   path('delete/product/<int:pk>/', basketapp.delete, name='delete'),
   path('edit/<int:pk>/', basketapp.edit, name='basket_edit'),
]
