# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 23:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0003_auto_20180424_0400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plots',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]