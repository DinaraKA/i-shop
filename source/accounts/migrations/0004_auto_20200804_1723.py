# Generated by Django 2.2 on 2020-08-04 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200522_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='type',
            field=models.CharField(choices=[('client', 'Физическое лицо'), ('company', 'Юридическое лицо'), ('dealer', 'Дилер'), ('trader', 'Оптовик')], max_length=20, verbose_name='Тип'),
        ),
    ]
