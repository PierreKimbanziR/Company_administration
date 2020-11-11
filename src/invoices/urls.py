from django.urls import path
from .views import AddInvoice, InvoiceDetailView, InvoiceListView, InvoiceUpdateView

urlpatterns = [
   path('add-invoices/', AddInvoice.as_view(), name="add-invoices"),
   path('show-invoices/', InvoiceListView.as_view(), name="show-invoices"),
   path('invoice/<int:pk>/detail/', InvoiceDetailView.as_view(), name="detail-invoice"),
   path('invoice/<int:pk>/update/', InvoiceUpdateView.as_view(), name="update-invoice"),
   ]
