# Generated by Django 2.1.1 on 2019-02-18 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0030_auto_20190218_0236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('1 Mes de Cadeia', '1 Mes de Cadeia'), ('1 Ano de Cadeia', '1 Ano de Cadeia'), ('2 Mes de Cadeia', '2 Mes de Cadeia'), ('outro', 'outro'), ('2 Ano de Cadeia', '2 Ano de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza')], max_length=500),
        ),
    ]
