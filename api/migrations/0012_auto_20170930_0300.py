# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-30 03:00
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_auto_20170930_0245'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='status',
            new_name='active',
        ),
    ]