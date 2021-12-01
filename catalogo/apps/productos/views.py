from django.shortcuts import render

# Create your views here.

def ListarProductos(request):
	
	return render(request,'productos/listarProductos.html')