# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import AddInvoiceForm

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

