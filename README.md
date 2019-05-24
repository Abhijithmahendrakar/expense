# Expense Tracker
## Overview
Expense tracker is an open source, simple web application with features to maintain the daily/monthly expenses of an user.
This is designed and implemented using **Django** framework with python as scripting language and front-end tools
like **HTML** and **CSS**.  
The app includes unit testing and end-to-end testing.

## Setup Tools Required
- [Python](https://www.python.org/downloads/) == 3.6.3
- [Pip](https://pip.pypa.io/en/stable/installing/) required
- Download the repository and 
  `clone to your desktop or to any folder`.
  
## Features  
- The user is provided with **Login**, **Signup** page.
- **CRUD** operations
- Filtering and Sorting by name, price and created date.
- The user will be able to see the list of expenses along with **total expense**.

# Installation Guide
- Create `virtualenv` and activate the `Scripts`.
- Go to the `folder` where u downloaded the `repository` using `commond prompt`
- Install **Django==2.0** using `pip install django=2.0`
- Install all the dependencies using `pip install -r requirements.txt`

## To run and use the app
After setup and installation use these cmds in commond prompt within the `root directory`
- then enter `python manage.py runserver`
- Create Database tables `python manage.py migrate` 
- `python manage.py makemigrations`(used to save changes)
- CreateSuperUser using `python manage.py createsuperuser` and give your name and email.
- Open **Web browser** and enter the **URL** as `http://127.0.0.1:8000/signup`
The app starts to run on your localserver and use it.

## URLs 
- `http://127.0.0.1:8000/accounts/login`
- `http://127.0.0.1:8000/accounts/logout`
- `http://127.0.0.1:8000/sortname`
- `http://127.0.0.1:8000/sortprice`
- `http://127.0.0.1:8000/sortdate`
- `http://127.0.0.1:8000/item`
- `http://127.0.0.1:8000/display`

# Testing
The end-to-end testing is done by the following

check the version of your **google browser** and then

Download [ChromeDriver](http://chromedriver.chromium.org/downloads) for python-testing in google chrome , and copy its absolute path in **EndToEndTest** function line no:89 in **tests.py**.

if not installed using `requirements.txt` then use 
(install Selenium using `pip install selenium`

install Django-nose `using pip install django-nose`

install coverage using `pip install coverage`)

move to .../track/tests.py and under **def EndToEndTest():** edit the **username ,password ,email** as mentioned in the script

To **Test the app** , move to root directory of the project and runserver using `python manage.py runserver` then

open **another command prompt** , move to root directory and run `python manage.py test track` to test the app.
