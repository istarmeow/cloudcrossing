# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-12 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField()),
                ('modified_time', models.DateTimeField()),
                ('excerpt', models.CharField(blank=True, max_length=200)),
                ('views', models.PositiveIntegerField(default=0)),
            ],
            options={
                'ordering': ['-created_time'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
