from django import forms

class loginForm(forms.Form):
	username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'username', 'style':'display: block; margin: 5px; height: 20px; width: 200px;'}))
	passwd=forms.CharField(max_length=30, widget=forms.PasswordInput(attrs={'placeholder':'password', 'style':'display: block; margin-left: 5px; height: 20px; width: 200px'}))