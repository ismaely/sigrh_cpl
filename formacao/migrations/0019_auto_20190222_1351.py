# Generated by Django 2.1.1 on 2019-02-22 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0018_auto_20190222_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='instituicao',
            field=models.CharField(choices=[('Centro Polivalente Nzoji', 'Centro Polivalente Nzoji'), ('Escola Nacional de Policia de Ordem Publica', 'Escola Nacional de Policia de Ordem Publica'), ('Escola Nacional de Policia de protecção e Intervenção', 'Escola Nacional de Policia de protecção e Intervenção'), ('Instituto Superior de Ciências Policias e Criminais', 'Instituto Superior de Ciências Policias e Criminais'), ('Instituto Médio de Ciências Policias', 'Instituto Médio de Ciências Policias')], default=' ', max_length=900, null=True),
        ),
    ]
