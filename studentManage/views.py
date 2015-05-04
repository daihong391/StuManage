from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import loginForm

# Create your views here.
def mainpage(request):
	#if the HTTP method is 'POST'
	if request.method=='POST':

		#redirect to Login Page(student or teacher)
		form=loginForm()
		return render_to_response('MainPage.html', {'form':form},context_instance=RequestContext(request))

	form=loginForm()
	return render_to_response('MainPage.html', {'form':form},context_instance=RequestContext(request))
