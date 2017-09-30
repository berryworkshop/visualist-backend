# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 15:47
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20170928_0252'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('value', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='api.Category')),
            ],
        ),
        migrations.AddField(
            model_name='record',
            name='status',
            field=models.NullBooleanField(default=None),
        ),
        migrations.AddField(
            model_name='record',
            name='categories',
            field=models.ManyToManyField(to='api.Category'),
        ),
        migrations.AlterUniqueTogether(
            name='category',
            unique_together=set([('value', 'parent')]),
        ),
    ]