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