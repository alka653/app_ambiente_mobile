from django.conf.urls import patterns, include, url
from tastypie.api import Api
from .api import *
from .views import *

ambiente_api = Api(api_name = 'serve')
ambiente_api.register(LoginResource())
ambiente_api.register(SendSolicitudResource())
ambiente_api.register(TipoMaterialResource())
ambiente_api.register(FindBodegaResource())

urlpatterns = patterns('app_ambiente.apps.api_serve.views',
	url(r'^', include(ambiente_api.urls)),
)