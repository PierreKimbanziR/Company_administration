# This project is still in progress

# Company administration

## Overview
This project is a full administration tool made with **Django**. This tool can be used to manage the deifferents operations that service company can encounter.

## Technologies used 

* Python
* Django
* Ajax
* MDBoostrap
* Sqlite

## Details 

The database contains 4 models : Companies (either client or provider), Contact (each company has one person of contact), Invoices (either IN or OUT) and the users. 
To manage the users creation/login/logout I used the django built-in Class Based View (LoginView, LogoutView). As well I used them to manage all of the CRUD operations on the database (CreateView, UpdateView, DetailView, DeleteView, ListView). 
To manage the different forms submission for the with AJAX. 

## User levels

There is two user levels : users and admin user. 
The users can read and update every database object. The admin users can CRUD everything. 

