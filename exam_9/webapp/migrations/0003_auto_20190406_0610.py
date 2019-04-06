# Generated by Django 2.2 on 2019-04-06 06:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0002_auto_20190404_1457'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Категория')),
                ('description', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=255, verbose_name='Телефон')),
                ('address', models.CharField(blank=True, max_length=255, null=True, verbose_name='Адрес')),
                ('comment', models.TextField(blank=True, max_length=2000, null=True, verbose_name='Комментарий')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Время создания')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, max_length=2000, null=True)),
                ('arrival_date', models.DateField()),
                ('is_deleted', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('categories', models.ManyToManyField(blank=True, related_name='product', to='webapp.Category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='Product_photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='photo', to='webapp.Product', verbose_name='Фото продукта')),
            ],
        ),
        migrations.DeleteModel(
            name='Movie',
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ManyToManyField(related_name='order', to='webapp.Product', verbose_name='Продукты'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='order', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
