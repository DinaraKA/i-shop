# Generated by Django 2.2 on 2020-07-12 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0037_auto_20200712_1538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminalpayment',
            name='payed',
            field=models.DecimalField(decimal_places=3, max_digits=8, verbose_name='Оплаченная сумма'),
        ),
    ]
