# Generated by Django 2.2 on 2020-07-16 13:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0046_auto_20200714_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orderproduct', to='webapp.Order', verbose_name='Заказ'),
        ),
        migrations.AlterField(
            model_name='terminalpayment',
            name='txn_id',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='TXN_ID'),
        ),
    ]
