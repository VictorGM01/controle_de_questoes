from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('erros_e_acertos.urls')),
    path('users/', include('usuarios.urls')),
    path('redacoes/', include('redacoes.urls'))
]
