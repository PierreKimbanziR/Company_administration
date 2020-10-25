# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Company(models.Model):


    roles = [("CLI", "Client"), ("PROV", "Provider")]
    Name = models.CharField(max_length=150)
    Country = models.CharField(max_length=150)
    Vat_Number = models.IntegerField()
    Role = models.CharField(max_length=150, choices=roles, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Name

    def get_companies(self):
        name = []
        country =[]
        vat =[]
        role =[]
        for company in Company.objects.all().order_by('Name'):
            name.append(company.Name)
            country.append(company.Country)
            vat.append(company.Vat_Number)
            role.append(company.Role)
        attribute_list = zip(name,country,vat,role)

        return attribute_list
