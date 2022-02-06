from django.urls import path
from .views import index, adicionar_registro

urlpatterns =[
    path('', index, name='index'),
    path('add_registro/', adicionar_registro.as_view(), name='add-registro')
]
