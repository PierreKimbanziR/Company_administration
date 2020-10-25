from django.urls import path
from .views import add_contact, get_contacts
from companies.views import home_view

urlpatterns =[
    path('add-contact/', add_contact, name='add-contact'),
    path('show-contacts/', get_contacts, name='show-contacts'),
    path('', home_view, name='company-home')
]