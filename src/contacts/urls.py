from django.urls import path
from .views import add_contact
from companies.views import home_view

urlpatterns =[
    path('add-contact/', add_contact, name='add-contact'),
    path('', home_view, name='company-home')
]