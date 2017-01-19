# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-18 22:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0003_auto_20170118_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contactselfjoin',
            name='child',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='parents', to='directory.Contact'),
        ),
        migrations.AlterField(
            model_name='contactselfjoin',
            name='parent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='children', to='directory.Contact'),
        ),
    ]