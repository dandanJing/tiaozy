# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0007_user_items_table_istradesuccess'),
    ]

    operations = [
        migrations.AddField(
            model_name='tzy_users',
            name='RealName',
            field=models.CharField(default=b'', max_length=50),
            preserve_default=True,
        ),
    ]
