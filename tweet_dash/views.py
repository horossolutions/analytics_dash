from django.shortcuts import render
from .forms import TweetHandleForm

def home(request):
	context = { 'form': TweetHandleForm}
	return render(request, 'index.html', context)

def tweet_dash(request):
	return render(request,'tweet_dash.html')