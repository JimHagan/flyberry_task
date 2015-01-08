# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0003_auto_20150108_1816'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='meeting_name',
            field=models.CharField(max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='meeting_year',
            field=models.IntegerField(null=True),
            preserve_default=True,
        ),
    ]
