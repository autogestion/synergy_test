from django import forms

class SynergyUserForm(forms.Form):
	username = forms.CharField(max_length=200)
	email = forms.EmailField()
	phone = forms.CharField(max_length=40)
