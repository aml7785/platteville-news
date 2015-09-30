# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='status',
        ),
        migrations.AddField(
            model_name='news',
            name='is_published',
            field=models.BooleanField(default=True),
        ),
    ]
