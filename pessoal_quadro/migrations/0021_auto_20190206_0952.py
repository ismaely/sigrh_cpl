# Generated by Django 2.1.1 on 2019-02-06 09:52

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0020_auto_20190130_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('numero_processo', models.CharField(max_length=10)),
                ('data', models.CharField(max_length=20)),
                ('motivo', models.CharField(choices=[('Homicído', 'Homicído'), ('Desvio de informação', 'Desvio de informação'), ('Calúnia e Difamação', 'Calúnia e Difamação'), ('Ausência', 'Ausência'), ('Desacato a Lei', 'Desacato a Lei'), ('Outro', 'Outro')], max_length=4000)),
                ('pena', models.CharField(choices=[('Repreensão simples', 'Repreensão simples'), ('Repreensão registada', 'Repreensão registada'), ('Patrulhas, guardas e piquetes até 5 por mês', 'Patrulhas, guardas e piquetes até 5 por mês'), ('Rondas, guardas e piquetes até 5 por mês', 'Rondas, guardas e piquetes até 5 por mês'), ('Multa correspondente a 1 dia', 'Multa correspondente a 1 dia'), ('Multa correspondente a 20 dia', 'Multa correspondente a 20 dia'), ('Detenção até 25 dias', 'Detenção até 25 dias'), ('Prisão até 15 dias', 'Prisão até 15 dias'), ('Prisão até 30 dias', 'Prisão até 30 dias'), ('Prisão até 45 dias', 'Prisão até 45 dias'), ('Despromoção', 'Despromoção'), ('Delegado', 'Delegado')], max_length=800)),
                ('dispacho', models.CharField(default='Sem dispacho', max_length=20, null=True)),
                ('descricao', models.CharField(default=' ', max_length=9500, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='disciplina/%Y/')),
            ],
        ),
        migrations.AlterField(
            model_name='baixa',
            name='data_entrada',
            field=models.CharField(default=datetime.date(2019, 2, 6), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='baixa',
            name='motivo',
            field=models.CharField(choices=[('Transferência', 'Transferência'), ('Falecimento', 'Falecimento'), ('Dificiência Contraída', 'Dificiência Contraída'), ('Demissão', 'Demissão'), ('Outro', 'Outro')], max_length=30),
        ),
        migrations.AlterField(
            model_name='despromocao',
            name='suspensao',
            field=models.CharField(choices=[('2 Ano de Cadeia', '2 Ano de Cadeia'), ('1 Mes de Cadeia', '1 Mes de Cadeia'), ('1 Ano de Cadeia', '1 Ano de Cadeia'), ('Retirada da Patente', 'Retirada da Patente'), ('outro', 'outro'), ('3 Mes de Cadeia', '3 Mes de Cadeia'), ('Prestar serviço de Limpeza', 'Prestar serviço de Limpeza'), ('2 Mes de Cadeia', '2 Mes de Cadeia')], max_length=500),
        ),
        migrations.AlterField(
            model_name='nomiacao_cargo',
            name='cargo',
            field=models.CharField(choices=[('Delegado', 'Delegado'), ('Investigador', 'Investigador'), ('Auxiliar de Investigador', 'Auxiliar de Investigador'), ('Escrivão', 'Escrivão'), ('Perito Criminal', 'Perito Criminal'), ('perito Medico-Legista', 'perito Medico-Legista')], max_length=200),
        ),
        migrations.AlterField(
            model_name='orgao',
            name='data_colocacao',
            field=models.CharField(blank=True, default=datetime.date(2019, 2, 6), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='patentiamento',
            name='data',
            field=models.CharField(default=datetime.date(2019, 2, 6), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='reforma',
            name='data',
            field=models.CharField(default=datetime.date(2019, 2, 6), max_length=10, null=True),
        ),
    ]
