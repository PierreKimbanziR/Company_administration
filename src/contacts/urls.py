from django.urls import path
from .views import AddContact, get_contacts
from companies.views import home_view


urlpatterns =[
    path('show-contacts/', AddContact.as_view(), name='show-contacts'),
    path('', home_view, name='company-home')
]