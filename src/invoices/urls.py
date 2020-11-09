from django.urls import path
from .views import AddInvoice, InvoicesList

urlpatterns = [
   path('show-invoices/', AddInvoice.as_view(), name="show-invoices"),
   path('', InvoicesList.as_view(), name="invoices-list")]
