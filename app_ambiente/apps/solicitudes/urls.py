from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns('app_ambiente.apps.solicitudes.views',
	url(r'^make-solicitud/$', login_required(SolicitudView.as_view()), name = 'new_solicitud'),
	url(r'^find-bodega/$', 'find_bodega', name = 'find_bodega'),
	url(r'^save/$', 'save', name = 'save'),
	url(r'^solicitud-user/$', 'solicitud_user', name = 'solicitud_user'),
	url(r'^solicitud-bodega/$', 'view_solicitud', name = 'view_solicitud'),
)