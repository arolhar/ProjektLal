#-*- coding: utf-8 -*-
from django.contrib import admin
from . models import Info, News, Pack, Equipment

admin.site.register(Info)
admin.site.register(News)
admin.site.register(Pack)
admin.site.register(Equipment)