# Generated by Django 2.2 on 2020-08-07 08:46

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0053_auto_20200806_1630'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='color',
            field=colorfield.fields.ColorField(default='white', max_length=18),
        ),
    ]