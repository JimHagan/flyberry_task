# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0010_auto_20150118_1752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='meetingscheduleentry',
            old_name='proections_html_url',
            new_name='projections_html_url',
        ),
    ]
