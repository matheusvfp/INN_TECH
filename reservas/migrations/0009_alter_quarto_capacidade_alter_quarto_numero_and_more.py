# Generated by Django 4.0.5 on 2022-07-09 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas', '0008_alter_reserva_options_alter_reserva_datasaida'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quarto',
            name='capacidade',
            field=models.IntegerField(help_text='*Campo Obrigatório', verbose_name='Capacidade'),
        ),
        migrations.AlterField(
            model_name='quarto',
            name='numero',
            field=models.IntegerField(help_text='*Campo Obrigatório', unique=True, verbose_name='Número'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='dataChegada',
            field=models.DateTimeField(help_text='*Campo Obrigatório', verbose_name='Data Chegada'),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='valorReserva',
            field=models.DecimalField(decimal_places=2, help_text='*Campo Obrigatório', max_digits=7, verbose_name='Valor da Reserva'),
        ),
    ]
