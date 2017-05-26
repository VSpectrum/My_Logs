# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from notes.models import Log

class LogDisplay(admin.ModelAdmin):
    def time_seconds(self, obj):
        return obj.date.strftime("%d-%b-%Y | %H:%M:%S")
    time_seconds.short_description = 'Date'
    list_display = ('logHours', 'logNote', 'order', 'date')

admin.site.register(Log, LogDisplay)