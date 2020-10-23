from django.urls import path
from .views import home_view, add_company

urlpatterns =[
    path('', home_view, name="company-home"),
    path('add-company/', add_company, name="add-company")
]
