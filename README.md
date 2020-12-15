
# Company administration tool

## Overview
This project is a full administration tool made with **Django**. This tool can be used to manage the differents operations a service company can encounter.

## Technologies used 

* Python
* Django
* Ajax
* MDBoostrap
* Sqlite

### Useful dependecies I used : 
* [Factory-boy](https://factoryboy.readthedocs.io/en/stable/index.html) : To make test and fill the db with dummy data.
* [django-money](https://github.com/django-money/django-money) : To simply generate currency field inside the models. 
* [django-phonenumber-field](https://github.com/stefanfoulis/django-phonenumber-field) : To create phonenumbers field in teh models.
* [django-widget-tweaks](https://github.com/jazzband/django-widget-tweaks)  : To pass css classes to django form attribute wthout having to modify the python code. 

## Details 

### Database : 
The database contains 4 models : Companies (either client or provider), Contact (each company has one person of contact), Invoices (either IN or OUT) and the users.

### Authentication : 
To manage the users creation/login/logout I used the django built-in Class Based View (LoginView, LogoutView). Users can retrieve their passwords using the email address. An email is sent to them containing a link to reset their password. 

### User levels : 

There is two user levels : users and admin user. 
The users can read and update every database object. The admin users can CRUD everything. 

## Layouts : 
The app is not yet deployed but here are a few screenshots. 

### The homepage with a quick overviex of the last registered entries.
![Homepage](/images/homepage.png)

### The invoices page. It contains an ordered table with a search option. There is also the possibility to choose by which parameter to search in the table. In the last column, there are different buttons to perform operations on the invoice in question (see in details, edit, delete). 

### The page the user lands on when they have submitted their email address to change their password. 
