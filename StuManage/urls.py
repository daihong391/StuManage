from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover
from studentManage.views import mainpage, changePasswd, addAccount1, addAccount2, addAccount3, modifyPassword1, modifyPassword2, modifyPassword3, deleteAdmin, deleteTeacher, deleteStudent, modifyCourse1, modifyCourse2, modifyCourse21, deleteCourse
import os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StuManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # (r'^admin/$', include(admin.site.urls)),
    (r'^mainpage/$', mainpage),
    (r'^changePasswd/$', changePasswd),
    (r'^addAccount1/$', addAccount1),
    (r'^addAccount2/$', addAccount2),
    (r'^addAccount3/$', addAccount3),
    (r'^modifyPassword1/$', modifyPassword1),
    (r'^modifyPassword2/$', modifyPassword2),
    (r'^modifyPassword3/$', modifyPassword3),
    (r'^deleteAdmin/$', deleteAdmin),
    (r'^deleteTeacher/$', deleteTeacher),
    (r'^deleteStudent/$', deleteStudent),
    (r'^modifyCourse1/$', modifyCourse1),
    (r'^modifyCourse2/$', modifyCourse2),
    (r'^modifyCourse21/$', modifyCourse21),
    (r'^deleteCourse/$', deleteCourse),

    (r'^css/(?P<path>.*)$','django.views.static.serve',
    	{'document_root': os.path.join(os.path.dirname(__file__),'templates/css').replace('\\','/') }
    	),
    ( r'^images/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': os.path.join(os.path.dirname(__file__),'templates/images').replace('\\','/') }
    ),
    ( r'^js/(?P<path>.*)$', 'django.views.static.serve',
            { 'document_root': os.path.join(os.path.dirname(__file__),'templates/scripts').replace('\\','/') }
    ),

    url(r'^admin/', include(admin.site.urls)),
)
