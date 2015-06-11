from django.conf.urls import patterns, include, url
from django.contrib import admin
from lovelips.views import HomeView
urlpatterns = patterns('',
    # Examples:
     url(r'^$', HomeView.as_view(), name='index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^login/$', views.login_view,name='login'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^ahp/',include('lovelips.urls')),
)

