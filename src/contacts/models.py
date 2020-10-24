from django.db import models
from companies import models as companies_model

class Contact(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    working_at = models.ForeignKey(companies_model.Company, on_delete=models.CASCADE, default=None)
    telephone = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.first_name}  {self.last_name} ')