from django import forms
from . models import NewItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#ThisForm is for the item addition
class NewItemModelForm(forms.ModelForm):
	class Meta:
		model = NewItem
		fields = ('name', 'price', 'image')



