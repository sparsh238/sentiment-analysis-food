# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-23 22:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reviews', '0002_auto_20180424_0150'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plots',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_plot', models.ImageField(blank=True, null=True, upload_to='')),
                ('breakfast_plot', models.ImageField(blank=True, null=True, upload_to='')),
                ('lunch_plot', models.ImageField(blank=True, null=True, upload_to='')),
                ('snacks_plot', models.ImageField(blank=True, null=True, upload_to='')),
                ('dinner_plot', models.ImageField(blank=True, null=True, upload_to='')),
                ('pie_chart', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.AddField(
            model_name='reviews',
            name='pub_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]