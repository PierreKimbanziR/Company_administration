# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Company

from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse

class AddCompany(AjaxFormMixin, CreateView):
    template_name = 'companies/add_company.html'
    model = Company
    fields =["Name", "Country", "Vat_Number", "Role"]
    success_url = reverse_lazy('show-companies')
    labels = {
        "Name": "Company name",
        "Country": "Company country",
        "Vat_Number" :" Tva number",
        "Role" :"Company role"
    }

class CompanyListView(ListView):
    model = Company
    context_object_name = "companies"

class CompanyDetailView(DetailView):
    model = Company
    template_name = "companies/company_detail.html"

class CompanyUpdateView(UpdateView):
    model = Company
    template_name = "companies/company.html"
    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.id})


