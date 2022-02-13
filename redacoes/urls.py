from django.urls import path
from . import views


urlpatterns = [
    path('adicionar/redacao/', views.adicionar, name='add-redacoes'),
    path('dashboard/', views.dashboard_redacoes, name='dashboard-redacoes'),
    path('detalhes/redacao/<int:id_redacao>', views.detalhar, name='detalhes-redacoes'),
    path('editar/redacao/<int:id_redacao>', views.editar, name='editar-redacao'),
    path('atualizar/redacao', views.atualizar, name='atualizar-redacao')
]
