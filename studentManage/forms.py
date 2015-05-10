from django import forms

class loginForm(forms.Form):
	username=forms.EmailField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'email', 'style': 'margin-left: 20px; margin-bottom: 5px; display: block; width: 200px; height: 20px;'}))
	passwd=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password', 'style': 'margin-left: 20px; display: block; width: 200px; height: 20px;'}))

RANK=(
	('0', 'TEACHER'),
	('1', 'STUDENT')
)

class userLoginForm(forms.Form):
	username=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder':'username', 'style': 'margin-left: 20px; margin-bottom: 5px; display: block; width: 200px; height: 20px;'}))
	passwd=forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder':'password', 'style': 'margin-left: 20px; display: block; width: 200px; height: 20px;'}))
	rank=forms.ChoiceField(choices=RANK, required=True)