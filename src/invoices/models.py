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
    
    def get_invoices(self):
        numbers = []
        ids = []
        descriptions =[]
        amounts =[]
        types = []
        timestamps =[]

        for invoice in Invoice.objects.all().order_by('-created_at'):
            numbers.append(invoice.invoice_number)
            ids.append(invoice.company_id)
            descriptions.append(invoice.description)
            amounts.append(invoice.amount)
            types.append(invoice.type)
            timestamps.append(invoice.created_at)
        attributes_list =zip(numbers,ids, descriptions, amounts, types,timestamps)
        return attributes_list

