from django import forms

class loginForm(forms.Form):
	username=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'email', 'style': 'margin-left: 20px; margin-bottom: 5px; display: block; width: 200px; height: 20px;'}))
	passwd=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password', 'style': 'margin-left: 20px; display: block; width: 200px; height: 20px;'}))