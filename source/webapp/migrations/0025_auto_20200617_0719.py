# Generated by Django 2.2 on 2020-06-17 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0024_auto_20200616_1016'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='offer',
            field=models.BooleanField(default=False, verbose_name='Акция'),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('none', 'Любой'), ('white', 'Белый'), ('green', 'Зеленый'), ('grey', 'Серый'), ('blue', 'Синий'), ('red', 'Красный'), ('yellow', 'Желтый'), ('black', 'Черный'), ('orange', 'Оранжевый'), ('brown', 'Коричневый'), ('beige', 'Бежевый'), ('pink', 'Розовый'), ('purple', 'Фиолетовый')], default='none', max_length=20, null=True, verbose_name='Цвет'),
        ),
    ]
