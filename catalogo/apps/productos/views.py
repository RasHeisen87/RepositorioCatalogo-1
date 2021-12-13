from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy

from .models import Producto, Rubro
from .forms import  Formulario_alta_producto


def ListarProductos(request):
	
	#CONSULTA PARA TRAER TODOS LOS PRODUCTOS
	# P QUERYSET (MUY PAECIDO A UN DICCIONARIO) QUE CONTIENE TODOS LOS PRODUCTOS QUE ESTEN EN LA BD
	p = Producto.objects.all()

	#CONTEXTO
	ctx = {}
	ctx['product'] = p
	ctx['titulo'] = "HOLA SOY EL TITULO"

	return render(request,'productos/listarProductos.html',ctx)
# EN REALIDAD EN EL TEMPLATE VOY TENER VARIABLES SEPARADAS

# pruduct QUE CONTIENE a p
# titulo


def DetalleProducto(request, pk):

	p = Producto.objects.get(pk = pk)

	ctx = {}
	ctx['product'] = p


	return render(request, 'productos/detalleProducto.html',ctx)


def FiltroXRubro(request, pk):

	#TRAE SOLO EL RUBRO CON ESA PK
	rubro = Rubro.objects.get(pk = pk)
	#BUSCA TODOS LOS PRODUCTOS CON UNA RELACION A ESE RUBRO
	p = Producto.objects.filter(rubro = rubro )

	ctx = {}
	ctx['product'] = p
	ctx['rubro'] = rubro

	return render(request, 'productos/filtroxRubro.html',ctx)


class AltaProducto(CreateView):
	model = 'Producto'
	template_name = 'productos/alta.html'
	form_class = Formulario_alta_producto
	success_url = reverse_lazy('productos:listar_productos')





# CLASE.objects.all()   RETORNA TODOS

# CLASE.objects.get()   RETORNA SOLO 1 OBJETO (SOLO FUNCIONA SI ESTOY SEGURO QUE VA RETORNAR UNO)

# CLASE.objects.filter() RETORNA VARIOS QUE CUMPLAN CON LA CONDICION