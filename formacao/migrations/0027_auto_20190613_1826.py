# Generated by Django 2.2.1 on 2019-06-13 18:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0026_auto_20190516_0129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2019, 6, 13), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='data',
            field=models.CharField(default=datetime.date(2019, 6, 13), max_length=40, null=True),
        ),
    ]