# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime
from django.db import models
from django.conf import settings

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=120)
    first = models.CharField(max_length=120)
    last = models.CharField(max_length=120)
    def __str__(self):
        return self.username

class Query(models.Model):
    id = models.AutoField(primary_key=True)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    name = models.CharField(max_length=120)
    description = models.TextField()

    def __str__(self):
        return self.name

class KeyWord(models.Model):
   query = models.ForeignKey(Query, related_name='keywords', on_delete=models.CASCADE)
   word = models.CharField(max_length=120)

   def __str__(self):
       return self.word

class SourceType(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Source(models.Model):
    id = models.AutoField(primary_key=True)
    text = models.TextField()
    url = models.URLField()
    sourceType = models.ForeignKey(SourceType, on_delete=models.CASCADE)

    def __str__(self):
        return self.url


class Run(models.Model):
    id = models.AutoField(primary_key=True)
    query = models.ForeignKey(Query, on_delete=models.CASCADE)
    time = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title

class Result(models.Model):
    run = models.ForeignKey(Run, on_delete=models.CASCADE)
    source = models.ForeignKey(Source, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
