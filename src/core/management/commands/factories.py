import factory
from factory.django import DjangoModelFactory

from companies.models import Company
from invoices.models import Invoice
from contacts.models import Contact


class ContactFactory(DjangoModelFactory):
    class Meta:
        model = Contact

    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    gender = factory.Faker('random_element', elements=[x[0] for x in Contact.gender_choices])
    working_at = factory.SubFactory('core.management.commands.factories.CompanyFactory')
    telephone = factory.Faker('phone_number')
    email = factory.Faker('email')
    created_at = factory.Faker('date_time_this_month')

class CompanyFactory(DjangoModelFactory):
    class Meta: 
        model = Company

    Name = factory.Faker('company')
    Country = factory.Faker('country')
    Person_of_contact = factory.SubFactory(ContactFactory)
    Vat_Number = factory.Faker('ean8')
    Role = factory.Faker('random_element', elements=[x[0] for x in Company.roles])
    created_at = factory.Faker('date_time_this_month')

class InvoiceFactory(DjangoModelFactory):

    class  Meta:
        model = Invoice
    
    invoice_number = factory.Faker('ean13')
    contact_id = factory.SubFactory(ContactFactory)
    company_id = factory.SubFactory(CompanyFactory)
    description = factory.Faker('bs')
    amount = factory.Faker('ean8')
    type = factory.Faker('random_element', elements=[x[0] for x in Invoice.invoice_types])
    created_at = factory.Faker('date_time_this_month')