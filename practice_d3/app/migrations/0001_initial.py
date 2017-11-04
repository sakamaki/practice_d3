# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-05 04:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hotentry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookmark_user_count', models.IntegerField()),
                ('bookmark_title', models.CharField(max_length=1024)),
                ('description', models.TextField(blank=True, max_length=4096)),
                ('entry_date', models.DateTimeField(db_index=True)),
                ('link', models.CharField(max_length=2048)),
                ('rank', models.IntegerField()),
                ('category', models.CharField(max_length=1024)),
            ],
            options={
                'select_on_save': True,
            },
        ),
    ]