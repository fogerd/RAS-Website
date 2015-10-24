# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_dates', '0002_auto_20151020_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nextmeeting',
            name='meeting_date',
            field=models.DateField(verbose_name=b'meeting date'),
        ),
    ]
