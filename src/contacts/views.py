from django.shortcuts import render, redirect
from .forms import AddContactForm
from .models import Contact
from django.views.generic. edit import CreateView
from django.views.generic.dates import ArchiveIndexView
from src.mixins import  AjaxFormMixin
from django.urls import reverse_lazy, reverse




# def add_contact(request):
#     if request.method == "POST":
#         form = AddContactForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('company-home')
#     else:
#         form = AddContactForm()

#     context = {
#         "form" : form
#     }
#     return render(request, 'contacts/add_contact.html', context)

class AddContact(AjaxFormMixin, CreateView):

    template_name='contacts/show_contacts.html'
    model = Contact
    fields = ["first_name", "last_name", "working_at", "telephone", "email"]
    contacts_datas = Contact().get_contacts()
    success_url = reverse_lazy('company-home')

    labels  = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "working_at": "Working at",
            "telephone" : "Telephone Number",
            "email" : "Email adress"
            }
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts_datas"] = self.contacts_datas
        return context


class ContactsList(ArchiveIndexView):
    
    model = Contact
    paginate_by = 5
    date_field = "created_at"
    context_object_name = "last_contacts"



