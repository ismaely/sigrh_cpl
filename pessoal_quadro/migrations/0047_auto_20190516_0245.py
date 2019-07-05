# Generated by Django 2.2.1 on 2019-05-16 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0046_auto_20190516_0129'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pessoa',
            old_name='casa_numero',
            new_name='municipio',
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('3 Mes de Cadeia', '3 Mes de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('1 Ano de Cadeia', '1 Ano de Cadeia'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('2 Mes de Cadeia', '2 Mes de Cadeia'), ('2 Ano de Cadeia', '2 Ano de Cadeia'), ('outro', 'outro'), ('1 Mes de Cadeia', '1 Mes de Cadeia')], max_length=500),
        ),
        migrations.AlterField(
            model_name='pessoa',
            name='residencia',
            field=models.CharField(default='--', max_length=50, null=True),
        ),
    ]