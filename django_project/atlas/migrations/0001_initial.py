# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-15 19:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PointInSpace',
            fields=[
                ('record_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='base.Record')),
            ],
            options={
                'abstract': False,
            },
            bases=('base.record',),
        ),
        migrations.CreateModel(
            name='Venue',
            fields=[
                ('pointinspace_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='atlas.PointInSpace')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
            bases=('atlas.pointinspace',),
        ),
    ]
