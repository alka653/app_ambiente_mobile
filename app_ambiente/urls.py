from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^', include('app_ambiente.apps.principal.urls')),
	url(r'^users/', include('app_ambiente.apps.users.urls')),
	url(r'^solicitudes/', include('app_ambiente.apps.solicitudes.urls')),
	url(r'^api/', include('app_ambiente.apps.api_serve.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
