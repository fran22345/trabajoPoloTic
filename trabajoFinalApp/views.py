from django.shortcuts import redirect, render, get_object_or_404
from .models import Productos, CarritoUs, User
from .forms import CreatUserForm, categoria, Contacto, FormCarro
from django.contrib.auth.decorators import permission_required, login_required
from django.db.models import Q
from django.contrib import messages
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
    selector = request.GET.get('buscar')
    data =  {'lista': Productos.objects.filter(
            Q(Titulo = selector)|
            Q(Categoria = selector)|
            Q(Descripcion = selector)|
            Q(Imagen = selector)
        ).distinct()}
    return render(request, 'trabajoFinalApp/busqueda.html', data)



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

        if not User.objects.filter(username= request.POST.get('username')).exists():
            if form.is_valid():
                form.save()
                messages.success(request, 'Usuario Agregado Correctamente')
                return redirect('/registro/')
        else:
            messages.success(request, "Usuario Existente, intente nuevamente")
            return redirect('/registro/')
    form = CreatUserForm()
    contex = {
        'form': form
    }
    return render(request, 'trabajoFinalApp/registro.html', contex)

@login_required
def carrito(request):
    dato1= request.user.username
    carro= CarritoUs.objects.filter(UsuarioIdent= dato1)
    dato={
        'lista':carro
    }
    return render(request, 'trabajoFinalApp/carrito.html', dato)


def contacto(request):
    if request.method == "POST":
        form = Contacto(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mensaje enviado Exitosamente!')
           
    else:
        form = Contacto()
    data = {
        'form': form
    }
    return render(request, 'trabajoFinalApp/contacto.html', data)

def autos(request):
    autos= Productos.objects.filter(Categoria = "autos")
    articulo= request.GET.get("busqueda")
    if articulo:
        data = {'lista': Productos.objects.get(pk = articulo)
        }
        return render(request, 'trabajoFinalApp/solo.html', data)
    else:
        data = {
        'lista': autos
        }
        return render(request, 'trabajoFinalApp/busqueda.html', data)

@login_required
def solo(request):
    objetoId = request.GET.get('busqueda')
    if request.method == 'POST':   
        carro= request.POST
        carrito = FormCarro(carro)

        if carrito.is_valid():
            carrito.save()
            return redirect('/carrito/')
    else:
        Producto = Productos.objects.get(pk = objetoId)
        data = {
            'lista': Producto
        }
        return render(request, 'trabajoFinalApp/solo.html', data)

def borrar(request, id):
    borrar = get_object_or_404(CarritoUs, id=id)
    borrar.delete()
    return redirect('/carrito/')

def borrarTodo(request):
    user = request.user.username
    borrar = CarritoUs.objects.filter(UsuarioIdent = user).delete()
    return redirect('/carrito/')

def borrarProd(request, id):
    borrar = get_object_or_404(Productos, id=id)
    borrar.delete()
    return redirect('/')

def modificar(request, id):

    modificar = get_object_or_404(Productos, id=id)
    data = {
        'productos': categoria(instance=modificar)
    }

    if request.method =='POST':
        form = categoria (data= request.POST, instance=modificar, files= request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/')

    return render(request, 'trabajoFinalApp/modificar.html', data)