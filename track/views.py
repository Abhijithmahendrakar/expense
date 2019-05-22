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
        form = NewItemModelForm()
    return render(request, "track/index.html", {'form': form ,'item':item,'sum':p })

#displaying all items
def display(request):                                     
    k = NewItem.objects.aggregate(Sum('price'))
    l = json.dumps(k)
    p = re.findall("\d+", l)
    item = NewItem.objects.all()
    return render(request,"track/table.html",{'items':item ,'sum':p})

# Editing submitted data
def update(request,id):                       
    instance = get_object_or_404(NewItem,id=id)
    form = NewItemModelForm(data=request.POST, files=request.FILES, instance=instance) #posted files will be in request.FILES
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context={
        "name":instance.name,
        "price":instance.price,
        "instance":instance,
        "form":form,
    }
    return render(request,"track/update.html",context)

#deleting items by primary key on click    
def delete(request,id):                                    
    deleteitem=get_object_or_404(Item,pk=id).delete()
    return HttpResponseRedirect('/display')

#sorting by name
def sortbyname(request):                                  
    sname=NewItem.objects.order_by('name').all()
    return render(request,"track/sname.html",{'name':sname})
