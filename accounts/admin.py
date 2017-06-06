#-*- coding: utf-8 -*-
from django.contrib import admin
from accounts.models import UserProfile

admin.site.register(UserProfile)