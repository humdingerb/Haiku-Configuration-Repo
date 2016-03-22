# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-11 00:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0004_auto_20160110_2055'),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=200)),
                ('notes', models.CharField(default='', max_length=500)),
                ('is_working', models.CharField(default='', max_length=10)),
                ('rating', models.IntegerField()),
                ('author_first_name', models.CharField(default='', max_length=50)),
                ('author_last_name', models.CharField(default='', max_length=50)),
                ('author_email', models.CharField(default='', max_length=100)),
                ('date_created', models.DateTimeField(auto_now=True, verbose_name='date created')),
                ('date_modified', models.DateTimeField(auto_now=True, verbose_name='date modified')),
                ('cpu', models.CharField(default='', max_length=100)),
                ('motherboard', models.CharField(default='', max_length=100)),
                ('hard_drive', models.CharField(default='', max_length=100)),
                ('sound', models.CharField(default='', max_length=100)),
                ('is_sound_working', models.CharField(default='', max_length=10)),
                ('display', models.CharField(default='', max_length=100)),
                ('display_configuration', models.CharField(default='', max_length=20)),
                ('is_display_working', models.CharField(default='', max_length=10)),
                ('graphics_card', models.CharField(default='', max_length=100)),
                ('graphics_card_is_working', models.CharField(default='', max_length=10)),
            ],
        ),
    ]