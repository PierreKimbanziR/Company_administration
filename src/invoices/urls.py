from django.urls import path
from .views import add_invoice

urlpatterns = [
    path('add-invoice', add_invoice, name='add-invoice' )
]
