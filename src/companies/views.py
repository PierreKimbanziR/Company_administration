# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import AddCompanyForm
from .models import Company
from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse

class AddCompany(AjaxFormMixin, CreateView):
    template_name = 'companies/show_companies.html'
    model = Company
    fields =["Name", "Country", "Vat_Number", "Role"]
    success_url = reverse_lazy('show-companies')
    labels = {
        "Name": "Company name",
        "Country": "Company country",
        "Vat_Number" :" Tva number",
        "Role" :"Company role"
    }

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies"] = Company.objects.all()
        return context

