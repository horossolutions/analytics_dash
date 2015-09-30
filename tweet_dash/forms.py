from django import forms

class TweetHandleForm(forms.Form):
	inputTweetHandle = forms.CharField(label='Ingrese el nombre de usuario de su cuenta Twitter:', max_length=100)


