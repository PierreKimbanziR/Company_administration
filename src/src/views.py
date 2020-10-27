from django.shortcuts import render, redirect

def test(request):

    return render(request, 'src/index.html')