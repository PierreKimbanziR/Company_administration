# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import AddInvoiceForm
from .models import Invoice

def add_invoice(request):

    if request.method == "POST":
        form = AddInvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-home')
    else :
        form = AddInvoiceForm()

    context ={"form":form}

    return render(request, 'invoices/add_invoice.html', context)

def get_invoices(request):

    invoices_datas = Invoice().get_invoices()
    context = {
        'invoices_datas': invoices_datas
    }

    return render(request, 'invoices/show_invoices.html', context)

