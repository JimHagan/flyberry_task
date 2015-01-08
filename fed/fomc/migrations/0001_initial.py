# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MeetingScheduleEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('meeting_start_date', models.DateTimeField()),
                ('meeting_end_date', models.DateTimeField()),
                ('statement', models.BooleanField(default=True)),
                ('projecttions', models.BooleanField(default=True)),
                ('data_retrieval_date', models.DateTimeField()),
                ('estimated_release', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MeetingTableSummary',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=100)),
                ('table_as_json', models.TextField()),
                ('data_retrieval_date', models.DateTimeField()),
                ('meeting', models.ForeignKey(to='fomc.MeetingScheduleEntry')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
