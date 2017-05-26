# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-26 16:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('logID', models.AutoField(primary_key=True, serialize=False)),
                ('logHours', models.DecimalField(decimal_places=2, default=0, max_digits=4)),
                ('logNote', models.CharField(max_length=10000)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Log',
                'verbose_name_plural': 'Logs',
            },
        ),
    ]
