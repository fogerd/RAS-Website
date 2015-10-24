# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_dates', '0003_auto_20151023_2035'),
    ]

    operations = [
        migrations.AddField(
            model_name='officers',
            name='president_email',
            field=models.EmailField(default=b'youremail@rpi.edu', max_length=254),
        ),
        migrations.AddField(
            model_name='officers',
            name='secretary_email',
            field=models.EmailField(default=b'youremail@rpi.edu', max_length=254),
        ),
        migrations.AddField(
            model_name='officers',
            name='treasurer_email',
            field=models.EmailField(default=b'youremail@rpi.edu', max_length=254),
        ),
        migrations.AddField(
            model_name='officers',
            name='vice_president_email',
            field=models.EmailField(default=b'youremail@rpi.edu', max_length=254),
        ),
        migrations.AddField(
            model_name='officers',
            name='webmaster_email',
            field=models.EmailField(default=b'youremail@rpi.edu', max_length=254),
        ),
        migrations.AddField(
            model_name='officers',
            name='year',
            field=models.CharField(default=0, max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='officers',
            name='president',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='officers',
            name='secretary',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='officers',
            name='treasurer',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='officers',
            name='vice_president',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='officers',
            name='webmaster',
            field=models.CharField(max_length=80),
        ),
    ]
