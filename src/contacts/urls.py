from django.urls import path
from .views import AddContact



urlpatterns =[
    path('show-contacts/', AddContact.as_view(), name='show-contacts')
]