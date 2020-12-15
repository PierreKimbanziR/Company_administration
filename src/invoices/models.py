# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


from djmoney.models.fields import MoneyField

class Invoice(models.Model):

    invoice_types = [("In", "In"), ("Out", "Out")]

    invoice_number = models.IntegerField(unique=True)
    contact_id = models.ForeignKey("contacts.Contact", on_delete = models.CASCADE)
    company_id = models.ForeignKey("companies.Company", on_delete = models.CASCADE)
    description = models.CharField(max_length=150)
    amount = MoneyField(decimal_places=2, max_digits=14, default_currency="EUR")
    type = models.CharField(max_length=150,  choices=invoice_types)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.invoice_number)
