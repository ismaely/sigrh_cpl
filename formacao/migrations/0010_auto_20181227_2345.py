# Generated by Django 2.1.1 on 2018-12-27 23:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0009_auto_20181226_0032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presenca',
            name='data',
            field=models.CharField(default=datetime.date(2018, 12, 28), max_length=20, null=True),
        ),
    ]
