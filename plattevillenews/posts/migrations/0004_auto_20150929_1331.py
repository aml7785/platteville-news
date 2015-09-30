# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_auto_20150928_1346'),
    ]

    operations = [
        migrations.RenameField(
            model_name='news',
            old_name='published',
            new_name='published_date',
        ),
    ]
