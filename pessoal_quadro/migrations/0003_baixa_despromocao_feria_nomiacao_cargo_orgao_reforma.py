# Generated by Django 2.1.1 on 2018-11-15 04:12

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pessoal_quadro', '0002_agente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Baixa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('data_entrada', models.CharField(max_length=20)),
                ('data_oucorrencia', models.CharField(max_length=20)),
                ('motivo', models.CharField(choices=[(' ', 'Motivo'), ('Transferencia', 'Transferencia'), ('Acidente', 'Acidente'), ('Valecimento', 'Valecimento'), ('Dificiencia Contraida', 'Dificiencia Contraida'), ('Outro', 'Outro')], max_length=30)),
                ('descricao', models.CharField(default='Não descrita', max_length=420, null=True)),
                ('dispacho', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Despromocao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('data', models.CharField(max_length=20)),
                ('motivo', models.CharField(choices=[(' ', 'Motivo da Despromoção'), ('Indisciplina', 'Indisciplina'), ('Desvio de informação', 'Desvio de informação'), ('Omicido', 'Omicido'), ('Calunia e Defamação', 'Calunia e Defamação'), ('Outras', 'Outras')], max_length=30)),
                ('suspensao', models.CharField(max_length=500)),
                ('descricao', models.CharField(default='#######', max_length=1000, null=True)),
                ('dispacho', models.CharField(default='Sem dispacho', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Feria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('data_inicio', models.CharField(max_length=20)),
                ('data_fim', models.CharField(max_length=20)),
                ('situacao', models.CharField(blank=True, default='licença de feria', max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Nomiacao_Cargo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('cargo', models.CharField(blank=True, default='#######', max_length=20, null=True)),
                ('data', models.CharField(max_length=20)),
                ('tipo', models.CharField(choices=[(' ', 'Tipo'), ('Indicação', 'Indicação'), ('Nomiação', 'Nomiação')], max_length=100)),
                ('categoria', models.CharField(choices=[(' ', 'Categoria'), ('Graduação', 'Graduação'), ('Promoção', 'Promoção')], max_length=100)),
                ('dispacho', models.CharField(default='Sem dispacho', max_length=20, null=True)),
                ('descricao', models.CharField(default='#######', max_length=3500, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Orgao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('orgao_colocacao', models.CharField(blank=True, default='cpl', max_length=60, null=True)),
                ('localizacao', models.CharField(blank=True, default='sem local', max_length=40, null=True)),
                ('data_colocacao', models.CharField(blank=True, max_length=20, null=True)),
                ('dispacho', models.CharField(blank=True, default='Sem dispacho', max_length=20, null=True)),
                ('unidade', models.CharField(blank=True, default='cpl', max_length=90, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reforma',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='pessoal_quadro.Agente')),
                ('motivo', models.CharField(blank=True, choices=[(' ', 'Motivo'), ('Acidente', 'Acidente'), ('Valecimento', 'Valecimento'), ('Dificiencia Contraida', 'Dificiencia Contraida'), ('Outro', 'Outro')], default='Outro', max_length=100, null=True)),
                ('reforma', models.CharField(blank=True, default='sim', max_length=20, null=True)),
                ('data', models.CharField(default=datetime.date(2018, 11, 15), max_length=10, null=True)),
                ('dispacho', models.CharField(default='Sem dispacho', max_length=20, null=True)),
                ('descricao', models.CharField(default='Sem descrição', max_length=3500, null=True)),
            ],
        ),
    ]
