from django.db import models
from application.ssl_users.models import tzy_users
from utils.utils import *

# Create your models here.
class ask_info_table(models.Model):
    ItemId          = models.CharField(max_length=100, unique=True)
    ItemTitle       = models.TextField(default='')
    ClickCount       = models.IntegerField(default = 0)
    PostTime        = models.IntegerField(default=0)
    IsBlock         = models.BooleanField( default=False)
    ContactUserName = models.CharField(max_length=100, default="")
    ContactUserPhone = models.CharField(max_length=20,default="")
    ItemType        = models.CharField(max_length=20,default="")
    TzyUser        = models.ForeignKey(tzy_users,null=True)
    LikeList        = models.TextField(default='[]')
    LikeCount       = models.IntegerField(default=0)
    ReportList      = models.TextField(default='[]')
    ReportReason    = models.TextField(default='')
    ItemDescription = models.TextField(default='')

    @classmethod
    def createUniqueItemId(cls):
        item_id = md5HashEncodeWithTime(getRandomString())
        while cls.isItemExist(item_id):
            item_id = md5HashEncodeWithTime(getRandomString())
        return item_id

    @classmethod
    def isItemExist(cls, item_id):
        try:
            cls.objects.get(ItemId=item_id)
        except cls.DoesNotExist:
            return False
        else:
            return True