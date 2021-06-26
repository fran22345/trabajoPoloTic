from django.shortcuts import render
from .models import Productos
from .forms import CreatUserForm, categoria, Contacto
from django.contrib.auth.decorators import permission_required
# Create your views here.


def index(request):
    lista = Productos.objects.order_by('id').reverse()[:3]
    lista2 = Productos.objects.order_by('id').reverse()[3:10]
    data = {
        'lista': lista,
        'lista2': lista2,
    }
    return render(request, 'trabajoFinalApp/index.html', data)


def acerca_de(request):
    return render(request, 'trabajoFinalApp/acercaDe.html')


def resultado_de_busqueda(request):
    
    return render(request, 'trabajoFinalApp/busqueda.html')


@permission_required('trabajoFinalApp.add_producto')
def producto(request):
    data = {
        'productos': categoria()
    }
    if request.method == 'POST':
        formulario = categoria(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
    
    return render(request, 'trabajoFinalApp/producto.html', data)


def login(request):
    return render(request, 'trabajoFinalApp/login.html')


def registro(request):
    if request.method == "POST":
        form = CreatUserForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CreatUserForm()
    contex = {
        'form': form
    }
    return render(request, 'trabajoFinalApp/registro.html', contex)


def carrito(request):
    return render(request, 'trabajoFinalApp/carrito.html')


def contacto(request):
    if request.method == "POST":
        form = Contacto(request.POST)
        if form.is_valid():
            form.save()
           
    else:
        form = Contacto()
    data = {
        'form': form
    }
    return render(request, 'trabajoFinalApp/contacto.html', data)
