# Generated by Django 2.0 on 2017-12-28 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('config', '0004_menutype_sitemenu_sitemenuitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sitemenu',
            name='menuType',
        ),
        migrations.DeleteModel(
            name='MenuType',
        ),
    ]