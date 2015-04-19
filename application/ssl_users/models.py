#encoding=utf-8
from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from utils.utils import *

# Create your models here.
class tzy_users(AbstractUser):
    mobilephone = models.CharField(max_length=20,default="")
    qq          = models.IntegerField(default=0)
    nickname    = models.CharField(max_length=20)
    isStudent   = models.BooleanField(default=True)

    def __str__(self):
        return "username:%s\tphone:%s\temail:%s\t"%(self.username,self.mobilephone,self.email)

class user_items_table(models.Model):
    itemid          = models.CharField(max_length=100, unique=True)
    itemname        = models.CharField(max_length=100)
    itemcostprice   = models.IntegerField(default = 0)
    itemprice       = models.IntegerField(default = 0)
    itemsnum        = models.IntegerField(default = 1)
    itemImageurls    = models.TextField(default='[]')
    clickCount       = models.IntegerField(default = 0)
    postTime        = models.IntegerField(default=0)
    lastEditTime    = models.IntegerField(default=0)
    isBlock         = models.BooleanField( default=True)
    feature         = models.CharField(max_length=100,default="全新")
    itemType        = models.CharField(max_length=20,default="")
    tzyUser        = models.ForeignKey(tzy_users)
    LikeList        = models.TextField(default='[]')
    LikeCount       = models.IntegerField(default=0)
    ReportList      = models.TextField(default='[]')
    ReportReason    = models.TextField(default='')

    @classmethod
    def isItemExist(cls, item_id):
        try:
            cls.objects.get(itemid=item_id)
        except cls.DoesNotExist:
            return False
        else:
            return True

    @classmethod
    def getObject(cls, item_id):
        try:
            return cls.objects.get(itemid=item_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def createUniqueItemId(cls):
        item_id = md5HashEncodeWithTime(getRandomString())
        while cls.isItemExist(item_id):
            item_id = md5HashEncodeWithTime(getRandomString())
        return item_id

    def addLiker(self, liker):
        like_list = json_loads(self.LikeList)
        if liker not in like_list:
            like_list.append(liker)
            self.LikeList = json_dumps(like_list)
            self.LikeCount = len(like_list)
            self.save()

    def removeLiker(self, liker):
        like_list = json_loads(self.LikeList)
        if liker in like_list:
            like_list.remove(liker)
            self.LikeList = json_dumps(like_list)
            self.LikeCount = len(like_list)
            self.save()

    def isLiked(self, liker):
        return self.LikeList.find(liker) > -1

    def addReporter(self, reporter, reason):
        report_list = json_loads(self.ReportList)
        if reporter not in report_list:
            if self.ReportReason.find(reason) > -1:
                self.delete()
            else:
                self.ReportReason = '%s%s' % (self.ReportReason, reason)
                report_list.append(reporter)
                self.ReportList = json_dumps(report_list)
                self.save()

    def clickAction(self):
        self.clickCount = self.clickCount+1
        self.save()
    
    def __unicode__(self):
        return self.itemid