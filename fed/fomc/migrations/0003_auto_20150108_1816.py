# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0002_auto_20150108_1811'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingscheduleentry',
            old_name='projecttions',
            new_name='projections',
        ),
    ]
