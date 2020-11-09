from django.urls import path
from .views import home_view, test, AddCompany, CompaniesList

urlpatterns =[
    path('/', home_view, name="company-home"),
    path('table/', test, name="table"), 
    path("show-companies/", AddCompany.as_view(), name="show-companies"),
    path("", CompaniesList.as_view(), name='companies')

]
