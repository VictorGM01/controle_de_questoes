from django.urls import path
from .views import index, adicionar_registro, detalhar_lista, editar_lista, atualizar_lista

urlpatterns =[
    path('', index, name='index'),
    path('add_registro/', adicionar_registro, name='add-registro'),
    path('detalhes/<int:id_lista>', detalhar_lista, name='detalhes-listas'),
    path('editar/<int:id_lista>', editar_lista, name='editar-lista'),
    path('atualizar_lista', atualizar_lista, name='atualizar-lista')
]
