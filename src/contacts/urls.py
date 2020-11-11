from django.urls import path
from .views import AddContact, ContactUpdateView, ContactDetailView, ContactListView



urlpatterns =[
    path('show-contacts/', ContactListView.as_view(), name='show-contacts'),
    path('add-contact/', AddContact.as_view(), name="add-contacts"),
    path('contact/<int:pk>/update/', ContactUpdateView.as_view(), name='update-contact'),
    path('contact/<int:pk>/detail/', ContactDetailView.as_view(), name='detail-contact')
]