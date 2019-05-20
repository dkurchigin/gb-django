from django.urls import path

import mainapp.views as mainapp

app_name = 'mainapp'

urlpatterns = [
   path('', mainapp.products, name='index'),
   path('detail/<int:pk>/', mainapp.detail, name='detail'),
   path('<int:pk>/', mainapp.products, name='category'),
]