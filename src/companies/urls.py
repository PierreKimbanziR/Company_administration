from django.urls import path
from .views import  AddCompany, CompanyListView, CompanyDetailView, CompanyUpdateView, CompanyDeleteView

urlpatterns =[
    path("add-companies/", AddCompany.as_view(), name="add-companies"),
    path("show-companies/", CompanyListView.as_view(), name="show-companies"),
    path("<int:pk>/update/", CompanyUpdateView.as_view(), name="update-company"),
    path("<int:pk>/detail/", CompanyDetailView.as_view(), name="detail-company"),
    path("<int:pk>/delete/", CompanyDeleteView.as_view(), name='delete-company')
]
