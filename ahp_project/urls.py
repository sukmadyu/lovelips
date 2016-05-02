from django.conf.urls import patterns, include, url
from django.contrib import admin
from ejento.views import HomeView
urlpatterns = patterns('',
    # Examples:
     url(r'^$', HomeView.as_view(), name='index'),
     url(r'^codingcamp/', 'codingcamp.views.index', name='codingcamp-index'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^login/$', views.login_view,name='login'),
    
    url(r'^admin/', include(admin.site.urls)),
    
    url(r'^ahp/',include('ejento.urls')),
)

