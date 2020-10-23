from django.forms import ModelForm
from .model import Company

class AddCompanyForm(ModelForm):

    class Meta:
        model : Company
        fields : ["Name", "Country", "VAT Number", "Role"]