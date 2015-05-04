from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import loginForm
from studentManage.models import Adminer
from django.db.models import Count,Q
import json as simplejson

# Create your views here.
def mainpage(request):
	#if the HTTP method is 'POST'
	if request.method=='POST':

		#redirect to Login Page(student or teacher)
		form=loginForm(request.POST)
		if form.is_valid():
			username=form.cleaned_data['username']
			passwd=form.cleaned_data['passwd']
			if Adminer.objects.filter(username=username):
				if Adminer.objects.filter(password=passwd):
					return render_to_response('adminPage.html', {'username':username},context_instance=RequestContext(request))

	form=loginForm()
	return render_to_response('MainPage.html', {'form':form},context_instance=RequestContext(request))
