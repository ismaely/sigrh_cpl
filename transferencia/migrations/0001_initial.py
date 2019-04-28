# Generated by Django 2.1.1 on 2018-11-15 04:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('origem', models.CharField(max_length=100)),
                ('destino', models.CharField(max_length=100)),
                ('data_entrada', models.CharField(max_length=20)),
                ('situacao', models.CharField(blank=True, choices=[(' ', 'Opção'), ('Espera', 'Espera'), ('Autorizado', 'Autorizado')], default='deferido', max_length=40, null=True)),
                ('motivo', models.TextField(blank=True, max_length=500, null=True)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='transferencia/%Y/')),
            ],
        ),
        migrations.CreateModel(
            name='Transferencia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('orgao_origem', models.CharField(max_length=100)),
                ('orgao_destino', models.CharField(max_length=100)),
                ('data_entrada', models.CharField(max_length=20)),
                ('motivo', models.TextField(blank=True, max_length=500, null=True)),
                ('arquivo', models.CharField(blank=True, max_length=100, null=True)),
                ('data', models.CharField(default=datetime.date(2018, 11, 15), max_length=20, null=True)),
                ('dispacho', models.CharField(default='Sem dispacho', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Troca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('primeiro_agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='primeiro_troca', to='pessoal_quadro.Agente')),
                ('segundo_agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='segundo_troca', to='pessoal_quadro.Agente')),
                ('origem_primeiro', models.CharField(max_length=100)),
                ('destino_primeiro', models.CharField(max_length=100)),
                ('origem_segundo', models.CharField(max_length=100)),
                ('destino_segundo', models.CharField(max_length=100)),
                ('data', models.DateField()),
                ('motivo', models.TextField(blank=True, max_length=500, null=True)),
            ],
        ),
    ]
