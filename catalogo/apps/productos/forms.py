from django import forms

from .models import Producto


class Formulario_alta_producto(forms.ModelForm):
	

	class Meta:
		model = Producto
		fields = '__all__'