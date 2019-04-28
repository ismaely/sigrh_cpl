# Generated by Django 2.1.1 on 2018-11-29 19:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0004_auto_20181124_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='formacao_conclusao',
            name='pais',
            field=models.CharField(default='Angola', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='formacao_conclusao',
            name='razao_posse',
            field=models.CharField(default='Bolsa Interna', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='formacao_conclusao',
            name='ultima_funcao',
            field=models.CharField(default='CPL', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='selecionado_formacao',
            name='pais',
            field=models.CharField(choices=[('Africa do Sul', 'Africa do Sul'), ('Brasil', 'Brasil'), ('Espanha', 'Espanha'), ('Portugal', 'Portugal'), ('Russia', 'Russia')], default='Angola', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='selecionado_formacao',
            name='razao_posse',
            field=models.CharField(choices=[('Bolsa Interna', 'Bolsa Interna'), ('Bolsa Externa', 'Bolsa Externa')], default='Bolsa Interna', max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='selecionado_formacao',
            name='ultima_funcao',
            field=models.CharField(choices=[('Porteiro', 'Porteiro'), ('Oficial Simples', 'Oficial Simples'), ('Gramado', 'Gramado'), ('Rondante', 'Rondante'), ('Anfibo', 'Anfibo')], default=' CPL', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2018, 11, 29), max_length=20, null=True),
        ),
    ]
