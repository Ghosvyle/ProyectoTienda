from django.shortcuts import render, HttpResponse
from Tienda.models import empleado, cliente, producto, marca, pedido, comprobante, prod_pedido
from Tienda.forms import empleadosForm, clientesForm, productosForm, marcasForm, pedidosForm, comprobantesForm, prodpedidosForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from usuario.forms import RegistroForm

# Create your views here.
def home(request):
    return render(request, "home.html")

def empleados(request):
    e=empleado.objects.all()
    return render(request, "empleados.html",{'e':e})

def clientes(request):
    c=cliente.objects.all()
    return render(request, "clientes.html",{'c':c})

def productos(request):
    pro=producto.objects.all()
    return render(request, "productos.html",{'pro':pro})

def marcas(request):
    m=marca.objects.all()
    return render(request, "marcas.html",{'m':m})

def pedidos(request):
    ped=pedido.objects.all()
    return render(request, "pedidos.html",{'ped':ped})

def comprobantes(request):
    com=comprobante.objects.all()
    return render(request, "comprobantes.html",{'com':com})

def prodped(request):
    pp=prod_pedido.objects.all()
    return render(request, "prodped.html",{'pp':pp})


#Vistas clases
class empleadolist(ListView):
    model= empleado
    template_name= 'empleados.html'

class clientelist(ListView):
    model= cliente
    template_name= 'clientes.html'

class productolist(ListView):
    model= producto
    template_name= 'productos.html'

class marcalist(ListView):
    model= marca
    template_name= 'marcas.html'

class pedidolist(ListView):
    model= pedido
    template_name= 'pedidos.html'

class comprobantelist(ListView):
    model= comprobante
    template_name= 'comprobantes.html'

class prodpedlist(ListView):
    model= prod_pedido
    template_name= 'prodped.html'


#Crear Clase
class empleadocreate(CreateView):
    model= empleado
    form_class = empleadosForm
    template_name = 'empleadocreate.html'
    success_url = reverse_lazy('Empleados')

class clientecreate(CreateView):
    model= cliente
    form_class = clientesForm
    template_name = 'clientecreate.html'
    success_url = reverse_lazy('Clientes')

class marcacreate(CreateView):
    model= marca
    form_class = marcasForm
    template_name = 'marcacreate.html'
    success_url = reverse_lazy('Marcas')

class productocreate(CreateView):
    model= producto
    form_class = productosForm
    template_name = 'productocreate.html'
    success_url = reverse_lazy('Productos')

class pedidocreate(CreateView):
    model= pedido
    form_class = pedidosForm
    template_name = 'pedidocreate.html'
    success_url = reverse_lazy('Pedidos')

class comprobantecreate(CreateView):
    model= comprobante
    form_class = comprobantesForm
    template_name = 'comprobantecreate.html'
    success_url = reverse_lazy('Comprobantes')

class prodpedcreate(CreateView):
    model= prod_pedido
    form_class = prodpedidosForm
    template_name = 'prodpedcreate.html'
    success_url = reverse_lazy('Productos-Pedidos')


#Clases Update
class empleadoupdate(UpdateView):
    model= empleado
    form_class = empleadosForm
    template_name = 'empleadocreate.html'
    success_url = reverse_lazy('Empleados')

class clienteupdate(UpdateView):
    model= cliente
    form_class = clientesForm
    template_name = 'clientecreate.html'
    success_url = reverse_lazy('Clientes')

class productoupdate(UpdateView):
    model= producto
    form_class = productosForm
    template_name = 'productocreate.html'
    success_url = reverse_lazy('Productos')

class marcaupdate(UpdateView):
    model= marca
    form_class = marcasForm
    template_name = 'marcacreate.html'
    success_url = reverse_lazy('Marcas')

class pedidoupdate(UpdateView):
    model= pedido
    form_class = pedidosForm
    template_name = 'pedidocreate.html'
    success_url = reverse_lazy('Pedidos')

class comprobanteupdate(UpdateView):
    model= comprobante
    form_class = comprobantesForm
    template_name = 'comprobantecreate.html'
    success_url = reverse_lazy('Comprobantes')

class prodpedupdate(UpdateView):
    model= prod_pedido
    form_class = prodpedidosForm
    template_name = 'prodpedcreate.html'
    success_url = reverse_lazy('Productos-Pedidos')

#Clases Delete
class empleadodelete(DeleteView):
    model= empleado
    template_name = 'empleadodelete.html'
    success_url = reverse_lazy('Empleados')

class clientedelete(DeleteView):
    model= cliente
    template_name = 'clientedelete.html'
    success_url = reverse_lazy('Clientes')

class productodelete(DeleteView):
    model= producto
    template_name = 'productodelete.html'
    success_url = reverse_lazy('Productos')

class marcadelete(DeleteView):
    model= marca
    template_name = 'marcadelete.html'
    success_url = reverse_lazy('Marcas')

class pedidodelete(DeleteView):
    model= pedido
    template_name = 'pedidodelete.html'
    success_url = reverse_lazy('Pedidos')

class comprobantedelete(DeleteView):
    model= comprobante
    template_name = 'comprobantedelete.html'
    success_url = reverse_lazy('Comprobantes')

class prodpeddelete(DeleteView):
    model= prod_pedido
    template_name = 'prodpeddelete.html'
    success_url = reverse_lazy('Productos-Pedidos')

class RegistroUsuario(CreateView):
    model = User
    form_class = RegistroForm
    template_name = "registro.html"
    success_url = reverse_lazy('Empleados')