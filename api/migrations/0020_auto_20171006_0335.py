# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-06 03:35
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20171006_0321'),
    ]

    operations = [
        migrations.AddField(
            model_name='recordlocation',
            name='properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterUniqueTogether(
            name='recordsource',
            unique_together=set([('record', 'source')]),
        ),
    ]
