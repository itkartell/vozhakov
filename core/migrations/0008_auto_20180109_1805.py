# Generated by Django 2.0 on 2018-01-09 18:05

import ckeditor_uploader.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Заголовок')),
                ('slug', models.SlugField(max_length=255)),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='ArticleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категория статей',
                'verbose_name_plural': 'Категории статей',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='a_category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.ArticleCategory', verbose_name='Выбрать категорию'),
        ),
    ]
