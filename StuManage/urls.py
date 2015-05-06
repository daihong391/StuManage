from django.conf.urls import patterns, include, url
from django.contrib import admin
from studentManage.views import mainpage, changePasswd, addAccount1, addAccount2, addAccount3
import settings,os

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'StuManage.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^mainpage/$', mainpage),
    (r'^changePasswd/$', changePasswd),
    (r'^addAccount1/$', addAccount1),
    (r'^addAccount2/$', addAccount2),
    (r'^addAccount3/$', addAccount3),

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
