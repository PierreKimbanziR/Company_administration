# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

class UserCreation(AbstractUser):
    user_id = models
    username = models.CharField(max_length=150, blank=False, unique=True)
    first_name= models.CharField(max_length=150, blank=False)
    last_name= models.CharField(max_length=150, blank=False)
    email= models.EmailField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

