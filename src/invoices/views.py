# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import AddInvoiceForm
from .models import Invoice
from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView

from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse


class AddInvoice(AjaxFormMixin, CreateView):
    template_name ="invoices/add_invoice.html"
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

class InvoiceListView(ListView):
    model = Invoice
    template_name = "invoices/invoice_list.html"
    context_object_name = 'invoices'

class InvoiceUpdateView(UpdateView):
    model = Invoice
    template_name = "invoices/invoice_update.html"
    def get_success_url(self):
        return reverse_lazy('detail-invoice', kwargs={'pk': self.object.id})


class InvoiceDetailView(DetailView):
    model = Invoice
    template_name = "invoices/invoice_detail.html"



class InvoiceDeleteView(DeleteView):
    model = Invoice
    template_name = "invoices/invoice_list.html"
    success_url = reverse_lazy('show-invoices')
