from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserInfo(models.Model):
    fname = models.CharField(max_length = 200)
    lname = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)


