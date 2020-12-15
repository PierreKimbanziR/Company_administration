# Generated by Django 3.1.2 on 2020-12-15 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
        ('companies', '0002_company_person_of_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='Person_of_contact',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='contacts.contact'),
        ),
    ]