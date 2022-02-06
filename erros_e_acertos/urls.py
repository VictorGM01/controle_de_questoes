from django.urls import path
from .views import index, AdicionarRegistro

urlpatterns =[
    path('', index, name='index'),
    path('add_registro/', AdicionarRegistro.as_view(), name='add-registro')
]