# Generated by Django 2.2.1 on 2019-06-13 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0048_auto_20190516_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agente',
            name='patente',
            field=models.CharField(choices=[('Agente-1ª-Classe', 'Agente 1ª Classe'), ('Agente-2ª-Classe', 'Agente 2ª Classe'), ('Agente-3ª-Classe', 'Agente 3ª Classe'), ('1ª-Subchefe', '1ª subchefe'), ('2ª-Subchefe', '2ª Subchefe'), ('3ª-Subchefe', '3ª Subchefe'), ('Inspector', 'Inspector'), ('Sub-inspetor', 'Sub-inspetor'), ('Inspector-chefe', 'Inspector-chefe'), ('Intendente', 'Intendente'), ('Superintendente', 'Superintendente'), ('Sub-comissário', 'Sub-comissário'), ('Comissário-chefe', 'Comissário chefe'), ('Comissário-geral', 'Comissário geral')], max_length=60),
        ),
        migrations.AlterField(
            model_name='baixa',
            name='data_entrada',
            field=models.CharField(default=datetime.date(2019, 6, 13), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('2 Ano de Cadeia', '2 Ano de Cadeia'), ('1 Ano de Cadeia', '1 Ano de Cadeia'), ('2 Mes de Cadeia', '2 Mes de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('outro', 'outro'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('1 Mes de Cadeia', '1 Mes de Cadeia')], max_length=500),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='data_colocacao',
            field=models.CharField(blank=True, default=datetime.date(2019, 6, 13), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patentiamento',
            name='data',
            field=models.CharField(default=datetime.date(2019, 6, 13), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reforma',
            name='data',
            field=models.CharField(default=datetime.date(2019, 6, 13), max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='reforma',
            name='motivo',
            field=models.CharField(blank=True, choices=[('Acidente', 'Acidente'), ('Incapacidade', 'Incapacidade'), ('Dificiência Contraída', 'Dificiência Contraída'), ('Outro', 'Outro')], default='Outro', max_length=100, null=True),
        ),
    ]
