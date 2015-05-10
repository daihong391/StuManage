from django.shortcuts import render_to_response
from django.template import RequestContext
from .forms import loginForm,userLoginForm
from studentManage.models import Adminer,Course,Teacher,Student
from django.db.models import Count,Q
import json as simplejson

def studentModify(request):
	studentId=request.POST.get('studentId')
	studentName=request.POST.get('studentName')
	studentPassword=request.POST.get('studentPassword')
	courseName=request.POST.get('courseName')[7:]

	p=Student.objects.get(studentId=studentId)
	p.studentName=studentName
	p.studentPassword=studentPassword
	course=Course.objects.get(courseName=courseName)
	p.course=course
	p.save()


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

	student=Student.objects.get(studentId=studentId)

	return render_to_response('studentPage.html', {'student':student, 'username':studentId, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))


def teacherModify(request):
	teacherId=request.POST.get('teacherId')
	teacherName=request.POST.get('teacherName')
	teacherPassword=request.POST.get('teacherPassword')
	courseName=request.POST.get('courseName')[7:]

	p=Teacher.objects.get(teacherId=teacherId)
	p.teacherName=teacherName
	p.teacherPassword=teacherPassword
	course=Course.objects.get(courseName=courseName)
	p.course=course
	p.save()


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

	teacher=Teacher.objects.get(teacherId=teacherId)

	return render_to_response('teacherPage.html', {'teacher':teacher, 'username':teacherId, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))


def mainpage1(request):
	if request.method=='POST':
		form1=userLoginForm(request.POST)

		if form1.is_valid():
			rank=form1.cleaned_data['rank']
			username=form1.cleaned_data['username']
			passwd=form1.cleaned_data['passwd']

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

			if rank=='0':
				if Teacher.objects.filter(teacherId=username):
					if Teacher.objects.filter(teacherPassword=passwd):
						teacher=Teacher.objects.get(teacherId=username)
						return render_to_response('teacherPage.html', {'teacher':teacher, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))
			else:
				if Student.objects.filter(studentId=username):
					if Student.objects.filter(studentPassword=passwd):
						student=Student.objects.get(studentId=username)
						return render_to_response('studentPage.html', {'student':student, 'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

	form=loginForm()
	form1=userLoginForm()
	return render_to_response('MainPage.html', {'form':form, 'form1':form1},context_instance=RequestContext(request))

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
	form1=userLoginForm()
	return render_to_response('MainPage.html', {'form':form, 'form1':form1},context_instance=RequestContext(request))

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
	username=request.POST.get('username')
	user1=request.POST.get('user1')
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

	if Adminer.objects.filter(username=user1):
		p=Adminer.objects.get(username=user1)
		p.password=newPassword
		p.save()

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#modify password for teacher
def modifyPassword2(request):
	username=request.POST.get('username')
	user2=request.POST.get('user2')
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

	if Teacher.objects.filter(teacherId=user2):
		p=Teacher.objects.get(teacherId=user2)
		p.teacherPassword=newPassword
		p.save()

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

#modify password for student
def modifyPassword3(request):
	username=request.POST.get('username')
	user3=request.POST.get('user3')
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

# delete administer account
def deleteAdmin(request):
	username=request.POST.get('username')
	adminName=request.POST.get('user1')

	if username != adminName:
		p=Adminer.objects.get(username=adminName)
		p.delete()

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

# delete teacher account
def deleteTeacher(request):
	username=request.POST.get('username')
	teacherName=request.POST.get('user2')

	p=Teacher.objects.get(teacherId=teacherName)
	p.delete()

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

# delete student account
def deleteStudent(request):
	username=request.POST.get('username')
	studentName=request.POST.get('user3')

	p=Student.objects.get(studentId=studentName)
	p.delete()

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

# modify courses: add course
def modifyCourse1(request):
	username=request.POST.get('username')
	courseName=request.POST.get('courseName')
	MESSAGE=''

	if Course.objects.filter(courseName=courseName).count()==0:
		courseCredit=request.POST.get('courseCredit')
		courseHour=request.POST.get('courseHour')
		courseStart=request.POST.get('courseStart')
		coursePeople=request.POST.get('coursePeople')
		p=Course(courseName=courseName, courseCredit=courseCredit, courseHour=courseHour, courseStart=courseStart, coursePeople=coursePeople)
		p.save()
		MESSAGE='add successful'
	else:
		MESSAGE='fail'

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

	return render_to_response('adminPage.html', {'MESSAGE1':MESSAGE,'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))

# modify courses: show course
def modifyCourse2(request):
	courseName=request.POST.get('courseName')
	username=request.POST.get('username')

	p=Course.objects.all().get(courseName=courseName)

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list, 'course':p},context_instance=RequestContext(request))

#modify courses: modify course
def modifyCourse21(request):
	username=request.POST.get('username')
	courseName=request.POST.get('courseName')
	courseCredit=request.POST.get('courseCredit')
	courseHour=request.POST.get('courseHour')
	courseStart=request.POST.get('courseStart')
	coursePeople=request.POST.get('coursePeople')

	p=Course.objects.all().get(courseName=courseName)
	p.courseCredit=courseCredit
	p.courseHour=courseHour
	p.courseStart=courseStart
	p.coursePeople=coursePeople
	p.save()

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list, 'course':p},context_instance=RequestContext(request))

#modify courses: delete course
def deleteCourse(request):
	username=request.POST.get('username')
	courseName=request.POST.get('courseName')
	p=Course.objects.all().get(courseName=courseName)
	p.delete()

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

	return render_to_response('adminPage.html', {'username':username, 'courseList':course_list, 'adminerList':adminer_list, 'teacherList':teacher_list, 'studentList':student_list},context_instance=RequestContext(request))
