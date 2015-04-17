# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_items_table',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('itemid', models.CharField(unique=True, max_length=100)),
                ('itemname', models.CharField(max_length=100)),
                ('itemcostprice', models.IntegerField(default=0)),
                ('itemprice', models.IntegerField(default=0)),
                ('itemsnum', models.IntegerField(default=1)),
                ('itemImageurl', models.TextField(default=b'[]')),
                ('clickCount', models.IntegerField(default=0)),
                ('postTime', models.IntegerField(default=0)),
                ('lastEditTime', models.IntegerField(default=0)),
                ('isBlock', models.BooleanField(default=True)),
                ('feature', models.CharField(default=b'\xe5\x85\xa8\xe6\x96\xb0', max_length=100)),
                ('itemType', models.CharField(default=b'', max_length=20)),
                ('LikeList', models.TextField(default=b'[]')),
                ('LikeCount', models.IntegerField(default=0)),
                ('ReportList', models.TextField(default=b'[]')),
                ('ReportReason', models.TextField(default=b'')),
                ('tzyUser', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='tzy_users',
            name='is_student',
        ),
        migrations.AddField(
            model_name='tzy_users',
            name='isStudent',
            field=models.BooleanField(default=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tzy_users',
            name='mobilephone',
            field=models.CharField(default=b'', max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tzy_users',
            name='nickname',
            field=models.CharField(max_length=20),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tzy_users',
            name='qq',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
