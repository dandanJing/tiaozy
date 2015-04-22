# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('display_items', '0005_comments_table'),
    ]

    operations = [
        migrations.AddField(
            model_name='comments_table',
            name='ItemPostUsername',
            field=models.CharField(default=b'', max_length=100),
            preserve_default=True,
        ),
    ]
