# Generated by Django 4.0.2 on 2022-02-12 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redacoes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='redaction',
            name='genero',
            field=models.TextField(choices=[('Dissertação', 'Dissertacao'), ('Artigo de Opinião', 'Artigo De Opiniao'), ('Carta Aberta', 'Carta Aberta'), ('Resenha', 'Resenha'), ('Crônica Reflexiva', 'Cronica Reflexiva'), ('Narração', 'Narracao'), ('Descrição', 'Descricao'), ('Estilo Jornalístico', 'Jornalistico'), ('Comentário', 'Comentario')], max_length=30),
        ),
    ]