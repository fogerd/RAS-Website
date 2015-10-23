# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting_dates', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Next_Meeting',
            new_name='NextMeeting',
        ),
    ]
