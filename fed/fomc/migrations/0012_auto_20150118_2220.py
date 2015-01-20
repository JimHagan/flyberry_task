# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0011_auto_20150118_1753'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='MeetingTableSummary',
            new_name='ProjectionTableSummary',
        ),
        migrations.RenameField(
            model_name='projectiontablesummary',
            old_name='meeting',
            new_name='meeting_schedule_entry',
        ),
        migrations.RenameField(
            model_name='projectiontablesummary',
            old_name='table_as_json',
            new_name='table_body_as_json',
        ),
        migrations.RenameField(
            model_name='projectiontablesummary',
            old_name='title',
            new_name='table_name',
        ),
    ]
