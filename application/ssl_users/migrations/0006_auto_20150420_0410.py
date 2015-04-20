# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0005_auto_20150420_0248'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_items_table',
            name='ContactUserName',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user_items_table',
            name='ContactUserPhone',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='user_items_table',
            name='IsBlock',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
