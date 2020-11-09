from django.urls import path
from .views import  AddCompany

urlpatterns =[
    path("show-companies/", AddCompany.as_view(), name="show-companies")

]
