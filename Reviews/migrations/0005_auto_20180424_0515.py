# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 23:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0004_auto_20180424_0514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plots',
            name='id',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
        ),
    ]
