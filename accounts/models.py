#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    description = models.CharField(max_length=100, default='', verbose_name="Opis")
    city = models.CharField(max_length=100, default='', verbose_name="Miasto")
    position = models.CharField(max_length=100, default='', verbose_name="Stanowisko")
    phone = models.IntegerField(default=0, verbose_name="Telefon")
    
    def __str__(self):
        return str(self.user)
    
    class Meta:
        verbose_name = "Profil"
        verbose_name_plural = "Profile"