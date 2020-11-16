# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic.list import ListView
from django.views.generic.edit import FormView
from django.contrib import messages

from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from companies.models import Company
from invoices.models import Invoice
from contacts.models import Contact


class RegisterView(FormView):
    form_class = UserRegisterForm
    template_name = 'users/register.html'

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return redirect('login')


class HomepageListView(ListView):
    
    template_name = "users/homepage.html"
    queryset = Company.objects.all().order_by('-created_at')[:5]
    context_object_name = "last_companies"

    def get_context_data(self, **kwargs):
        context = super(HomepageListView, self).get_context_data(**kwargs)
        context["last_contacts"] = Contact.objects.all().order_by('-created_at')[:5]
        context["last_invoices"] = Invoice.objects.all().order_by('-created_at')[:5]

        return context
    

