#-*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Info(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=100, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('info:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Informacja'
        verbose_name_plural = 'Informacje'
        

class News(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Autor")
    title = models.CharField(max_length=100, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('news:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Aktualności'
        verbose_name_plural = 'Aktualności'
        

class Pack(models.Model):
    title = models.CharField(max_length=100, verbose_name="Tytuł")
    description = models.TextField(verbose_name="Opis")
    price = models.IntegerField(default=0, verbose_name="Cena")
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('pack:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Pakiet'
        verbose_name_plural = 'Pakiety'
        
        
class Equipment(models.Model):
    producer = models.CharField(max_length=100, verbose_name="Producent")
    model = models.CharField(max_length=100, verbose_name="Model")
    description = models.TextField(verbose_name="Opis")
    image = models.FileField(verbose_name="Ścieżka do zdjęcia", upload_to='Image/%Y-%m-%d')
    created_date = models.DateTimeField(default=timezone.now)
    
    def get_absolute_url(self):
        return reverse('equipment:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Sprzęt'
        verbose_name_plural = 'Sprzęty'