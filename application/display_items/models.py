from django.db import models
from application.ssl_users.models import tzy_users
from application.ssl_users.models import user_items_table
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

class item_messages_table(models.Model):
    MessageId       = models.CharField(max_length=100, unique=True)
    Message         = models.TextField(default='')
    Item            = models.ForeignKey(user_items_table,null=False)
    TzyUser         = models.ForeignKey(tzy_users,null=True)
    PostTime        = models.IntegerField(default=0)
    IsBlock         = models.BooleanField( default=False)
    LikeList        = models.TextField(default='[]')
    LikeCount       = models.IntegerField(default=0)
    ReportList      = models.TextField(default='[]')
    ReportReason    = models.TextField(default='')
    
    @classmethod
    def isMessageExist(cls, message_id):
        try:
            cls.objects.get(MessageId=message_id)
        except cls.DoesNotExist:
            return False
        else:
            return True

    @classmethod
    def getObject(cls, message_id):
        try:
            return cls.objects.get(MessageId=message_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def createUniqueMessageId(cls):
        message_id = md5HashEncodeWithTime(getRandomString())
        while cls.isMessageExist(message_id):
            message_id = md5HashEncodeWithTime(getRandomString())
        return message_id

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

class comments_table(models.Model):
    CommentId       = models.CharField(max_length=100, unique=True)
    Message         = models.TextField(default='')
    Item            = models.ForeignKey(user_items_table,null=False)
    CommentUser     = models.ForeignKey(tzy_users,null=False)
    PostTime        = models.IntegerField(default=0)
    Grade           = models.FloatField(default=0.0)
    IsDelete        = models.BooleanField(default=False)

    @classmethod
    def isCommentExist(cls, comment_id):
        try:
            cls.objects.get(CommentId=comment_id)
        except cls.DoesNotExist:
            return False
        else:
            return True

    @classmethod
    def getObject(cls, comment_id):
        try:
            return cls.objects.get(CommentId=comment_id)
        except cls.DoesNotExist:
            return None

    @classmethod
    def createUniqueCommentId(cls):
        comment_id = md5HashEncodeWithTime(getRandomString())
        while cls.isCommentExist(comment_id):
            comment_id = md5HashEncodeWithTime(getRandomString())
        return comment_id