# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from .forms import AddCompanyForm

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

def home_view(request):

    return render(request, "companies/home.html")