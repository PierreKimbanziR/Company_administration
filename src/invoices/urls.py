from django.urls import path
from .views import AddInvoice

urlpatterns = [
   path('show-invoices/', AddInvoice.as_view(), name="show-invoices"),
   ]
