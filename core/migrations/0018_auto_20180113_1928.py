# Generated by Django 2.0 on 2018-01-13 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_page_short_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='pages', verbose_name='Изображение'),
        ),
    ]
