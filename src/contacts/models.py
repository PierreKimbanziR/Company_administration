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
    
    def get_contacts(self):
        cfirst_name = []
        clast_name = []
        cworkingat = []
        ctelephone = []
        cemail = []
        ccreatedat=[]

        for contact in Contact.objects.all().order_by('last_name'):
            cfirst_name.append(contact.first_name)
            clast_name.append(contact.last_name)
            cworkingat.append(contact.working_at)
            ctelephone.append(contact.telephone)
            cemail.append(contact.email)
            ccreatedat.append(contact.created_at)
        attribute_list = zip(clast_name, cfirst_name, cworkingat, ctelephone, cemail, ccreatedat)
        return attribute_list