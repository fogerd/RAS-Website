# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Next_Meeting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_date', models.DateTimeField(verbose_name=b'meeting date')),
                ('meeting_time', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Officers',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('president', models.CharField(max_length=200)),
                ('vice_president', models.CharField(max_length=200)),
                ('treasurer', models.CharField(max_length=200)),
                ('secretary', models.CharField(max_length=200)),
                ('webmaster', models.CharField(max_length=200)),
            ],
        ),
    ]
