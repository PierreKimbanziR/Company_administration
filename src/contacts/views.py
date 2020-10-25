from django.shortcuts import render, redirect
from .forms import AddContactForm
from .models import Contact

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

def get_contacts(request):

    contacts_datas = Contact().get_contacts()

    context ={
        'contacts_datas':contacts_datas
    }

    return render(request, 'contacts/show_contacts.html', context)




