from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard_redacoes, name='dashboard-redacoes')
]
