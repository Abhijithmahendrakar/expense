from django.test import TestCase, LiveServerTestCase
from track.models import NewItem
from django.utils import timezone
from track.forms import *
import datetime
from django.test import Client
from django.shortcuts import render,redirect,reverse
from django.test import TestCase, LiveServerTestCase
from track.models import NewItem
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import os,time

# testing Views by checking response with status code
class NewItemViewTests(TestCase): 
    def test_signup(self):     #signup page test 
        response = self.client.get("http://127.0.0.1:8000/signup/")
        self.assertEqual(response.status_code, 200)

    #displaying items test    
    def test_display(self):     
        response = self.client.get("http://127.0.0.1:8000/display/")
        self.assertEqual(response.status_code, 200)

    #sorting name test
    def test_sortname(self):    
        response = self.client.get("http://127.0.0.1:8000/sortname/")
        self.assertEqual(response.status_code, 200)

    #sort price test
    def test_sortprice(self):   
        response = self.client.get("http://127.0.0.1:8000/sortprice/")
        self.assertEqual(response.status_code, 200)

    def test_sdate(self):
        response = self.client.get("http://127.0.0.1:8000/sortdate/")
        self.assertEqual(response.status_code, 200)

    #on form submission test
    def test_login(self):        
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/login/',{'username': "ananth", 'password': "1234zxcv"})
        self.assertNotEquals(response.status_code, 302)

    #logout page test
    def test_logout(self):       
        p=Client()
        response = p.post('http://127.0.0.1:8000/accounts/logout/')
        response = p.get('/accounts/logout', follow=True)
        self.assertEqual(response.status_code, 200)

#testing models by creating an instance
class NewItemModelTest(TestCase):    
    def create_item(self,name="television",price=1200):
        return NewItem.objects.create(name=name,price=price,created_at=timezone.now())

#Testing forms both Userform
class UserFormTest(TestCase):      
	#testing validation
    def test_valid_form(self):     
        w = NewItem.objects.create(name='bike', price=10000)
        data = {'username':"abhijithms", 'email':"abhijithms@gmail.com",'password1':"qaz12xwscv",'password2':"qaz12xwscv"}
        form = SignUpForm(data=data)
        self.assertTrue(form.is_valid())

    #invalid form testing using false details    
    def test_invalid_form(self):   
        w = NewItem.objects.create(name='bike', price=10000)
        data = {'username': "abhijithms", 'email': "abhijithms@gmail.com", 'password1': "qaz11xwsc", 'password2': "qaz11xwscv"}
        form = SignUpForm(data=data)
        self.assertFalse(form.is_valid())

#testing Item form
class NewItemModelFormTest(TestCase):  

    def test_valid_form(self):
        w = NewItem.objects.create(name='bike', price=10000,image='images/bicycle.png')
        data = {'name':"Bike",'price':10000}
        form = NewItemModelForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        w = NewItem.objects.create(name='bike', price=10000)
        data = {'name': "Bike",}
        form = NewItemModelForm(data=data)
        self.assertFalse(form.is_valid())

#change the values of usename , password, email everytime you test here and in line no: 140 
class EndtoEndTest(LiveServerTestCase): #End to End testing using Selenium
    username = "newramesh"                   #sample name
    email = "ramesh@gmail.com"            #email
    password = "sriram123"             #and password

    driver = webdriver.Chrome('C:\\Users\\abhi\\Desktop\\proj\\chromedriver') #load chrome driver from local system

    driver.get('http://127.0.0.1:8000/signup/') #Local host

    assert "Signup" in driver.title

    elem = driver.find_element_by_id("id_username") #finds elements by id and enter the data
    elem.send_keys(username)

    elem = driver.find_element_by_id("id_email")
    elem.send_keys(email)

    elem = driver.find_element_by_id("id_password1")
    elem.send_keys(password)

    elem = driver.find_element_by_id("id_password2")
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)                     #Press enter key

    elem = driver.find_element_by_id("id_name")     #add items page , enter the credentials
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/tv.png") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element_by_id("id_name")
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/tv.png") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    elem = driver.find_element_by_id("id_name")
    elem.send_keys("television")
    elem = driver.find_element_by_id("id_price")
    elem.send_keys(1000)
    driver.find_element_by_id("id_image").send_keys(os.getcwd() + "/tv.png") #give path to image from root during testing
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button2').click() #verify all filters
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button5').click()
    time.sleep(2)
    driver.find_element_by_css_selector('.button.button5').click()
    link = driver.find_element_by_link_text('Logout')
    time.sleep(2)
    link.click()
    link = driver.find_element_by_link_text('Login') #testing login page using creditials from Signup
    link.click()
    elem = driver.find_element_by_id("id_username") 
    elem.send_keys(username) 
    elem = driver.find_element_by_id("id_password")
    elem.send_keys(password)
    time.sleep(1)
    elem.send_keys(Keys.RETURN)
    driver.close() #Closes the Chrome browser