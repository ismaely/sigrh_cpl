# Generated by Django 2.1.1 on 2019-02-22 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('formacao', '0020_auto_20190222_1446'),
    ]

    operations = [
        migrations.AddField(
            model_name='formacao_conclusao',
            name='instituicao',
            field=models.CharField(default=1, max_length=900),
            preserve_default=False,
        ),
    ]
