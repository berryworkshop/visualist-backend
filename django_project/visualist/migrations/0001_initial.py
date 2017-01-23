# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-23 22:20
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('service', models.CharField(choices=[('FACEBOOK', 'Facebook'), ('PINTEREST', 'Pinterest'), ('TUMBLR', 'Tumblr'), ('TWITTER', 'Twitter')], default='FACEBOOK', max_length=20)),
                ('username', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('street', models.TextField(blank=True)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('state_province', models.CharField(blank=True, max_length=100)),
                ('postal_code', models.CharField(blank=True, max_length=100)),
                ('country', models.CharField(default='USA', max_length=3)),
            ],
            options={
                'verbose_name_plural': 'addresses',
            },
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Body',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('body_types', models.CharField(choices=[('PERSON', 'person'), ('ARCHIVE', 'archive'), ('ASSOCIATION', 'association'), ('COMPANY', 'company'), ('ENSEMBLE', 'ensemble'), ('FOUNDATION', 'foundation'), ('GALLERY', 'gallery'), ('LIBRARY', 'library'), ('MUSEUM', 'museum'), ('SCHOOL', 'school')], default='PERSON', max_length=20)),
                ('first_name', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='BodyEventJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('PRODUCED', 'producer of'), ('HOSTED', 'host of'), ('SHOWN', 'shown work during')], default='PRODUCED', max_length=25)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Body')),
            ],
        ),
        migrations.CreateModel(
            name='BodyPlaceJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('OCCUPIED', 'occupant of'), ('OWNER', 'owner of')], default='OCCUPIED', max_length=25)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Body')),
            ],
        ),
        migrations.CreateModel(
            name='DimensionSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('length', models.DecimalField(decimal_places=3, max_digits=7)),
                ('width', models.DecimalField(decimal_places=3, max_digits=7)),
                ('height', models.DecimalField(blank=True, decimal_places=3, max_digits=7, null=True)),
                ('dimension_unit', models.CharField(choices=[('mm', 'millimeters'), ('cm', 'centimeters'), ('m', 'meters'), ('in', 'inches'), ('ft', 'feet')], default='in', max_length=2)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('email_address', models.EmailField(max_length=254)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='email_set', to='visualist.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('start', models.DateTimeField(default=django.utils.timezone.now)),
                ('end', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('event_type', models.CharField(choices=[('EXHIBITION', 'exhibition'), ('PERFORMANCE', 'performance'), ('WORKSHOP', 'workshop')], default='EXHIBITION', max_length=20)),
                ('bodies', models.ManyToManyField(blank=True, through='visualist.BodyEventJoin', to='visualist.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='EventPlaceJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('HOSTED', 'hosted at')], default='SHOWN', max_length=25)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Event')),
            ],
        ),
        migrations.CreateModel(
            name='HourSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('country_code', models.PositiveSmallIntegerField(default=1, validators=[django.core.validators.MaxValueValidator(999)])),
                ('area_code', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(999)])),
                ('number', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(9999999)])),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phone_set', to='visualist.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
                ('room', models.CharField(blank=True, max_length=250)),
                ('latitude', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True, validators=[django.core.validators.MaxValueValidator(90), django.core.validators.MinValueValidator(-90)])),
                ('longitude', models.DecimalField(blank=True, decimal_places=8, max_digits=11, null=True, validators=[django.core.validators.MaxValueValidator(180), django.core.validators.MinValueValidator(-180)])),
                ('appointment_only', models.BooleanField(default=False)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='visualist.Address')),
                ('hours_open', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='visualist.HourSet')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('MEMBER', 'is member of'), ('FRIEND', 'is friend of')], default='MEMBER', max_length=25)),
                ('child', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='parents', to='visualist.Body')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='children', to='visualist.Body')),
            ],
        ),
        migrations.CreateModel(
            name='Website',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('contact_item_type', models.CharField(choices=[('BUSINESS', 'business'), ('PERSONAL', 'personal')], default='PERSONAL', max_length=20)),
                ('url', models.URLField()),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='website_set', to='visualist.Body')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.CharField(max_length=250, unique=True)),
                ('description', models.TextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='WorkBodyJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('CREATED', 'created by'), ('PUBLISHED', 'published by'), ('OWNED', 'owned by'), ('COLLECTION', 'in the collection of')], default='CREATED', max_length=25)),
                ('body', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Body')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Work')),
            ],
        ),
        migrations.CreateModel(
            name='WorkEventJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('SHOWN', 'shown during')], default='SHOWN', max_length=25)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Event')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Work')),
            ],
        ),
        migrations.CreateModel(
            name='WorkPlaceJoin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('relation_type', models.CharField(choices=[('SHOWN', 'shown at')], default='SHOWN', max_length=25)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Place')),
                ('work', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Work')),
            ],
        ),
        migrations.AddField(
            model_name='work',
            name='bodies',
            field=models.ManyToManyField(blank=True, through='visualist.WorkBodyJoin', to='visualist.Body'),
        ),
        migrations.AddField(
            model_name='work',
            name='dimension_set',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='visualist.DimensionSet'),
        ),
        migrations.AddField(
            model_name='work',
            name='events',
            field=models.ManyToManyField(blank=True, through='visualist.WorkEventJoin', to='visualist.Event'),
        ),
        migrations.AddField(
            model_name='work',
            name='places',
            field=models.ManyToManyField(blank=True, through='visualist.WorkPlaceJoin', to='visualist.Place'),
        ),
        migrations.AddField(
            model_name='eventplacejoin',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='places',
            field=models.ManyToManyField(blank=True, through='visualist.EventPlaceJoin', to='visualist.Place'),
        ),
        migrations.AddField(
            model_name='bodyplacejoin',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Place'),
        ),
        migrations.AddField(
            model_name='bodyeventjoin',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Event'),
        ),
        migrations.AddField(
            model_name='body',
            name='body_parents',
            field=models.ManyToManyField(blank=True, through='visualist.Relationship', to='visualist.Body'),
        ),
        migrations.AddField(
            model_name='body',
            name='places',
            field=models.ManyToManyField(blank=True, through='visualist.BodyPlaceJoin', to='visualist.Place'),
        ),
        migrations.AddField(
            model_name='alias',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='visualist.Body'),
        ),
        migrations.AddField(
            model_name='account',
            name='body',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account_set', to='visualist.Body'),
        ),
    ]
