var nombre = document.querySelector('#nombre');
var descripcion = document.querySelector('#descripcion');
var precio = document.querySelector('#precio');
var cantidad = document.querySelector('#cantidad');
var totalpedido = document.querySelector('#totalpedido');
var eliminar = document.querySelector('#eliminar');
var cart = document.querySelector('#cart');


function carritocompras_p() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var totalproductos = localStorage.getItem('totalproductos');
    console.log('totalproductos1', totalproductos);
    var cartSize = orders.length;

    nombre.innerHTML = '<h4>Nombre</h4>';
    descripcion.innerHTML = '<h4>Descripción</h4>';
    precio.innerHTML = '<h4>Precio</h4>';
    cantidad.innerHTML = '<h4>Cantidad</h4>';
    eliminar.innerHTML = '<h4>Eliminar</h4>';

    for (let i = 0; i < cartSize; i++) {
        eliminar.innerHTML += '<h6><button class="btn-danger" onclick="borrarProducto_p(' + i + ')">X</button><h6>';
        nombre.innerHTML += '<h5>' + orders[i][0] + '</h5>'
        descripcion.innerHTML += '<h5>' + orders[i][1] + '</h5>'
        precio.innerHTML += '<h5>' + orders[i][2] + '</h5>'
        cantidad.innerHTML += '<h5>' + orders[i][3] + '</h5>'
    }
    totalpedido.innerHTML = '<h4>Total: ' + '$' + total + '</h4>';
    var cart = document.querySelector('#cart');
    cart.innerHTML = totalproductos;
}

function borrarProducto_p(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    console.log('borra');
    //totalpedido = Number(total) - Number(orders[n][3]);
    var totalproductos = localStorage.getItem('totalproductos');
    totalproductos = Number(totalproductos) - Number(orders[n][3]);
    console.log('1 '+totalproductos+' 2 '+(orders[n][3]))
    total = Number(total) - (Number(orders[n][3])*Number(orders[n][2]));
    //total = Number(total) - Number(orders[n][2]);
    orders.splice(n, 1);
    //actualizar carrito
    var cart = document.querySelector('#cart');
    cart.innerHTML = totalproductos;
    //cart.innerHTML = orders.length;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('totalproductos', totalproductos);
    localStorage.setItem('total', total);
    carritocompras_p();
}

carritocompras_p();

