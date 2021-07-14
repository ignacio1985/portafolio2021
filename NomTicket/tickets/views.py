from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from CORE.models import PRODUCTO, TICKET, EMPLEADO
from .forms import CrearTicket
from django.contrib import messages

# Create your views here.

#@login_required(login_url='home')
def empleado(request):
    form = CrearTicket(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form' : form
    }
    return render(request, 'tickets/empleado.html', context)


#@login_required(login_url='home')
#def lista_productos(request):
#    productos = PRODUCTO.objects.all().order_by('codigo_producto')
#    producto = PRODUCTO.objects.get(codigo_producto=1)
#    print(producto)
#    return render(request, 'tickets/lista_productos.html', {'productos' : productos })


#@login_required(login_url='home')
def tickets_emitidos(request):
    tickets = TICKET.objects.all().order_by('fecha_imp')
    return render(request, 'tickets/lista_tickets_emitidos.html', {'tickets' : tickets })


#@login_required(login_url='home')
#def ticket_empleado(request):
    #return render(request, 'tickets/ticket_empleado.html')
    

