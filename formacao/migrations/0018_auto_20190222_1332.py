# Generated by Django 2.1.1 on 2019-02-22 13:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0017_auto_20190221_0855'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='formacao_conclusao',
            name='ultima_funcao',
        ),
        migrations.RemoveField(
            model_name='selecionado_formacao',
            name='ultima_funcao',
        ),
        migrations.AddField(
            model_name='selecionado_formacao',
            name='instituicao',
            field=models.CharField(choices=[('Centro Polivalente Nzoji', 'Centro Polivalente Nzoji'), ('Escola Nacional de Policia de Ordem Publica', 'Escola Nacional de Policia de Ordem Publica'), ('Escola Nacional de Policia de protecção e Intervenção', 'Escola Nacional de Policia de protecção e Intervenção'), ('Instituto Superior de Ciências Policias e Criminais', 'Instituto Superior de Ciências Policias e Criminais'), ('Instituto Médio de Ciências Policias', 'Instituto Médio de Ciências Policias')], default=' CPL', max_length=900, null=True),
        ),
        migrations.AlterField(
            model_name='formacao_conclusao',
            name='curso',
            field=models.CharField(max_length=900),
        ),
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2019, 2, 22), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='curso',
            field=models.CharField(choices=[('Agente de Vigilância e Escolta', 'Agente de Vigilância e Escolta'), ('Técnico de Inteligência', 'Técnico de Inteligência'), ('Agente de Inteligência', 'Agente de Inteligência'), ('Escrivão de policia', 'Escrivão de policia'), ('Perito Criminal Geral', 'Perito Criminal Geral'), ('Investigador de Policia Civil', 'Investigador de Policia Civil'), ('Auxiliar de Perícia Médica', 'Auxiliar de Perícia Médica'), ('Agente de Segurança Penitenciária', 'Agente de Segurança Penitenciária'), ('Noções de Direitos Humanos', 'Noções de Direitos Humanos'), ('Pilotagem', 'Pilotagem'), ('Auditoria', 'Auditoria'), ('Exercícios de Direito Administrativo', 'Exercícios de Direito Administrativo')], max_length=900),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='data',
            field=models.DateField(default=datetime.date(2019, 2, 22), null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='pais',
            field=models.CharField(choices=[(' ', ' '), ('Africa do Sul', 'Africa do Sul'), ('Afeganistão', 'Afeganistão'), ('Albânia', 'Albânia'), ('Alemanha', 'Alemanha'), ('Andorra', 'Andorra'), ('Argélia', 'Argélia'), ('Argentina', 'Argentina'), ('Austrália', 'Austrália'), ('Bélgica', 'Bélgica'), ('Bolívia', 'Bolívia'), ('Brasil', 'Brasil'), ('Botsuana', 'Botsuana'), ('Cabo Verde', 'Cabo Verde'), ('Canada', 'Canada'), ('China', 'China'), ('Costa Rica', 'Costa Rica'), ('cubana', 'cubana'), ('Espanha', 'Espanha'), ('Estados Unidos', 'Estados Unidos'), ('França', 'França'), ('Gabão', 'Gabão'), ('Grécia', 'Grécia'), ('Holanda', 'Holanda'), ('Russia', 'Russia')], default='Angola', max_length=100, null=True),
        ),
    ]
