from django.forms import ModelForm
from .models import Invoice

class AddInvoiceForm(ModelForm):

    class Meta:
        model = Invoice
        fields = ['invoice_number', 'contact_id', 'company_id', 'description', 'amount', 'type']
        labels = {
        'invoice_number' : 'Invoice number',
        'contact_id':'Contact Person',
        'company_id': 'Company name',
        'descriptions':'Invoice description',
        'amount':'Amount',
        'type':'Type'
        }