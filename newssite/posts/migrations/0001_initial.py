# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('news_text', models.TextField(max_length=200)),
                ('pub_date', models.DateTimeField(verbose_name=b'date to publish')),
                ('create_date', models.DateTimeField(verbose_name=b'date created')),
                ('last_edited', models.DateTimeField(verbose_name=b'last edited')),
                ('unpub_date', models.DateTimeField(verbose_name=b'unpublish date')),
            ],
        ),
    ]
