from django.shortcuts import render, redirect
from .forms import AddContactForm
from .models import Contact
from django.views.generic. edit import CreateView
from django.views.generic.list import ListView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

from src.mixins import  AjaxFormMixin

from django.urls import reverse_lazy, reverse

class AddContact(AjaxFormMixin, CreateView):

    template_name='contacts/add_contact.html'
    model = Contact
    fields = ["first_name", "last_name", "working_at", "telephone", "email"]
    success_url = reverse_lazy('show-contacts')

    labels  = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "working_at": "Working at",
            "telephone" : "Telephone Number",
            "email" : "Email adress"
            }

class ContactListView(ListView):
    model = Contact
    context_object_name = "contacts"

class ContactDetailView(DetailView):
    model = Contact
    template_name = "contacts/contact_detail.html"
    fields = ["first_name", "last_name", "working_at", "telephone", "email", "created_at"]

class ContactUpdateView(UpdateView):
    model = Contact
    template_name = "contacts/contact_update.html"
    fields = ["first_name", "last_name", "working_at", "telephone", "email"]
    labels  = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "working_at": "Working at",
            "telephone" : "Telephone Number",
            "email" : "Email adress"
            }
    def get_success_url(self):
        return reverse_lazy('detail-contact', kwargs={'pk': self.object.id})
