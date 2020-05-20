# Generated by Django 2.2 on 2020-05-20 21:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0007_auto_20200511_1828'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='category_images', verbose_name='Изображение'),
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.IntegerField(default=None, verbose_name='Оценка')),
                ('text', models.TextField(blank=True, max_length=500, null=True, verbose_name='Отзыв')),
                ('date', models.DateField(auto_now_add=True, null=True, verbose_name='Дата')),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='review_author', to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
                ('product', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='webapp.Product', verbose_name='Товар')),
            ],
        ),
    ]
