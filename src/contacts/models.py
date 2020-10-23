from django.db import models

class Contact(models.Model):

    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    telephone = models.IntegerField()
    email = models.EmailField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (f'{self.first_name}  {self.last_name}')