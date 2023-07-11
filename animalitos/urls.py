from django.urls import path
from . import views

app_name = 'animalitos'

urlpatterns = [
    path('', views.BaseView.as_view(), name='base'),
    path('inicio/', views.InicioView.as_view(), name='inicio'),
    path('nosotros/', views.NosotrosView.as_view(), name='nosotros'),
    path('tienda/', views.TiendaView.as_view(), name='tienda'),
    path('tienda/subseccion/<int:subseccion_id>/', SubseccionView.as_view(), name='subseccion'),
    path('tienda/detalle/<int:producto_id>/', DetalleProductoView.as_view(), name='detalle_producto'),
    path('contacto/', views.ContactoView.as_view(), name='contacto'),
    path('donaciones/', views.DonacionesView.as_view(), name='donaciones')
    # Define otras rutas aquí...
]