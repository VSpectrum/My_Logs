# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone as datetime
from taggit.managers import TaggableManager
# Create your models here.

class Log(models.Model):
    logID = models.AutoField(primary_key=True)
    order = models.SmallIntegerField()
    logHours = models.DecimalField(default=0, max_digits=4, decimal_places=2)
    logNote = models.TextField(blank=False)
    date = models.DateField(default=datetime.now, blank=False)
    tags = TaggableManager()

    class Meta:
        verbose_name = 'Log'
        verbose_name_plural = 'Logs'

    def __str__(self):
        return str(self.logID)