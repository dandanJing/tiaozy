# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0008_tzy_users_realname'),
    ]

    operations = [
        migrations.AddField(
            model_name='tzy_users',
            name='AvatarUrl',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
