# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .models import Company
from django.contrib.auth.mixins import LoginRequiredMixin

from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic import DeleteView

from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse

class AddCompany(LoginRequiredMixin,AjaxFormMixin, CreateView):

    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
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

class CompanyListView(LoginRequiredMixin,ListView):
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Company
    context_object_name = "companies"

class CompanyDetailView(LoginRequiredMixin,DetailView):
    
    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Company
    template_name = "companies/company_detail.html"


class CompanyUpdateView(LoginRequiredMixin,UpdateView):


    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Company
    template_name = "companies/company_update.html"
    fields =["Name", "Country", "Vat_Number", "Role"]
    def get_success_url(self):
        return reverse_lazy('detail-company', kwargs={'pk': self.object.id} )

class CompanyDeleteView(LoginRequiredMixin,DeleteView):

    login_url = reverse_lazy('login')
    redirect_field_name = 'redirect_to'
    model = Company
    success_url = reverse_lazy('show-companies')
    template_name = 'companies/company_list.html'

