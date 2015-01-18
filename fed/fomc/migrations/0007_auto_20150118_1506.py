# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0006_auto_20150108_2215'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingscheduleentry',
            old_name='data_retrieval_date',
            new_name='scrape_data',
        ),
        migrations.RenameField(
            model_name='meetingtablesummary',
            old_name='data_retrieval_date',
            new_name='scrape_data',
        ),
    ]
