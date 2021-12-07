from django.shortcuts import render

from apps.productos.models import Rubro

def Inicio(request):

	r = Rubro.objects.all()

	ctx = {}
	ctx['rubros'] = r

	
	return render(request,'inicio.html',ctx)

