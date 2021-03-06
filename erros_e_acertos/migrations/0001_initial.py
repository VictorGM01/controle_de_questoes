# Generated by Django 4.0.2 on 2022-02-05 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lista',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('materia', models.TextField(choices=[('Matemática', 'Matematica'), ('Física', 'Fisica'), ('Português', 'Portugues'), ('História', 'Historia'), ('Filosofia', 'Filosofia'), ('Sociologia', 'Sociologia'), ('Biologia', 'Biologia'), ('Química', 'Quimica'), ('Literatura', 'Literatura'), ('Geografia', 'Geografia')], max_length=15)),
                ('nome_da_lista', models.CharField(max_length=100)),
                ('quantidade_questoes', models.IntegerField()),
                ('tipo', models.CharField(max_length=60)),
                ('acertos', models.IntegerField()),
                ('erros', models.IntegerField()),
                ('descricao_erros', models.CharField(max_length=300)),
                ('tempo_realizacao', models.IntegerField()),
                ('data_realizacao', models.DateField(default=datetime.datetime.today)),
            ],
        ),
    ]
