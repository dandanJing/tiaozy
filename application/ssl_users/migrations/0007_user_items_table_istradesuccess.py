# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0006_auto_20150420_0410'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_items_table',
            name='IsTradeSuccess',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
