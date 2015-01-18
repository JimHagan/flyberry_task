# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0008_auto_20150118_1517'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='statement_url',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
