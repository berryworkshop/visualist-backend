# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-12 21:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0016_auto_20170912_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='address_for',
        ),
        migrations.AddField(
            model_name='record',
            name='addresses',
            field=models.ManyToManyField(blank=True, to='api.Address'),
        ),
    ]
