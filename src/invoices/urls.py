from django.urls import path
from .views import add_invoice, get_invoices

urlpatterns = [
    path('add-invoice', add_invoice, name='add-invoice' ),
    path('show-invoices', get_invoices, name='show-invoices')
]
