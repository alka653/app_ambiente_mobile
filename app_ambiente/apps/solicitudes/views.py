import json
from .forms import *
from .models import *
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.decorators import login_required

class SolicitudView(CreateView):
	model = SolicitudUser
	form_class = SolicitudForm
	template_name = 'solicitud/make_solicitud.html'

	def form_valid(self, form):
		form.instance.user = self.request.user
		return super(SolicitudView, self).form_valid(form)

	def get_context_data(self, **kwargs):
		context = super(SolicitudView, self).get_context_data(**kwargs)
		context['title'] = 'Solicitar'
		return context

def find_bodega(request):
	results = []
	response = {}
	for material in TipoMaterial.objects.get(pk = request.GET.get('material')).bodegamaterial_set.all():
		response['pk'] = material.pk
		response['bodega'] = material.bodega.nombre
		response['bodega_dir'] = material.bodega.direccion
		response['precio'] = str(int(material.precio))
		results.append(response)
		response = {}
	return HttpResponse(json.dumps(results), content_type = 'application/json')

def save(request):
	response = {}
	print request.GET.get('bodega_material')
	bodega_material = BodegaMaterial.objects.get(pk = request.GET.get('bodega_material'))
	peso_aprox = request.GET.get('peso_aprox')
	solicitud = SolicitudUser(user = request.user, bodega_material = bodega_material, peso_aprox = peso_aprox)
	solicitud.save()
	response['msg'] = 'Guardado con exito'
	return HttpResponse(json.dumps(response), content_type = 'application/json')

def solicitud_user(request):
	solicitud = SolicitudUser.objects.filter(user = request.user)
	return render(request, 'solicitud/solicitud_user.html', {'title': 'Lista de Solicitudes', 'solicitudes': solicitud})

def view_solicitud(request):
	solicitud = BodegaMaterial.objects.filter(bodega = request.user.bodega)
	return render(request, 'solicitud/solicitud_bodega.html', {'title': 'Lista de Solicitudes', 'solicitudes': solicitud})