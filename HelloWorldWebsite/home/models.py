# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Counter(models.Model):
    count = models.IntegerField(blank=False, default=0)

class Artist(models.Model):
    id = models.CharField(max_length=100, primary_key=True)
    name = models.CharField(max_length=100)
<<<<<<< HEAD
    related = models.ManyToManyField("self", related_name="_related", symmetrical=False, blank=True)
    img = models.CharField(max_length=1000, default='no image available')
||||||| merged common ancestors
    related = models.ManyToManyField("self", related_name="_related", symmetrical=False, blank=True)
=======
    related = models.ManyToManyField("self", related_name="_related", symmetrical=False, blank=True)
>>>>>>> 0c543ee2edd8c4596291d1706f4bb1bf2138781b
