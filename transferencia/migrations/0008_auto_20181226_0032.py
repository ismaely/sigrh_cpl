# Generated by Django 2.1.1 on 2018-12-26 00:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferencia', '0007_auto_20181208_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pedido',
            name='data_entrada',
            field=models.CharField(default=datetime.date(2018, 12, 26), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='transferencia',
            name='data',
            field=models.CharField(default=datetime.date(2018, 12, 26), max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='troca',
            name='data',
            field=models.CharField(default=datetime.date(2018, 12, 26), max_length=20, null=True),
        ),
    ]
