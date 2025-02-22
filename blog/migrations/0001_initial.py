# Generated by Django 5.1.5 on 2025-01-15 15:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: сеггодня 212ww22434', max_length=250, verbose_name='Название статьи')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='URL')),
            ],
            options={
                'verbose_name': 'категоря ',
                'verbose_name_plural': 'Категория',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Например: сеггодня 21222434', max_length=250, verbose_name='Название статьи')),
                ('slug', models.CharField(max_length=255, unique=True, verbose_name='URL')),
                ('is_active', models.BooleanField(default=True, verbose_name='jnjfjfj')),
                ('content', models.TextField(verbose_name='Контент')),
                ('image', models.ImageField(upload_to='blog/', verbose_name='izo')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.category', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Посты ',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
