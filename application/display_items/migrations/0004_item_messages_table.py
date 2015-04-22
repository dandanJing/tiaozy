# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0007_user_items_table_istradesuccess'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display_items', '0003_auto_20150421_0700'),
    ]

    operations = [
        migrations.CreateModel(
            name='item_messages_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('MessageId', models.CharField(unique=True, max_length=100)),
                ('Message', models.TextField(default=b'')),
                ('PostTime', models.IntegerField(default=0)),
                ('IsBlock', models.BooleanField(default=False)),
                ('LikeList', models.TextField(default=b'[]')),
                ('LikeCount', models.IntegerField(default=0)),
                ('ReportList', models.TextField(default=b'[]')),
                ('ReportReason', models.TextField(default=b'')),
                ('Item', models.ForeignKey(to='ssl_users.user_items_table')),
                ('TzyUser', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
