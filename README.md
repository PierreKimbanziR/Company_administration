
# Company administration tool

## Overview
This project is a full administration tool made with **Django**. This tool can be used to manage the differents operations a service company can encounter.

## Technologies used 

* Python
* Django
* Ajax
* MDBoostrap
* Sqlite

## Details 

### Database : 
The database contains 4 models : Companies (either client or provider), Contact (each company has one person of contact), Invoices (either IN or OUT) and the users.

### Authentication : 
To manage the users creation/login/logout I used the django built-in Class Based View (LoginView, LogoutView). Users can retrieve their passwords using the email address. An email is sent to them containing a link to reset their password. 

### User levels : 

There is two user levels : users and admin user. 
The users can read and update every database object. The admin users can CRUD everything. 

## Layouts : 
