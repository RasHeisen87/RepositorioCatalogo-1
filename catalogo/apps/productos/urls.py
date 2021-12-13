
from django.urls import path
from . import views

app_name = 'productos'

urlpatterns = [
 	
	path('listar/', views.ListarProductos, name = 'listar_productos'),

	path('detalle/<int:pk>', views.DetalleProducto, name= 'detalle'),

	path('FILTRO/<int:pk>', views.FiltroXRubro, name= 'filtro'),

	path('Alta/', views.AltaProducto.as_view(), name="alta_producto"),
	
]
