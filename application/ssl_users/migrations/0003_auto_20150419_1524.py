# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0002_auto_20150417_1803'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemImageurl',
            new_name='itemImageurls',
        ),
    ]
