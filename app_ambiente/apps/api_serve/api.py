from tastypie.authentication import ApiKeyAuthentication, BasicAuthentication, MultiAuthentication
from tastypie.authorization import *
from app_ambiente.apps.solicitudes.models import *
from tastypie.resources import ALL_WITH_RELATIONS
from tastypie.validation import FormValidation
from django.contrib.auth import get_user_model
from tastypie.serializers import Serializer
from .corsresource import CorsResourceBase
from tastypie.models import ApiKey
from tastypie.resources import *
from app_ambiente.apps.solicitudes.forms import SolicitudUserForm

User = get_user_model()
cont = 0

class LoginResource(CorsResourceBase, ModelResource):
	class Meta:
		queryset = User.objects.all()
		fields = ["first_name", "last_name", "username", "pk"]
		allowed_method = ['get']
		resource_name = 'login'
		authorization = DjangoAuthorization()
		authentication = BasicAuthentication()

	def dehydrate(self, bundle):
		username = bundle.data.get('username')
		user = User.objects.get(username = username)
		bundle.data['api_key'] = ApiKey.objects.get_or_create(user = user)[0].key
		return bundle

class SendSolicitudResource(ModelResource):
	class Meta:
		queryset = SolicitudUser.objects.all()
		resource_name = 'send_solicitud'
		filtering = {
			"peso_aprox": ALL_WITH_RELATIONS,
			"user": ALL_WITH_RELATIONS,
			"bodega_material": ALL_WITH_RELATIONS,
		}

	def hydrate(self, bundle):
		bundle.obj.user = bundle.request.user
		return bundle

class TipoMaterialResource(ModelResource):
	class Meta:
		queryset = TipoMaterial.objects.all()
		fields = ["id", "nombre"]
		allowed_method = ['get']
		resource_name = 'tipo_material'
		authorization = DjangoAuthorization()
		serializer = Serializer(formats=['json', 'plist'])

class FindBodegaResource(ModelResource):
	class Meta:
		queryset = TipoMaterial.objects.all()
		fields = ["id"]
		allowed_method = ['get']
		resource_name = 'find_bodega'
		authorization = DjangoAuthorization()

	def dehydrate(self, bundle):
		global cont
		cont = cont + 1
		results = []
		response = {}
		if cont < 2:
			for material in TipoMaterial.objects.get(pk = bundle.request.GET['material']).bodegamaterial_set.all():
				response['pk'] = material.pk
				response['bodega'] = material.bodega.nombre
				response['bodega_dir'] = material.bodega.direccion
				response['precio'] = str(int(material.precio))
				results.append(response)
				response = {}
			bundle.data['response'] = results
			return bundle
		else:
			cont = 0