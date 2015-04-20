# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_items', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ask_info_table',
            old_name='Title',
            new_name='ItemTitle',
        ),
    ]
