# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0003_auto_20150419_1524'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_items_table',
            name='itemDescription',
            field=models.TextField(default=b''),
            preserve_default=True,
        ),
    ]
