# Generated by Django 3.1.2 on 2020-11-11 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_auto_20201028_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('NB', 'Non-Binary'), ('O', 'Other')], default=None, max_length=150),
        ),
    ]
