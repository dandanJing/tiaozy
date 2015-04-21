# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('display_items', '0002_auto_20150420_0428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ask_info_table',
            name='TzyUser',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
