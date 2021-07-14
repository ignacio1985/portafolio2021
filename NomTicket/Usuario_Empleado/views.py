from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm, loginEmpForm, guardarpedido, rec_con_Form
from CORE.models import EMPLEADO, PRODUCTO, TICKET, TIPO_TICKET, PEDIDO_TICKET ,TIPO_PRODUCTO, TURNO, PRODUCTO_TURNO
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from random import choice
from django.contrib.auth import logout
from django.http import HttpResponse
from django.db.models import Max
import json

#v_global
g_rut_emp = ""

def inicio(request):
    return render(request, 'inicio.html')

#def logout(request):
#    response = redirect('/')
#    response.delete_cookie('user_location')
#    return response

def logout_user(request):
     logout(request)
     response = redirect('/')
     response.delete_cookie('user_location')
     return response


def login_empleado(request):
    if request.method == 'POST':
        form = loginEmpForm(request.POST)
        if form.is_valid:
            global g_rut_emp
            g_rut_emp = request.POST['rut_emp']
            clave = request.POST['clave']
            verificar = EMPLEADO.objects.filter(rut_emp=g_rut_emp).exists()
            if verificar == True:
                print("true")
                empleados = EMPLEADO.objects.filter(rut_emp = g_rut_emp)
                data = {
                    'empleados' : empleados
                }
                for empleado in empleados:
                    clave_emp=empleado.clave
                    print("nom_emp",g_rut_emp)
                    print("clave",clave)
                    print ("clave_emp",clave_emp)
                if check_password(clave, clave_emp):
                    print("si")
                #verificar = EMPLEADO.objects.filter(rut_emp=g_rut_emp, clave=clave).exists()
                #if verificar == True:
                    today = date.today()
                    now = datetime.now()
                    formato = now.strftime('%d/%m/%Y-%H:%M:%S')
                    print(formato)
                    #messages.info(request, f'FECHA: {formato}')
                    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
                    data = {
                        'empleados': empleados,
                        'formato':formato
                    }
                    print("primero")
                    return render(request, "home_empleado.html", data)
                else:
                    print("no")
                    print("segundo")
                    messages.error(
                        request, 'Por favor, introduzca un nombre de usuario y clave correctos.Observe que ambos campos pueden ser sensibles a mayúsculas.')
                    return redirect('/login_empleado')
            else:
                print("no")
                print("segundo")
                messages.error(
                    request, 'Por favor, introduzca un nombre de usuario y clave correctos.Observe que ambos campos pueden ser sensibles a mayúsculas.')
                return redirect('/login_empleado')
    else:
        form = loginEmpForm
        print("tercero")
        return render(request, "login_empleado.html", {'form': form})


def prueba(request):
    global g_rut_emp
    print(g_rut_emp)
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    data = {
        'empleados': empleados
    }
    return render(request, "prueba.html", data)


def home_empleado(request):
    return render(request, "home_empleado.html")


#@login_required(login_url='home')
def lista_productos_old(request):
    global g_rut_emp
    if g_rut_emp !=" ":
        print(g_rut_emp)
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    data = {
        'empleados': empleados
    }
    productos = PRODUCTO.objects.all().order_by('codigo_producto')
    if productos!="":
        producto = PRODUCTO.objects.get(codigo_producto=1)
        print(producto)
    context =  {'empleados': empleados , 'productos' : productos}
    return render(request, 'lista_productos.html',context)

def lista_productos(request):
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)    
    data = {'empleados': empleados}
    for empleado in empleados:
        turno=empleado.fk_turno
        print(empleado.fk_turno)
        print(type(turno))
    turnos_empleados=TURNO.objects.raw('select id_turno from turno where nombre="Turno AM"')
    productos = PRODUCTO.objects.raw('select pro.* from (select * from empleado where rut_emp=%s) emp left outer join (select * from producto_turno) pro_tur on emp.fk_turno_id= pro_tur.fk_id_turno_id left OUTER JOIN (select * from producto) pro  on pro_tur.fk_id_tipo_producto_id=pro.fk_tipo_producto_id', [g_rut_emp])
    datos = {'empleados': empleados , 'productos' : productos}
    return render(request, 'lista_productos.html', datos)

