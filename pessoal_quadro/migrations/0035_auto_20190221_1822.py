# Generated by Django 2.1.1 on 2019-02-21 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0034_auto_20190221_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='baixa',
            name='tipo_invalidez',
            field=models.CharField(choices=[('', ''), ('Permanente', 'Permanente'), ('Parcial', 'Parcial')], default='Não descrita', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='baixa',
            name='motivo',
            field=models.CharField(choices=[('Reforma', 'Reforma'), ('Demissão', 'Demissão'), ('Transferência', 'Transferência'), ('Falecimento', 'Falecimento'), ('Dificiência Contraída', 'Dificiência Contraída'), ('Invalidez', 'Invalidez'), ('Outro', 'Outro')], max_length=30),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('2 Mes de Cadeia', '2 Mes de Cadeia'), ('2 Ano de Cadeia', '2 Ano de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('outro', 'outro'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('1 Mes de Cadeia', '1 Mes de Cadeia'), ('1 Ano de Cadeia', '1 Ano de Cadeia')], max_length=500),
        ),
    ]
