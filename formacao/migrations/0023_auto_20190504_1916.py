# Generated by Django 2.2.1 on 2019-05-04 19:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0022_auto_20190501_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2019, 5, 4), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='data',
            field=models.CharField(default=datetime.date(2019, 5, 4), max_length=40, null=True),
        ),
    ]
