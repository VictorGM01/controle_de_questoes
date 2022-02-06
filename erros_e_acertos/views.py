from django.shortcuts import render, reverse
from django.views.generic import CreateView
from .forms import CadastroForms
from .models import Lista


def index(request):
    return render(request, 'acertos_e_erros/index.html')


class AdicionarRegistro(CreateView):
    template_name = "acertos_e_erros/adicionar_registros.html"
    form_class = CadastroForms

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
