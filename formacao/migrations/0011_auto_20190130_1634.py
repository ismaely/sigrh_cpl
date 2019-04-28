# Generated by Django 2.1.1 on 2019-01-30 16:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0010_auto_20181227_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2019, 1, 30), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='pais',
            field=models.CharField(choices=[(' ', ' '), ('Africa do Sul', 'Africa do Sul'), ('Afeganistão', 'Afeganistão'), ('Albânia', 'Albânia'), ('Alemanha', 'Alemanha'), ('Andorra', 'Andorra'), ('Argélia', 'Argélia'), ('Argentina', 'Argentina'), ('Austrália', 'Austrália'), ('Bélgica', 'Bélgica'), ('Bolívia', 'Bolívia'), ('Brasil', 'Brasil'), ('Botsuana', 'Botsuana'), ('Cabo Verde', 'Cabo Verde'), ('Canada', 'Canada'), ('China', 'China'), ('Costa Rica', 'Costa Rica'), ('cubana', 'cubana'), ('Espanha', 'Espanha'), ('Estados Unidos', 'Estados Unidos'), ('França', 'França'), ('Gabão', 'Gabão'), ('Grécia', 'Grécia'), ('Holanda', 'Holanda'), ('Russia', 'Russia')], default='Angola', max_length=40, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='ultima_funcao',
            field=models.CharField(choices=[('Centro Polivalente Nzoji', 'Centro Polivalente Nzoji'), ('Escola Nacional de Policia de Ordem Publica', 'Escola Nacional de Policia de Ordem Publica'), ('Escola Nacional de Policia de protecção e Intervenção', 'Escola Nacional de Policia de protecção e Intervenção'), ('Instituto Superior de Ciências Policias e Criminais', 'Instituto Superior de Ciências Policias e Criminais'), ('Instituto Médio de Ciências Policias', 'Instituto Médio de Ciências Policias')], default=' CPL', max_length=40, null=True),
        ),
    ]
