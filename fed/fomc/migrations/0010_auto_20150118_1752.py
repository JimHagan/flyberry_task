# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0009_meetingscheduleentry_statement_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='proections_html_url',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='projections_pdf_url',
            field=models.CharField(max_length=256, null=True),
            preserve_default=True,
        ),
    ]
