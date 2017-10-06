# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-05 23:55
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_auto_20171005_1622'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='source',
            name='authors',
        ),
        migrations.AddField(
            model_name='source',
            name='author_primary',
            field=models.CharField(default='', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='record',
            name='properties',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
        migrations.AlterField(
            model_name='source',
            name='extra',
            field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, default={}),
        ),
    ]
