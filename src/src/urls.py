"""src URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include
from django.contrib import admin
from companies.urls import urlpatterns as companies_urls
from contacts.urls import urlpatterns as contacts_urls
from invoices.urls import urlpatterns as invoices_urls
from users.urls import urlpatterns as users_urls
from .views import test



urlpatterns = [
    path('admin/', admin.site.urls, name="admin-page"),
    path('companies/', include(companies_urls)),
    path('contacts/', include(contacts_urls)),
    path('invoices/', include(invoices_urls)),
    path('', include(users_urls)),
    path('test/', test, name="test"),
]

