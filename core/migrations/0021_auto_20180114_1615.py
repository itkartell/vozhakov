# Generated by Django 2.0 on 2018-01-14 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_page_direction'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='text',
        ),
    ]