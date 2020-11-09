# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic.list import ListView
from django.views.generic.dates import ArchiveIndexView

from django.shortcuts import render, redirect
from .forms import UserCreationForm
from companies.models import Company
from invoices.models import Invoice
from contacts.models import Contact

def add_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-home')
    else :
        form = UserCreationForm()

    context = {'form':form}

    return render(request, 'users/add_user.html', context)

class HomepageListView(ListView):
    
    template_name = "users/homepage.html"
    queryset = Company.objects.all().order_by('-created_at')[:5]
    context_object_name = "last_companies"

    def get_context_data(self, **kwargs):
        context = super(HomepageListView, self).get_context_data(**kwargs)
        context["last_contacts"] = Contact.objects.all().order_by('-created_at')[:5]
        context["last_invoices"] = Invoice.objects.all().order_by('-created_at')[:5]

        return context
    

