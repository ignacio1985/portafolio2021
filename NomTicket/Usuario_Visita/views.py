from django.shortcuts import render,redirect
from django.contrib.auth.forms import AuthenticationForm
from CORE.models import EMPLEADO, PRODUCTO, VISITANTE, TIPO_TICKET, TICKET , PEDIDO_TICKET ,TIPO_PRODUCTO, TURNO, PRODUCTO_TURNO
from .forms import visitanteForm, guardarpedido
from django.contrib import messages
from datetime import date
from datetime import datetime
from django.db.models import Max

#v_global
g_rut_visitante = ""

def inicio(request):
    return render(request, 'inicio.html')

def login_visitante(request):
    print('entra')
    if request.method == 'POST':
        form = visitanteForm(request.POST)
        if form.is_valid:
            global g_rut_visita
            g_rut_visita = request.POST['rut_visitante']
            visitante = VISITANTE(rut_visitante=request.POST['rut_visitante'])
            visitante.save()
            print(g_rut_visita)
            data = { 'g_rut_visita': g_rut_visita }
            return render(request,'home_visitante.html',data)        
    return render(request,"login_visitante.html")

def home_visitante(request):
    global g_rut_visita
    data = { 'g_rut_visita': g_rut_visita }
    print('home',g_rut_visita)
    return render(request,"home_visitante.html",data)

def lista_productosv(request):
    global g_rut_visita
    data = { 'g_rut_visita': g_rut_visita }
    print('home',g_rut_visita)
    productos = PRODUCTO.objects.all()
    context = {'productos' : productos,'g_rut_visita': g_rut_visita}
    return render(request, 'lista_productosv.html', context)

def pedidov(request):
    global g_rut_visita
    datos = { 'g_rut_visita': g_rut_visita }
    today = date.today()
    now = datetime.now()
    formato = now.strftime('%d/%m/%Y-%H:%M:%S')
    muesta_boton_imprimir = 'display:none' 
    id_ticket = ''
    boton_imprimir = ''
    if request.method == 'POST':
        form = guardarpedido(request.POST)
        visitante = VISITANTE(rut_visitante = request.POST["rut_visitante"])
        print(visitante)
        empleado = 'null'
        tipo_ticket = TIPO_TICKET(id_tipo_ticket = int(request.POST["FK_TIPO_TICKET_ID"]))
        ticket = TICKET(fecha_imp = request.POST["FECHA_IMP"],
                        hora_vig_inicio = request.POST["HORA_VIG_INICIO"], 
                        hora_vig_termino = request.POST["HORA_VIG_TERMINO"], 
                        estado = request.POST["ESTADO"], 
                        comentario = request.POST["COMENTARIO"],
                        valor = request.POST["VALOR"],
#                        fk_codigo_emp = empleado,
                        fk_tipo_ticket = tipo_ticket,
                        fk_rut_visitante = visitante)
        ticket.save()
        id_ticket = (TICKET.objects.all().aggregate(Max('codigo_ticket')))
        #id_ticket = (TICKET.objects.all().aggregate('codigo_ticket'))
        print("el id dl ticket es " + str(id_ticket["codigo_ticket__max"]))
        boton_imprimir = str(id_ticket["codigo_ticket__max"])

        if form.is_valid:
            for key, value in request.POST.items():
                print('Key: %s' % (key) ) 
                # print(f'Key: {key}') in Python >= 3.7
                print('Value %s' % (value) )
                # print(f'Value: {value}') in Python >= 3.7
                
        for p in request.POST.getlist("producto_id"):
            p_tmp = p.split("-")
            print("la cantidad %s", p_tmp[0])
            print("el id %s", p_tmp[2])
            codigo_producto = PRODUCTO(codigo_producto = p_tmp[2])
            codigo_ticket = TICKET(codigo_ticket = str(id_ticket["codigo_ticket__max"]))
            print('codigo_ticket %s' % (codigo_ticket) )
            pedido_ticket = PEDIDO_TICKET(cantidad = p_tmp[0],
                                          fk_codigo_producto = codigo_producto,
                                          fk_num_ticket = codigo_ticket)
            pedido_ticket.save()
#            for x in len(request.POST["producto_id"]):
#                print(x)
            messages.success(request,"ticket guardado") 
        muesta_boton_imprimir = 'display:block' 
    data = {'formato': formato, 'imprimir': muesta_boton_imprimir, 'id_ticket': boton_imprimir, 'g_rut_visita': g_rut_visita}
               
    return render(request, 'pedidov.html', data)
