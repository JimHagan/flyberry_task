# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0007_auto_20150118_1506'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingscheduleentry',
            old_name='scrape_data',
            new_name='scrape_date',
        ),
        migrations.RenameField(
            model_name='meetingtablesummary',
            old_name='scrape_data',
            new_name='scrape_date',
        ),
        migrations.AlterUniqueTogether(
            name='meetingscheduleentry',
            unique_together=set([('meeting_name', 'scrape_date')]),
        ),
    ]
