# coding: euc-jp

from django.conf.urls import include, url
from cms import views
from django.contrib import admin
admin.autodiscover()


urlpatterns = [
    # Examples:
    # url(r'^$', 'rokken.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^venture/login/$', 'django.contrib.auth.views.login',{'template_name': 'login.html'}),
    url(r'^venture/logout/$', 'django.contrib.auth.views.logout',
{'template_name': 'logged_out.html'}),
    url(r'^venture/register/$', views.register),
    url(r'^venture/register_done/$', views.register),
    #url(r'^venture/new_user/$', views.new_user),
    #url(r'^venture/(?P<User_id>¥d+)/$', views.userhome),
    #url(r'^venture/(?P<User_id>¥d+)/results/$', views.results),
    url(r'^admin/', include(admin.site.urls)),
]
