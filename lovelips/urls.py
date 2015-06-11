from django.conf.urls import patterns, include, url
from django.contrib import admin

from . import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),

    

    url(r'^input-ahp/(?P<id>\d+)$', views.InputAHPView.as_view(id=None),name='input-ahp'),

    url(r'^input-nama/(?P<id>\d+)$', views.InputNamaView.as_view(id=None),name='input-nama'),

    url(r'^input-kri/$', views.InputKriteriaAHPView.as_view(),name='input-kri'),

    url(r'^detail-ahp/(?P<id>\d+)$', views.DetailAHPView.as_view(id=None),name='detail-ahp'),

    url(r'^konsistensi-ahp/(?P<id>\d+)$', views.KonsistensiAHPView.as_view(id=None),name='konsistensi-ahp'),

    )
