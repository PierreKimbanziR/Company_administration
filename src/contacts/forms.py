from django.forms import ModelForm
from .models import Contact

class AddContactForm(ModelForm):

    class Meta:
        model = Contact
        fields = ["first_name", "last_name", "working_at", "telephone", "email"]
        labels  = {
            "first_name" : "First Name",
            "last_name" : "Last Name",
            "working_at": "Working at",
            "telephone" : "Telephone Number",
            "email" : "Email adress"
            }