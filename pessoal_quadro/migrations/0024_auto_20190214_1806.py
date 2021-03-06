# Generated by Django 2.1.1 on 2019-02-14 18:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0023_auto_20190213_1539'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baixa',
            name='data_entrada',
            field=models.CharField(default=datetime.date(2019, 2, 14), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('1 Mes de Cadeia', '1 Mes de Cadeia'), ('2 Ano de Cadeia', '2 Ano de Cadeia'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('outro', 'outro'), ('1 Ano de Cadeia', '1 Ano de Cadeia'), ('2 Mes de Cadeia', '2 Mes de Cadeia')], max_length=500),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='data_colocacao',
            field=models.CharField(blank=True, default=datetime.date(2019, 2, 14), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patentiamento',
            name='data',
            field=models.CharField(default=datetime.date(2019, 2, 14), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reforma',
            name='data',
            field=models.CharField(default=datetime.date(2019, 2, 14), max_length=10, null=True),
        ),
    ]
