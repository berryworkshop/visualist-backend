# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-13 16:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='name_given',
            new_name='name_personal',
        ),
    ]