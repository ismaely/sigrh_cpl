# Generated by Django 2.1.1 on 2019-02-14 18:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transferencia', '0013_auto_20190214_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transferencia',
            name='orgao_destino',
            field=models.CharField(choices=[('Comando-Geral', 'Comando-Geral'), ('Comando Provincial de Luanda', 'Comando Provincial de luanda'), ('Comando Provincial do Huambo', 'Comando Provincial do Huambo'), ('Comando Provincial do Bengo', 'Comando Provincial do Bengo'), ('Comando Provincial do Kuanza Sul', 'Comando Provincial do Kuanza Sul'), ('Comando Provincial do Kuanza Norte', 'Comando Provincial do Kuanza Norte'), ('Comando Provincial da Huila', 'Comando Provincial da Huila'), ('Comando Provincial da Lunda Norte', 'Comando Provincial da Lunda Norte'), ('Comando Provincial do Cunene', 'Comando Provincial do Cunene'), ('Comando Provincial do Uige', 'Comando Provincial do Uige'), ('Comando Provincial de Cabinda', 'Comando Provincial de Cabinda'), ('Comando Provincial do Namibe', 'Comando Provincial do Namibe'), ('Comando Provincial do Moxico', 'Comando Provincial do Moxico'), ('Comando Provincial do Bie', 'Comando Provincial do Bie'), ('Comando Provincial de Benguela', 'Comando Provincial de Benguela'), ('Comando Provincial do Malanje', 'Comando Provincial de Malanje'), ('Comando Provincial do Zaire', 'Comando Provincial do Zaire')], max_length=500),
        ),
    ]
