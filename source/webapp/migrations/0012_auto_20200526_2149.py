# Generated by Django 2.2 on 2020-05-26 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_auto_20200526_2129'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brand',
            options={'verbose_name': 'Бренд', 'verbose_name_plural': 'Бренды'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория', 'verbose_name_plural': 'Категории'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name': 'Новость', 'verbose_name_plural': 'Новости'},
        ),
        migrations.AlterModelOptions(
            name='review',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='subcategory',
            options={'verbose_name': 'Подкатегория', 'verbose_name_plural': 'Подкатегория'},
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(blank=True, choices=[('white', 'Белый'), ('green', 'Зеленый'), ('grey', 'Серый'), ('blue', 'Синий'), ('red', 'Красный'), ('yellow', 'Желтый'), ('black', 'Черный'), ('orange', 'Оранжевый'), ('brown', 'Коричневый'), ('#F0DEBA;', 'Бежевый'), ('pink', 'Розовый'), ('purple', 'Фиолетовый'), ('darkblue', 'Темно-синий'), ('darkgreen', 'Темно-зеленый')], default='white', max_length=20, null=True, verbose_name='Цвет'),
        ),
    ]