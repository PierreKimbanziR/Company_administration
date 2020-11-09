from django.urls import path
from .views import AddContact, ContactsList
from companies.views import home_view


urlpatterns =[
    path('contacts/', AddContact.as_view(), name='show-contacts'),
    path('', ContactsList.as_view(), name='list')
]