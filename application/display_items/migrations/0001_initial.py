# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ask_info_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ItemId', models.CharField(unique=True, max_length=100)),
                ('Title', models.TextField(default=b'')),
                ('ClickCount', models.IntegerField(default=0)),
                ('PostTime', models.IntegerField(default=0)),
                ('IsBlock', models.BooleanField(default=False)),
                ('ContactUserName', models.CharField(default=b'', max_length=100)),
                ('ContactUserPhone', models.CharField(default=b'', max_length=20)),
                ('ItemType', models.CharField(default=b'', max_length=20)),
                ('LikeList', models.TextField(default=b'[]')),
                ('LikeCount', models.IntegerField(default=0)),
                ('ReportList', models.TextField(default=b'[]')),
                ('ReportReason', models.TextField(default=b'')),
                ('ItemDescription', models.TextField(default=b'')),
                ('TzyUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
