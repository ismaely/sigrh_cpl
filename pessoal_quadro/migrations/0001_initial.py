# Generated by Django 2.1.1 on 2018-11-15 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pessoa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('nome_pai', models.CharField(max_length=100)),
                ('nome_mae', models.CharField(max_length=100)),
                ('nacionalidade', models.CharField(max_length=50)),
                ('naturalidade', models.CharField(max_length=20)),
                ('data_nascimento', models.CharField(max_length=20)),
                ('bi', models.CharField(max_length=20, unique=True)),
                ('passporte', models.CharField(blank=True, max_length=25, null=True)),
                ('estado_civil', models.CharField(choices=[(' ', 'Estado Civil'), ('Solteiro (a)', 'solteiro (a)'), ('Casado (a)', 'casado (a)'), ('Divorciado (a)', 'Divorciado (a)'), ('Viuvo (a)', 'viuvo (a)')], max_length=20)),
                ('genero', models.CharField(choices=[(' ', 'Genero'), ('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=12)),
                ('provincia', models.CharField(choices=[(' ', 'Provincia'), ('Luanda', 'Luanda'), ('Bengo', 'Bengo'), ('Benguela', 'Benguela'), ('Bié', 'Bié'), ('Cabinda', 'Cabinda'), ('Cunene', 'Cunene'), ('Huambo', 'Huambo'), ('Huila', 'Huila'), ('Kwando kubango', 'Kwando kubango'), ('Kwanza norte', 'Kwanza norte'), ('Kwanza sul', 'Kwanza sul'), ('Lunda Norte', 'Lunda Norte'), ('Lunda sul', 'Lunda sul'), ('Moxico', 'Moxico'), ('Namibe', 'Namibe'), ('Uige', 'Uige'), ('Zaire', 'Zaire')], max_length=25)),
                ('municipio', models.CharField(blank=True, max_length=40, null=True)),
                ('residencia', models.CharField(max_length=30)),
                ('casa_numero', models.IntegerField()),
                ('telefone', models.CharField(max_length=23)),
                ('telefone_parente', models.CharField(max_length=26)),
                ('email', models.EmailField(blank=True, max_length=60, null=True)),
            ],
        ),
    ]