function guardarPedidov() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var f = new Date();
    var mes = f.getMonth() + 1;
    //Se rescata el formulario
    var formulario = document.getElementById('guardar');
    //Se crea input campos
    var input_fecha = document.createElement('input');
    var input_h_ini = document.createElement('input');
    var input_h_ter = document.createElement('input');
    var input_estado = document.createElement('input');
    var input_comentario = document.createElement('input');
    var input_valor = document.createElement('input');
    var input_cantidad = document.createElement('input');
    var input_empleado = document.createElement('input');
    var input_tipo_ticket = document.createElement('input');
    var input_rut_visitante = document.createElement('input');
    //Se define el tipo de input (oculto)
    input_fecha.type = 'hidden';
    input_h_ini.type = 'hidden';
    input_h_ter.type = 'hidden';
    input_estado.type = 'hidden';
    input_comentario.type = 'hidden';
    input_valor.type = 'hidden';
    input_cantidad.type = 'hidden';
    input_empleado.type = 'hidden';
    input_tipo_ticket.type = 'hidden';
    input_rut_visitante.type = 'hidden';
    //Se define el nombre de los input
    input_fecha.name = "FECHA_IMP";
    input_h_ini.name = "HORA_VIG_INICIO";
    input_h_ter.name = "HORA_VIG_TERMINO";
    input_estado.name = "ESTADO";
    input_comentario.name = "COMENTARIO";
    input_valor.name = "VALOR";
    input_cantidad.name = "CANTIDAD";
    input_empleado.name = "FK_CODIGO_EMP_ID";
    input_tipo_ticket.name = "FK_TIPO_TICKET_ID";
    input_rut_visitante.name = 'FK_RUT_VISITANTE_ID';

    //Se calcula la fecha de impresion
    var FECHA_IMP = f.getDate() + "-" + mes + "-" + f.getFullYear();
    //Se calcualan los valores
    //console.log(FECHA_IMP);
    var HORA_VIG_INICIO = localStorage.getItem('HORA_VIG_INICIO');
    //console.log(HORA_VIG_INICIO);
    var HORA_VIG_TERMINO = f.getHours() + ':' + f.getMinutes();
    //console.log(HORA_VIG_TERMINO);
    var ESTADO = 1;
    var VALOR = localStorage.getItem('total');
    //console.log(VALOR);
    var COMENTARIO = "visitante";
    var CANTIDAD =localStorage.getItem('CANTIDAD');
    //console.log(CANTIDAD);
    var FK_CODIGO_EMP_ID = null;
    //console.log(FK_CODIGO_EMP_ID);
    var FK_TIPO_TICKET_ID = 1;
    var FK_RUT_VISITANTE_ID = document.querySelector('#rut_visitante').value; 
    console.log('fk_visitante',FK_RUT_VISITANTE_ID)
    //Se agregan los valores a los input
    input_fecha.value = FECHA_IMP;
    input_h_ini.value = HORA_VIG_INICIO;
    input_h_ter.value = HORA_VIG_TERMINO;
    input_estado.value = ESTADO;
    input_comentario.value = COMENTARIO;
    input_valor.value = VALOR;
    input_cantidad.value = CANTIDAD;
    input_empleado.value = FK_CODIGO_EMP_ID;
    input_tipo_ticket.value = FK_TIPO_TICKET_ID;
    input_rut_visitante.value = FK_RUT_VISITANTE_ID;
    //Se agregan los input al formulario
    formulario.appendChild(input_fecha);
    formulario.appendChild(input_h_ini);
    formulario.appendChild(input_h_ter);
    formulario.appendChild(input_estado);
    formulario.appendChild(input_comentario);
    formulario.appendChild(input_valor);
    formulario.appendChild(input_cantidad);
    formulario.appendChild(input_empleado);
    formulario.appendChild(input_tipo_ticket);
    formulario.appendChild(input_rut_visitante);
    //Se crean los input de cada producto que viene en el ticket
    for (i = 0; i < orders.length; i++) {
        var input_producto = document.createElement('input');
        input_producto.type = 'hidden';
        input_producto.name = "producto_id";
        input_producto.id = "p" + i;
        input_producto.value = orders[i][3] + "-" + i + "-" + orders[i][4] + "-" + i ;
        formulario.appendChild(input_producto);
    }
    //Se envia el formulario
    //document.getElementById('guardar').submit();
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    nombre_m.innerHTML = '<h4>Nombre</h4>';
    descripcion_m.innerHTML = '<h4>Descripción</h4>';
    precio_m.innerHTML = '<h4>Precio</h4>';
    cantidad_m.innerHTML = '<h4>Cantidad</h4>';

    for (let i = 0; i < cartSize; i++) {
        nombre_m.innerHTML += '<h5>' + orders[i][0] + '</h5>'
        descripcion_m.innerHTML += '<h5>' + orders[i][1] + '</h5>'
        precio_m.innerHTML += '<h5>' + orders[i][2] + '</h5>'
        cantidad_m.innerHTML += '<h5>' + orders[i][3] + '</h5>'
    }
    totalpedido_m.innerHTML = '<h4>Total: ' + '$' + total + '</h4>';
    //document.getElementById("TicketModal").style.display = "block";
    document.getElementById('guardar').submit();
}

function envia_ticket() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var f = new Date();
    var mes = f.getMonth() + 1;
    //Se envia el formulario
    //document.getElementById('guardar').submit();
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;

    nombre_m.innerHTML = '<h4>Nombre</h4>';
    descripcion_m.innerHTML = '<h4>Descripción</h4>';
    precio_m.innerHTML = '<h4>Precio</h4>';
    cantidad_m.innerHTML = '<h4>Cantidad</h4>';

    for (let i = 0; i < cartSize; i++) {
        nombre_m.innerHTML += '<h5>' + orders[i][0] + '</h5>'
        descripcion_m.innerHTML += '<h5>' + orders[i][1] + '</h5>'
        precio_m.innerHTML += '<h5>' + orders[i][2] + '</h5>'
        cantidad_m.innerHTML += '<h5>' + orders[i][3] + '</h5>'
    }
    totalpedido_m.innerHTML = '<h4>Total: ' + '$' + total + '</h4>';
    document.getElementById("TicketModal").style.display = "block";
}
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks anywhere outside of the modal, close it
window.onclick = function (event) {
    if (event.target == document.getElementById("TicketModal")) {
        document.getElementById("TicketModal").style.display = "none";
    }
}
function cerrar_modal() {
    document.getElementById("TicketModal").style.display = "none";
}
