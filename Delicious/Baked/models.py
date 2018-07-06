# -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.db import models

# Create your models here.

class registeration(models.Model):
    Name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=264)
    Password = models.CharField(max_length=255, null=True)
    Confirmpass = models.CharField(max_length=255, null=True)

    def __str__(self):
        return self.Name

class Contact(models.Model):
    Name = models.CharField(max_length=264)
    Email = models.EmailField(max_length=254)
    Subject = models.CharField(max_length=264)
    Message = models.TextField(blank=True, null=True)
    File = models.ImageField(upload_to='photos', blank=True)

    def __str__(self):
        return self.Name
