# Generated by Django 2.1.1 on 2018-11-15 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Documento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero_ordem', models.CharField(max_length=40)),
                ('data_entrada', models.CharField(max_length=20)),
                ('categoria', models.CharField(choices=[(' ', ' '), ('Guia de Marcha', 'Guia de Marcha'), ('Mensagem', 'Mensagem'), ('Plano de Trabalho', 'Plano de Trabalho'), ('Officios', 'Officios'), ('Mapas', 'Mapas'), ('Declarções', 'Declarções'), ('Informações', 'Informações'), ('Propostas', 'Propostas'), ('Actas', 'Actas'), ('Relatorios', 'Relatorios'), ('Diversos', 'Diversos')], max_length=60)),
                ('descricao', models.CharField(max_length=600)),
                ('arquivo', models.FileField(blank=True, null=True, upload_to='arquivos/%Y/')),
            ],
        ),
    ]
