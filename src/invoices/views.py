# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import AddInvoiceForm
from .models import Invoice
from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse


class AddInvoice(AjaxFormMixin, CreateView):
    template_name ="invoices/show_invoices.html"
    model = Invoice
    fields = ['invoice_number', 'contact_id', 'company_id', 'description', 'amount', 'type']
    labels = {
        'invoice_number' : 'Invoice number',
        'contact_id':'Contact Person',
        'company_id': 'Company name',
        'descriptions':'Invoice description',
        'amount':'Amount',
        'type':'Type'
        }
    success_url = reverse_lazy('show-invoices')
    invoices_datas = Invoice().get_invoices()

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["invoices"] = Invoice.objects.all()
        return context