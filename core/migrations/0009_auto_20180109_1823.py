# Generated by Django 2.0 on 2018-01-09 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20180109_1805'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='a_category',
        ),
        migrations.DeleteModel(
            name='ArticleCategory',
        ),
    ]