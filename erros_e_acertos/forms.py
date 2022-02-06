from django import forms
from erros_e_acertos.models import Lista, Materia


class DateInput(forms.DateInput):
    input_type = "date"


class CadastroForms(forms.ModelForm):
    data_realizacao = forms.DateField(label='Data da Realização', widget=DateInput())

    class Meta:
        model = Lista
        fields = ['materia', 'nome_da_lista', 'quantidade_questoes', 'tipo', 'acertos', 'erros', 'descricao_erros',
                  'tempo_realizacao', 'data_realizacao']
        labels = {'materia': 'Matéria', 'nome_da_lista': 'Nome da Lista', 'quantidade_questoes': 'Número de Questões',
                  'tipo': 'Tipo da Lista', 'acertos': 'Quantidade de Acertos', 'erros': 'Quantidade de Erros',
                  'descricao_erros': 'Descrição do Erro', 'tempo_realizacao': 'Tempo para Realização'}
