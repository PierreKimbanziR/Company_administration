# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from django_countries.fields import CountryField


class Company(models.Model):


    roles = [("CLI", "Client"), ("PROV", "Provider")]
    Name = models.CharField(max_length=150)
    Person_of_contact = models.OneToOneField('contacts.Contact', on_delete = models.CASCADE)
    Country = CountryField(blank_label='Select a country')
    Vat_Number = models.IntegerField(unique=True)
    Role = models.CharField(max_length=150, choices=roles, default=None)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name
