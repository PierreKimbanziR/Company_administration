from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):

    gender_choices = [ ('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary'), ('O', 'Other')]

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    gender = models.CharField(max_length=150, choices=gender_choices, default=None,  null=True)
    working_at = models.OneToOneField('companies.Company', on_delete=models.CASCADE, null=True)
    telephone = PhoneNumberField(unique=True)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.first_name}  {self.last_name} ')
