from django.shortcuts import render
from .forms import TweetHandleForm

def home(request):
	if request.method == 'POST':
		form = TweetHandleForm(request.POST)
		if form.is_valid():
			print(f.cleaned_data)
			return HttpResponseRedirect('tweet_dash/')
	else:
		form = TweetHandleForm()
	context = {'form': form}
	return render(request, 'index.html', context)

def tweet_dash(request):
	return render(request,'tweet_dash.html')