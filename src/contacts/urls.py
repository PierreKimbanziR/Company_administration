from django.urls import path
from .views import AddContact, ContactUpdateView, ContactDetailView



urlpatterns =[
    path('show-contacts/', AddContact.as_view(), name='show-contacts'),
    path('contact/<int:pk>/update', ContactUpdateView.as_view(), name='update-contact'),
    path('contact/<int:pk>/detail', ContactDetailView.as_view(), name='detail-contact')
]