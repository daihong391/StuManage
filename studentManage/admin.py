from django.contrib import admin
from studentManage.models import Adminer

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display=('username', 'password')

admin.site.register(Adminer)