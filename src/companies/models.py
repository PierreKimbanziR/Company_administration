# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Company(models.Model):

    roles = [("CLI", "Client"), ("PROV", "Provider")]


    name = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    vat_number = models.IntegerField()
    role = models.CharField(max_length=150, choices=roles, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


