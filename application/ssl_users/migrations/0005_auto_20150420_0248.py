# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ssl_users', '0004_user_items_table_itemdescription'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tzy_users',
            old_name='isStudent',
            new_name='IsStudent',
        ),
        migrations.RenameField(
            model_name='tzy_users',
            old_name='mobilephone',
            new_name='Mobilephone',
        ),
        migrations.RenameField(
            model_name='tzy_users',
            old_name='nickname',
            new_name='Nickname',
        ),
        migrations.RenameField(
            model_name='tzy_users',
            old_name='qq',
            new_name='QQ',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='clickCount',
            new_name='ClickCount',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='feature',
            new_name='Feature',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='isBlock',
            new_name='IsBlock',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemDescription',
            new_name='ItemDescription',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemid',
            new_name='ItemId',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemImageurls',
            new_name='ItemImageUrls',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemname',
            new_name='ItemName',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemcostprice',
            new_name='ItemOldPrice',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemprice',
            new_name='ItemPrice',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemType',
            new_name='ItemType',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='itemsnum',
            new_name='ItemsNum',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='lastEditTime',
            new_name='LastEditTime',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='postTime',
            new_name='PostTime',
        ),
        migrations.RenameField(
            model_name='user_items_table',
            old_name='tzyUser',
            new_name='TzyUser',
        ),
    ]
