from django.shortcuts import render, redirect
from .forms import AddContactForm
from .models import Contact
from django.views.generic. edit import CreateView
from django.views.generic import UpdateView
from django.views.generic.detail import DetailView

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

    template_name='contacts/tables.html'
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
    def  get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contacts"] = Contact.objects.all()
        return context

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
