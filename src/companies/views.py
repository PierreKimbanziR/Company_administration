# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import AddCompanyForm
from .models import Company
from django.views.generic. edit import CreateView
from django.views.generic.dates import ArchiveIndexView
from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse



def add_company(request):

    if request.method == "POST":
        form = AddCompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("company-home")
    else:
        form = AddCompanyForm()

    context = {"form": form}
    return render(request, "companies/add_company.html", context)



def test(request):
    return render(request, "companies/base.html")

class AddCompany(AjaxFormMixin, CreateView):
    template_name = 'companies/show_companies.html'
    model = Company
    fields =["Name", "Country", "Vat_Number", "Role"]
    companies_datas = Company().get_companies()
    success_url = reverse_lazy('company-home')
    labels = {
        "Name": "Company name",
        "Country": "Company country",
        "Vat_Number" :" Tva number",
        "Role" :"Company role"
    }

    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["companies_data"] = self.companies_datas
        return context



def home_view(request):

    return render(request, "companies/home.html")

class CompaniesList(ArchiveIndexView):
    model = Company
    date_field = "created_at"
    context_object_name = "last_companies"
