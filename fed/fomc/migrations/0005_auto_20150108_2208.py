# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0004_auto_20150108_1939'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='meeting_month',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='unscheduled',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
