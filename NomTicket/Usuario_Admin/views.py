from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import AuthenticationForm
from .forms import empleadoForm, loginEmpForm
from CORE.models import EMPLEADO, TICKET, VISITANTE 
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.contrib.auth.hashers import check_password
from django.contrib.auth.hashers import make_password
from django.conf import settings
from django.core.mail import send_mail
from random import choice

def enviarcorreo(request):
    if request.method=="POST":
        subject=request.POST['asunto']

        message=request.POST['mensaje']+ " remitente: "+ request.POST['correo']

        email_from=settings.EMAIL_HOST_USER
        print(email_from)

        correo_dest=request.POST['correo_destino']
        #correo_dest=['josemiguelponcem@gmail.com']
        print(correo_dest)

        send_mail(subject, message, email_from, [correo_dest])
        print("enviado")

        #generar contraseña
        #longitud = 10
        #valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ<=>@#%&+"

        #p = ""
        #p = p.join([choice(valores) for i in range(longitud)])
        #print("contraseña",p)
        #data = {
        #            'empleados': "pico",
        #            'p':p
        #        }
        #print("primero")
        #return render(request, 'contacto.html', data)
        return redirect('/Usuario_Admin/contacto')

    return render(request, "contacto.html")


def inicio(request):
    return render(request, 'inicio.html')

def lista_empleado(request):
    empleados =  EMPLEADO.objects.all()
    #empleados =  EMPLEADO.objects.filter(nom_emp = 'juan')
    data = {
        'empleados' : empleados
    }
    return render(request,"lista_empleado.html", data)

def registrar_empleado(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = empleadoForm()
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(instance=empleado)
        return render(request,"registrar_empleado.html",{'form':form})
    else:
        if id == 0:
            form = empleadoForm(request.POST)
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(request.POST,instance= empleado)
        if form.is_valid():
            print("entra")
            form_emp = form.save(commit=False)
            clave = request.POST['clave']
            print(clave)            
            form_emp.clave = make_password(clave)
            #enviar contraseña por correo
            if request.method=="POST":
                subject='Contraseña Nomticket'

                message="Rut empleado: "+request.POST['rut_emp']+ " Contraseña: "+ request.POST['clave']+"  -Enviado por EMPRESA NOMTICKET.-"
                print(message)

                email_from=settings.EMAIL_HOST_USER
                print(email_from)

                #contraseña=request.POST['clave']
                #print(contraseña)

                correo_dest=request.POST['email']
                #correo_dest=['josemiguelponcem@gmail.com']
                print(correo_dest)

                send_mail(subject, message, email_from, [correo_dest])
                print("enviado")
        form.save()
        messages.success(request,"Guardado correctamente")
        return redirect('/Usuario_Admin/lista')
    return redirect('/Usuario_Admin/lista')
               
def eliminar_empleado(request,id): 
    empleado = get_object_or_404(EMPLEADO, pk=id)
    empleado.delete()
    messages.success(request,"Eliminado correctamente")
    return redirect('/Usuario_Admin/lista')

def logout(request): 
    return redirect("/")

def home_admin(request):
    return render(request,"home_admin.html")

def modificar_empleado(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = empleadoForm()
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(instance=empleado)
        return render(request,"modificar_empleado.html",{'form':form})
    else:
        if id == 0:
            form = empleadoForm(request.POST)
        else:
            empleado = EMPLEADO.objects.get(pk=id)
            form = empleadoForm(request.POST,instance= empleado)
        if form.is_valid():
            form_emp = form.save(commit=False)
            clave = request.POST['clave']
            print(clave)            
            form_emp.clave = make_password(clave)
            #print(form_emp.clave)
            #enviar contraseña por correo
            if request.method=="POST":
                subject='Contraseña Nomticket'

                message="Rut empleado: "+request.POST['rut_emp']+ " Contraseña: "+ request.POST['clave']+"  -Enviado por EMPRESA NOMTICKET.-"
                print(message)

                email_from=settings.EMAIL_HOST_USER
                print(email_from)

                correo_dest=request.POST['email']
                #correo_dest=['josemiguelponcem@gmail.com']
                print(correo_dest)

                send_mail(subject, message, email_from, [correo_dest])
                print("enviado")
            form.save()
            print("modificado")
            messages.success(request,"Modificado correctamente")
        return redirect('/Usuario_Admin/lista')

def tickets_empleados(request):
    empleados = EMPLEADO.objects.all()
    datos = {'empleados': empleados}
    for empleado in empleados:
        #codigo_empleado=empleado.codigo_emp
        #print (type(codigo_empleado))
    #tickets = TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s order by fecha_imp', [empleado.codigo_emp])
        tickets = TICKET.objects.raw('select * from empleado e join ticket t on e.codigo_emp=t.fk_codigo_emp_id')
    #tickets = TICKET.objects.raw('select t.codigo_ticket,p.nom_producto,t.fecha_imp,t.hora_vig_inicio,t.hora_vig_termino,t.valor,pt.cantidad from ticket t join pedido_ticket pt on t.codigo_ticket=pt.fk_num_ticket_id join producto p on pt.fk_codigo_producto_id=p.codigo_producto where t.fk_codigo_emp_id=446 order by t.fecha_imp;')
    data = {'empleados': empleados, 'tickets':tickets}
    #for p in TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s', [empleado.codigo_emp]):    
    #print (p.codigo_ticket)
            
    return render(request, 'tickets_empleados.html',data)

def tickets_visitantes(request):
    empleados = EMPLEADO.objects.all()
    datos = {'empleados': empleados}
    for empleado in empleados:
        #codigo_empleado=empleado.codigo_emp
        #print (type(codigo_empleado))
    #tickets = TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s order by fecha_imp', [empleado.codigo_emp])
        tickets = TICKET.objects.raw('select * from visitante v join ticket t on v.rut_visitante=t.fk_rut_visitante_id')
    #tickets = TICKET.objects.raw('select t.codigo_ticket,p.nom_producto,t.fecha_imp,t.hora_vig_inicio,t.hora_vig_termino,t.valor,pt.cantidad from ticket t join pedido_ticket pt on t.codigo_ticket=pt.fk_num_ticket_id join producto p on pt.fk_codigo_producto_id=p.codigo_producto where t.fk_codigo_emp_id=446 order by t.fecha_imp;')
    data = {'empleados': empleados, 'tickets':tickets}
    #for p in TICKET.objects.raw('select * from ticket where fk_codigo_emp_id=%s', [empleado.codigo_emp]):    
    #print (p.codigo_ticket)
            
    return render(request, 'tickets_visitantes.html',data)
