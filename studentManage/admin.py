from django.contrib import admin
from studentManage.models import Adminer,Course,Teacher,Student

# Register your models here.
class AdminerAdmin(admin.ModelAdmin):
	list_display=('username', 'password',)
	search_fields = ('username', 'password',)

class CourseAdmin(admin.ModelAdmin):
	list_display=('courseName',)
	search_fields=('courseName',)

class StudentAdmin(admin.ModelAdmin):
	list_display=('studentId', 'studentName',)
	search_fields=('studentId', 'studentName',)

class TeacherAdmin(admin.ModelAdmin):
	list_display=('teacherId', 'teacherName',)
	search_fields=('teacherId', 'teacherName',)

admin.site.register(Adminer, AdminerAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)