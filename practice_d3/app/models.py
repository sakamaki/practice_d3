# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Hotentry(models.Model):
    bookmark_user_count = models.IntegerField()
    bookmark_title = models.CharField(max_length=1024)
    description = models.TextField(max_length=4096, blank=True)
    entry_date = models.DateTimeField(db_index=True)
    link = models.CharField(max_length=2048)
    rank = models.IntegerField()
    category = models.CharField(max_length=1024)

    class Meta(object):
        select_on_save = True
