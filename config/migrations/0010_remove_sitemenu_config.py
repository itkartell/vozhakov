# Generated by Django 2.0 on 2017-12-28 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0009_siteconfig_top_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemenu',
            name='config',
        ),
    ]
