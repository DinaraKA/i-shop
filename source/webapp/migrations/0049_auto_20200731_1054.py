# Generated by Django 2.2 on 2020-07-31 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0048_product_vendor_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bar_coded',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Штрих код'),
        ),
        migrations.AddField(
            model_name='product',
            name='code',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Код товара'),
        ),
        migrations.AddField(
            model_name='product',
            name='tnvd_code',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='Код ТНВД'),
        ),
    ]
