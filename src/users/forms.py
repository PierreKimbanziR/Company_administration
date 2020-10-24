from django.forms import ModelForm
from .models import UserCreation

class UserCreationForm(ModelForm):

    class Meta:
        model = UserCreation
        fields = ['username', 'first_name', 'last_name', 'email']
        labels = {
            'username': 'Username',
            'first_name':'First name',
            'last_name': 'Last name',
            'email': 'Eamil adress'

        }