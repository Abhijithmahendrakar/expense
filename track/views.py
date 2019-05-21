from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect,reverse
from django.http import HttpResponse,HttpResponseRedirect
from . forms import NewItemModelForm
from . models import NewItem
from django.db.models import Sum
from django.contrib.auth import autenticate,login
from .forms import SignUpForm
import re,json

# Create your views here.
#View for signing up using custom inbuilt UserCreationForm
def signup(request):        
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        #Checking for form validation and retriving username,pass from POST data
        if form.is_valid():                
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            #User is logged in
            login(request, user)          
            return HttpResponseRedirect('/item')
    else:
        form = SignUpForm()               #IF not logged in then Show empty form
    return render(request, 'registration/signup.html', {'form': form})