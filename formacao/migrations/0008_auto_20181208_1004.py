# Generated by Django 2.1.1 on 2018-12-08 10:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0007_auto_20181204_0213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2018, 12, 8), max_length=20, null=True),
        ),
    ]
