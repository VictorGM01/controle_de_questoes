from django.contrib import admin
from .models import Redaction


@admin.register(Redaction)
class RedacaoAdmin(admin.ModelAdmin):
    list_display = ['tema', 'genero']
