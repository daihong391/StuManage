from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import loginForm
from studentManage.models import Adminer,Course,Teacher,Student
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

			#obtain all administer
			adminList=[]
			adminers=Adminer.objects.all().values_list('username', flat=True)
			for adminer in adminers:
				adminList.append(adminer)
			adminer_list=simplejson.dumps(adminList)

			#obtain all teacher
			teacherList=[]
			teachers=Teacher.objects.all().values_list('teacherId', flat=True)
			for teacher in teachers:
				teacherList.append(teacher)
			teacher_list=simplejson.dumps(teacherList)

			#obtain all student
			studentList=[]
			students=Student.objects.all().values_list('studentId', flat=True)
			for student in students:
				studentList.append(student)
			student_list=simplejson.dumps(studentList)

			if Adminer.objects.filter(username=username):
				if Adminer.objects.filter(password=passwd):
					return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

	form=loginForm()
	return render_to_response('MainPage.html', {'form':form},context_instance=RequestContext(request))

# Change Administer password
def changePasswd(request):
	username=request.POST.get('username')
	orgPasswd=request.POST.get('originPasswd')
	newPasswd=request.POST.get('newpasswd1')
	MESSAGE=''

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	if Adminer.objects.filter(username=username):
		if Adminer.objects.filter(password=orgPasswd):
			p=Adminer.objects.get(username=username)
			p.password=newPasswd
			p.save()
			MESSAGE='Password Changed'
		else:
			MESSAGE='Wrong Password'

	return render_to_response('adminPage.html', {'MESSAGE':MESSAGE, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#add account for administer
def addAccount1(request):
	administerName=request.POST.get('administerName')
	newPassword=request.POST.get('newPassword11')
	username=request.POST.get('username')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	MESSAGE=''
	#add account
	if Adminer.objects.filter(username=administerName).count()==0:
		p=Adminer(username=administerName, password=newPassword)
		p.save()
		MESSAGE='Account Creating'
	else:
		MESSAGE='Username existed'

	return render_to_response('adminPage.html', {'MESSAGE1':MESSAGE, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#add account for teacher
def addAccount2(request):
	teacherId=request.POST.get('TeacherId')
	teacherName=request.POST.get('TeacherName')
	courseName=request.POST.get('courseName')
	teacherPassword=request.POST.get('teacherPassword')
	username=request.POST.get('username')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	courseSelect=Course.objects.all().get(courseName=courseName)
	MESSAGE=''
	#add account
	if Teacher.objects.filter(teacherId=teacherId).count()==0:
		p=Teacher(teacherId=teacherId, teacherName=teacherName, course=courseSelect, teacherPassword=teacherPassword)
		p.save()
		MESSAGE='Account Creating'
	else:
		MESSAGE='Username existed'

	return render_to_response('adminPage.html', {'MESSAGE2':MESSAGE, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#add account for student
def addAccount3(request):
	studentId=request.POST.get('studentId')
	studentName=request.POST.get('studentName')
	courseName=request.POST.get('courseName')
	studentPassword=request.POST.get('studentPassword')
	username=request.POST.get('username')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	courseSelect=Course.objects.all().get(courseName=courseName)
	MESSAGE=''
	#add account
	if Student.objects.filter(studentId=studentId).count()==0:
		p=Student(studentId=studentId, studentName=studentName, course=courseSelect, studentPassword=studentPassword)
		p.save()
		MESSAGE='Account Creating'
	else:
		MESSAGE='Username existed'

	return render_to_response('adminPage.html', {'MESSAGE3':MESSAGE, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#modify password for administer
def modifyPassword1(request):
	username=request.POST.get('user1')
	newPassword=request.POST.get('pass11')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	if Adminer.objects.filter(username=username):
		p=Adminer.objects.get(username=username)
		p.password=newPassword
		p.save()

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#modify password for teacher
def modifyPassword2(request):
	username=request.POST.get('user2')
	newPassword=request.POST.get('pass21')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	if Teacher.objects.filter(teacherId=username):
		p=Teacher.objects.get(teacherId=username)
		p.teacherPassword=newPassword
		p.save()

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#modify password for student
def modifyPassword3(request):
	username=request.POST.get('user3')
	newPassword=request.POST.get('pass31')

	#obtain all the courses name
	courseList=[]
	courses=Course.objects.all().values_list('courseName', flat=True)
	for course in courses:
		courseList.append(course)
	course_list=simplejson.dumps(courseList)

	#obtain all administer
	adminList=[]
	adminers=Adminer.objects.all().values_list('username', flat=True)
	for adminer in adminers:
		adminList.append(adminer)
	adminer_list=simplejson.dumps(adminList)

	#obtain all teacher
	teacherList=[]
	teachers=Teacher.objects.all().values_list('teacherId', flat=True)
	for teacher in teachers:
		teacherList.append(teacher)
	teacher_list=simplejson.dumps(teacherList)

	#obtain all student
	studentList=[]
	students=Student.objects.all().values_list('studentId', flat=True)
	for student in students:
		studentList.append(student)
	student_list=simplejson.dumps(studentList)

	if Student.objects.filter(studentId=username):
		p=Student.objects.get(studentId=username)
		p.studentPassword=newPassword
		p.save()

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))
