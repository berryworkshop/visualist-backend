# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-29 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visualist', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='body',
            name='organization_types',
            field=models.CharField(choices=[('ARCHIVE', 'archive'), ('ASSOCIATION', 'association'), ('COMPANY', 'company'), ('ENSEMBLE', 'ensemble'), ('FOUNDATION', 'foundation'), ('GALLERY', 'gallery'), ('LIBRARY', 'library'), ('MUSEUM', 'museum'), ('SCHOOL', 'school')], default='GALLERY', max_length=20),
        ),
        migrations.AlterField(
            model_name='event',
            name='record_type',
            field=models.CharField(choices=[('EXHIBITION', 'exhibition'), ('PERFORMANCE', 'performance'), ('WORKSHOP', 'workshop'), ('LECTURE', 'lecture')], default='EXHIBITION', max_length=20),
        ),
    ]
