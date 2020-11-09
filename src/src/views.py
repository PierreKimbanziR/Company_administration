from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from companies.models import Company

def test(request):

    return render(request, 'src/index.html')



