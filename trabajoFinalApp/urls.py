from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name="principal"),
    path('acercaDe/',views.acerca_de, name="acerca de"),
    path('busqueda/',views.resultado_de_busqueda, name="busqueda"),
    path('producto/',views.producto, name="producto"),
    path('acounts/login/',views.login, name="login"),
    path('registro/',views.registro, name="registro"),
    path('carrito/',views.carrito, name="carrito"),
    path('contacto/',views.contacto, name="contacto"),
]