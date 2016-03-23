from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200,unique = True)
    password = models.CharField(max_length = 200)


#discussionTopic is a table which contains the topic description ,userid of the user  who posted the topic and date of the topic
class DiscussionTopic(models.Model):
    user = models.ForeignKey('UserInfo')     #user of the post just linking both the tables together
    topicText = models.CharField(max_length = 1000)
    timeStamp = models.DateTimeField()


#commentOnTopic contais the info about the comments on the topic and the userid of the user who commented and id of the topic o which the comment was made
class CommentOfTopic(models.Model):
    user = models.ForeignKey('UserInfo')
    topic = models.ForeignKey('DiscussionTopic')
    commentText = models.TextField(max_length = 1000)
    timestamp = models.DateTimeField(null = True)
