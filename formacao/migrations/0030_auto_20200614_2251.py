# Generated by Django 2.2.4 on 2020-06-14 22:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0029_auto_20190704_0126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2020, 6, 14), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='selecionado_formacao',
            name='data',
            field=models.CharField(default=datetime.date(2020, 6, 14), max_length=40, null=True),
        ),
    ]