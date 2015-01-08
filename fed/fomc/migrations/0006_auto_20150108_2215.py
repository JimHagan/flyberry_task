# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0005_auto_20150108_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='meeting_month',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
