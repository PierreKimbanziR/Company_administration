from django.urls import path
from .views import  AddCompany, CompanyListView, CompanyDetailView, CompanyUpdateView

urlpatterns =[
    path("add-companies/", AddCompany.as_view(), name="add-companies"),
    path("show-companies/", CompanyListView.as_view(), name="show-companies"),
    path("company/<int:pk>/update/", CompanyUpdateView.as_view(), name="update-company"),
    path("company/<int:pk>/detail/", CompanyDetailView.as_view(), name="detail-company")
]
