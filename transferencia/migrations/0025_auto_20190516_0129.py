# Generated by Django 2.2.1 on 2019-05-16 01:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferencia', '0024_auto_20190515_1327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='troca',
            name='data',
            field=models.CharField(default=datetime.date(2019, 5, 16), max_length=20, null=True),
        ),
    ]