from django.db import models
from django.contrib.auth.models import User,UserManager

# Create your models here.
class Adminer(models.Model):
	username=models.EmailField(max_length=30, default="", unique=True)
	password=models.CharField(max_length=30)

	def __str__(self):
        		return u'%s: %s' % (self.username, self.password)

class Course(models.Model):
	courseName=models.CharField(max_length=50, default="", unique=True)
	courseCredit=models.PositiveIntegerField()
	courseHour=models.PositiveIntegerField()
	courseStart=models.DateTimeField()
	coursePeople=models.PositiveIntegerField(default=0)

	def __str__(self):
		return self.courseName

class Teacher(models.Model):
	teacherId=models.CharField(max_length=30, default="", unique=True)
	teacherName=models.CharField(max_length=30, default="")
	course=models.ForeignKey(Course)
	teacherPassword=models.CharField(max_length=30, default="")

	def __str__(self):
		return "%s: %s" % (self.teacherId, self.teacherName)

class Student(models.Model):
	studentId=models.CharField(max_length=30, default="", unique=True)
	studentName=models.CharField(max_length=30, default="")
	course=models.ForeignKey(Course)
	studentPassword=models.CharField(max_length=30, default="")

	def __str__(self):
		return "%s: %s" % (self.studentId, self.studentName)