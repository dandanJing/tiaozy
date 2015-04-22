# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0007_user_items_table_istradesuccess'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('display_items', '0004_item_messages_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('CommentId', models.CharField(unique=True, max_length=100)),
                ('Message', models.TextField(default=b'')),
                ('PostTime', models.IntegerField(default=0)),
                ('Grade', models.FloatField(default=0.0)),
                ('IsDelete', models.BooleanField(default=False)),
                ('CommentUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('Item', models.ForeignKey(to='ssl_users.user_items_table')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
