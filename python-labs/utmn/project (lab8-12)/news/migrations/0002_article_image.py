# Generated by Django 4.1.3 on 2022-12-01 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.TextField(blank=True, null=True, verbose_name='Изображение'),
        ),
    ]