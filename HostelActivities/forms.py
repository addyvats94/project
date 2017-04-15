from django import forms
from django.contrib.auth import get_user_model

user=get_user_model()

class LoginForm(forms.Form):
	username=forms.CharField()
	email=forms.EmailField() 
	password=forms.CharField(widget=forms.PasswordInput)

class RegisterForm(forms.Form):
	username=forms.CharField()
	# if user.objects.filter(username=username).exists():
	# 	raise ValidationError("Username %s already exists"%(username))
	email=forms.EmailField()
	password=forms.CharField(widget=forms.PasswordInput)
	password2=forms.CharField(widget=forms.PasswordInput)

	def clean_username(self):
		username=self.cleaned_data['username']
		return username
	
	def clean(self):
		cleaned_data=super(RegisterForm,self).clean()
		
		password=cleaned_data.get("password")
		password2=cleaned_data.get("password2")
		if password != password2:
			self._errors["password2"]=self.error_class(["password2 does not match password"])				
		
		return cleaned_data
