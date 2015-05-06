from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import loginForm
from studentManage.models import Adminer,Course
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

			#obtain all the courses name
			courseList=[]
			courses=Course.objects.all().values_list('courseName', flat=True)
			for course in courses:
				courseList.append(course)
			course_list=simplejson.dumps(courseList)

			if Adminer.objects.filter(username=username):
				if Adminer.objects.filter(password=passwd):
					return render_to_response('adminPage.html', {'username':username, 'courseList':course_list},context_instance=RequestContext(request))

	form=loginForm()
	return render_to_response('MainPage.html', {'form':form},context_instance=RequestContext(request))

# Change Administer password
def changePasswd(request):
	username=request.POST.get('username')
	orgPasswd=request.POST.get('originPasswd')
	newPasswd=request.POST.get('newpasswd1')
	MESSAGE=''
	if Adminer.objects.filter(username=username):
		if Adminer.objects.filter(password=orgPasswd):
			p=Adminer.objects.get(username=username)
			p.password=newPasswd
			p.save()
			MESSAGE='Password Changed'
		else:
			MESSAGE='Wrong Password'

	return render_to_response('adminPage.html', {'MESSAGE':MESSAGE, 'username':username},context_instance=RequestContext(request))

#add account for administer
def addAccount(request):
	administerName=request.POST.get('administerName')
	newPassword=request.POST.get('newPassword11')
	username=request.POST.get('username')
	MESSAGE=''
	#add account
	if Adminer.objects.filter(username=administerName).count()==0:
		p=Adminer(username=administerName, password=newPassword)
		p.save()
		MESSAGE='Account Creating'
	else:
		MESSAGE='Username existed'

	return render_to_response('adminPage.html', {'MESSAGE':MESSAGE, 'username':username},context_instance=RequestContext(request))
