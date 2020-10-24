# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .forms import UserCreationForm

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
