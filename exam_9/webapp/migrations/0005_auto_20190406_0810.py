# Generated by Django 2.2 on 2019-04-06 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_auto_20190406_0638'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_photo',
            name='photo',
        ),
        migrations.AddField(
            model_name='product_photo',
            name='images',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
