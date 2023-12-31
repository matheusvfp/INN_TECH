# Generated by Django 4.0.5 on 2022-07-09 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('financeiro', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagamento',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Criação'),
        ),
        migrations.AlterField(
            model_name='pagamento',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor'),
        ),
        migrations.AlterField(
            model_name='saida',
            name='dataCriacao',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Data Criação'),
        ),
        migrations.AlterField(
            model_name='saida',
            name='valor',
            field=models.DecimalField(decimal_places=2, max_digits=7, verbose_name='Valor'),
        ),
    ]
