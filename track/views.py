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

def add_item(request):                      # Add all expenses items
    k=NewItem.objects.aggregate(Sum('price'))   # gets total sum of expenses
    l=json.dumps(k)                          # converts into json string
    p=re.findall("\d+",l)                    #Retrives numerical part from returned string
    item = NewItem.objects.all()
    if request.method == "POST":
        form = ItemModelForm(request.POST,request.FILES)  #request.FILES contains uploaded files
        if form.is_valid():
            # commit=False means the form doesn't save at this time.
            # commit defaults to True which means it normally saves.
            model_instance = form.save(commit=False)
            model_instance.save()
            form = ItemModelForm()
            return HttpResponseRedirect('/item') #redirects to same page after POST
    else:
        form = ItemModelForm()
    return render(request, "track/index.html", {'form': form ,'item':item,'sum':p })

def display(request):                                     #displaying all items
    k = NewItem.objects.aggregate(Sum('price'))
    l = json.dumps(k)
    p = re.findall("\d+", l)
    item = NewItem.objects.all()
    return render(request,"tracker/table.html",{'items':item ,'sum':p})
