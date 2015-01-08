# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fomc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meetingscheduleentry',
            name='raw_entry',
            field=models.TextField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='data_retrieval_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='estimated_release',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='meeting_end_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='meeting_start_date',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='projecttions',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='meetingscheduleentry',
            name='statement',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
