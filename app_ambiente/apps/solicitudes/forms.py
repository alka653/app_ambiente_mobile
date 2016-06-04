# -*- encoding: utf-8 -*-
from django.forms import *
from django import forms
from .models import *

class SolicitudForm(forms.ModelForm):
	class Meta:
		model = SolicitudUser
		fields = '__all__'
		exclude = ('user',)
		labels = {
			'peso_aprox': 'Peso Aproximado (Kg)',
		}

	def __init__(self, *args, **kwargs):
		super(SolicitudForm, self).__init__(*args, **kwargs)
		self.fields['peso_aprox'].widget = widgets.TextInput(attrs = {'class': 'form-control', 'required': True})
		self.fields['bodega_material'] = forms.ModelChoiceField(label = 'Material', queryset = TipoMaterial.objects.all(), empty_label = 'Seleccione un Material', widget = forms.Select(attrs = {'class': 'form-control', 'required': True}))

class SolicitudUserForm(forms.ModelForm):
	class Meta:
		model = SolicitudUser
		fields = '__all__'

	def clean_user(self):
		print "Ole"