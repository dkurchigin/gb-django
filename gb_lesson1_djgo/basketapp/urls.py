from django.urls import path
import basketapp.views as basketapp

app_name = 'basketapp'

urlpatterns = [
   path('add/product/<int:pk>/', basketapp.add, name='add'),
   path('delete/product/<int:pk>/', basketapp.delete, name='delete'),
]