# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from companies import models as companies_models
from contacts import models as contacts_models

class Invoice(models.Model):

    invoice_types = [("In", "In"), ("Out", "Out")]

    invoice_number = models.IntegerField()
    contact_id = models.ForeignKey(contacts_models.Contact, on_delete = models.CASCADE)
    company_id = models.ForeignKey(companies_models.Company, on_delete = models.CASCADE)
    description = models.CharField(max_length=150)
    amount = models.IntegerField()
    type = models.CharField(max_length=150,  choices=invoice_types)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return  str(self.invoice_number)
