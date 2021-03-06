# Generated by Django 2.1.1 on 2018-11-30 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0009_auto_20181129_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baixa',
            name='data_entrada',
            field=models.CharField(default=datetime.date(2018, 11, 30), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='dispacho',
            field=models.CharField(default='Sem despacho', max_length=20),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='motivo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('1 Mes de Cadeia', '1 Mes de Cadeia'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('2 Ano de Cadeia', '2 Ano de Cadeia'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('Retirada da Patente', 'Retirada da Patente'), ('outro', 'outro'), ('1 Ano de Cadeia', '1 Ano de Cadeia')], max_length=500),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='data_colocacao',
            field=models.CharField(blank=True, default=datetime.date(2018, 11, 30), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patentiamento',
            name='data',
            field=models.CharField(default=datetime.date(2018, 11, 30), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reforma',
            name='data',
            field=models.CharField(default=datetime.date(2018, 11, 30), max_length=10, null=True),
        ),
    ]
