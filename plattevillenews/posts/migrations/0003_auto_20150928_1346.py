# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20150928_1305'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='published_date',
            new_name='published',
        ),
        migrations.RenameField(
            model_name='news',
            old_name='unpublish_date',
            new_name='unpublished',
        ),
    ]
