# Generated by Django 2.2 on 2020-07-14 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0044_auto_20200714_1423'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderproduct',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='myorder', to='webapp.Order', verbose_name='Заказ'),
        ),
    ]
