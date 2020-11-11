import factory
from factory.django import DjangoModelFactory

from companies.models import Company

class CompanyFactory(DjangoModelFactory):
    class Meta: 
        model = Company

    Name = factory.Faker('first_name')
    Country = factory.Faker()
    last_name = factory.Faker('last_name')
