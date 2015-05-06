from django.contrib import admin
from studentManage.models import Adminer,Course,Teacher,Student

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display=('username', 'password')

admin.site.register(Adminer)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)