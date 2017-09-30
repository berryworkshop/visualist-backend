# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 02:52
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20170928_0204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True),
        ),
    ]