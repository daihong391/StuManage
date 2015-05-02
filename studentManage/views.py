from django.shortcuts import render
from django.shortcuts import render_to_response

# Create your views here.
def mainpage(request):
	#if the HTTP method is 'POST'
	if request.method=='POST':

		#redirect to Login Page(student or teacher)
		return render_to_response('MainPage.html')

	return render_to_response('MainPage.html')
