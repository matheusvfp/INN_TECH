# Generated by Django 4.0.5 on 2023-10-12 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospede',
            name='cpf',
            field=models.CharField(default='TEMP_CPF', help_text='Campo Obrigatório', max_length=14, verbose_name='CPF'),
            preserve_default=False,
        ),
    ]
