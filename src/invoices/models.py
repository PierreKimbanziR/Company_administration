# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Invoice(models.Model):

    invoice_types = [("In", "In"), ("Out", "Out")]

    invoice_number = models.IntegerField()
    contact_idd = models.IntegerField()
    company_id = models.IntegerField()
    description = models.CharField(max_length=150)
    amount = models.IntegerField()
    type = models.CharField(max_length=150,  choices=invoice_types)

    def __str__(self):
        return  self.invoice_number
