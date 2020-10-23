from django.shortcuts import render, redirect
from .forms import AddContactForm


def add_contact(request):

    if request.method == "POST":
        form = AddContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company-home')
    else:
        form = AddContactForm()

    context={"form":form}

    return render(request, "contacts/add_contact.html", context)