def pedido(request):
    today = date.today()
    now = datetime.now()
    formato = now.strftime('%d/%m/%Y-%H:%M:%S')
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    muesta_boton_imprimir = 'display:none' 
    id_ticket = ''
    boton_imprimir = ''
    if request.method == 'POST':
        form = guardarpedido(request.POST)
        empleado = EMPLEADO(codigo_emp = int(request.POST["FK_CODIGO_EMP_ID"]))
        tipo_ticket = TIPO_TICKET(id_tipo_ticket = int(request.POST["FK_TIPO_TICKET_ID"]))
        ticket = TICKET(fecha_imp = request.POST["FECHA_IMP"],
                        hora_vig_inicio = request.POST["HORA_VIG_INICIO"], 
                        hora_vig_termino = request.POST["HORA_VIG_TERMINO"], 
                        estado = request.POST["ESTADO"], 
                        comentario = request.POST["COMENTARIO"],
                        valor = request.POST["VALOR"],
                        fk_codigo_emp = empleado,
                        fk_tipo_ticket = tipo_ticket)
        ticket.save()
        cantidad = request.POST["CANTIDAD"]
        print('cantidad',cantidad)
        id_ticket = (TICKET.objects.all().aggregate(Max('codigo_ticket')))
        print("el id dl ticket es " + str(id_ticket["codigo_ticket__max"]))
        boton_imprimir = str(id_ticket["codigo_ticket__max"])

        if form.is_valid:
            for key, value in request.POST.items():
                print('Key: %s' % (key) ) 
                # print(f'Key: {key}') in Python >= 3.7
                print('Value %s' % (value) )
                # print(f'Value: {value}') in Python >= 3.7
    
        for p in request.POST.getlist("producto_id"):
            print('el indice: '+p+'hay este valor: '+str(request.POST.getlist("producto_id")))
            p_tmp = p.split("-")
            print("la cantidad %s", p_tmp[0])
            print("el id %s", p_tmp[2])
        
            codigo_producto = PRODUCTO(codigo_producto = p_tmp[2])
            #print('codigo_producto',codigo_producto)
            codigo_ticket = TICKET(codigo_ticket = str(id_ticket["codigo_ticket__max"]))
            print('codigo_ticket %s' % (codigo_ticket) )
            pedido_ticket = PEDIDO_TICKET(cantidad = p_tmp[0],
                                          fk_codigo_producto = codigo_producto,
                                          fk_num_ticket = codigo_ticket)
            pedido_ticket.save()
            print('cantidad',cantidad),
#            for x in len(request.POST["producto_id"]):
#                print(x)
            messages.success(request,"ticket guardado") 
        muesta_boton_imprimir = 'display:block' 
    data = {'empleados': empleados,'formato': formato, 'imprimir': muesta_boton_imprimir, 'id_ticket': boton_imprimir}
               
    return render(request, 'pedido.html', data)

def cookie(request):
    return render(request, 'cookie.html')

def tickets_emitidos(request):
    empleados = EMPLEADO.objects.filter(rut_emp=g_rut_emp)
    datos = {'empleados': empleados}
    for empleado in empleados:
        print('codigo_empleado',empleado.codigo_emp)
        #codigo_empleado=empleado.codigo_emp
        #print (type(codigo_empleado))
    tickets = TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s order by fecha_imp', [empleado.codigo_emp])
    #tickets = TICKET.objects.raw('select t.codigo_ticket,p.nom_producto,t.fecha_imp,t.hora_vig_inicio,t.hora_vig_termino,t.valor,pt.cantidad from ticket t join pedido_ticket pt on t.codigo_ticket=pt.fk_num_ticket_id join producto p on pt.fk_codigo_producto_id=p.codigo_producto where t.fk_codigo_emp_id=446 order by t.fecha_imp;')
    data = {'empleados': empleados, 'tickets':tickets}
    #for p in TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s', [empleado.codigo_emp]):    
    #print (p.codigo_ticket)
            
    return render(request, 'tickets_emitidos.html',data)

def detalle_ticket(request):

    return render(request, 'detalle_ticket.html')

