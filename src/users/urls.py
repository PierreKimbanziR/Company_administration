from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import add_user, HomepageListView

urlpatterns =[
    path('login/', auth_views.LoginView.as_view(template_name ='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('', HomepageListView.as_view(), name='users-homepage'),
    path('add-user/', add_user, name='add-user')
]