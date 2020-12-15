import random
from django.db import transaction
from django.core.management.base import BaseCommand

from companies.models import Company
from invoices.models import Invoice
from contacts.models import Contact

from .factories import (ContactFactory, CompanyFactory, InvoiceFactory)

NUM_CONTACTS = 100
NUM_COMPANIES = 100
NUM_INVOICES = 250

class Command(BaseCommand):
    help = "Generate test data"
    
    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write('Deleting ald data')
        models = [Company, Contact, Invoice]
        for m in models :
            m.objects.all().delete()
        self.stdout.write('creating new data')

        contacts = []
        for _ in range(NUM_CONTACTS):
            contact = ContactFactory()
            contacts.append(contact)

        companies = []
        for _ in range(NUM_COMPANIES):
            company = CompanyFactory()
            companies.append(company)
        
        invoices = []
        for _ in range(NUM_INVOICES):
            invoice = InvoiceFactory()
            invoices.append(invoice)

