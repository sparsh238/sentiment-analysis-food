# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-24 04:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0006_auto_20180424_1011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='timetables',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]