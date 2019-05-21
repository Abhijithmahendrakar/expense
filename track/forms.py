from django import forms
from . models import NewItem
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

#ThisForm is for the item addition
class NewItemModelForm(forms.ModelForm):
	class Meta:
		model = NewItem
		fields = ('name', 'price', 'image')

#ThisForm is for the User Registration
class SignUpForm(UserCreationForm):
		email = forms.EmailField(max_length = 254, help_text = 'Enter a valid Email address.')
		password = forms.CharField(widget = forms.PasswordInput, help_text = 'MIN 8 chars,should include special char,alpha-numeric char')

		class Meta:
			model = User
			fields = ('Username', 'Email', 'Password', 'Password1')	
