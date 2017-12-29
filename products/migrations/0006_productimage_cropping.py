# Generated by Django 2.0 on 2017-12-05 23:31

from django.db import migrations
import image_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_auto_20171205_2250'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='cropping',
            field=image_cropping.fields.ImageRatioField('image', '430x360', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping'),
        ),
    ]
