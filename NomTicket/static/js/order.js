var orders = JSON.parse(localStorage.getItem('orders'));
var total = localStorage.getItem('total');
var totalproductos = localStorage.getItem('totalproductos');
var HORA_VIG_INICIO = localStorage.getItem('HORA_VIG_INICIO');

if (orders === null || orders === undefined) {
    localStorage.setItem('orders', JSON.stringify([]));
    orders = JSON.parse(localStorage.getItem('orders'));
}

if (total === null || total === undefined) {
    localStorage.setItem('total', 0);
    total = localStorage.getItem('total');
}

if (totalproductos === null || totalproductos === undefined) {
    localStorage.setItem('totalproductos', 0);
    totalproductos = localStorage.getItem('totalproductos');
}

if (HORA_VIG_INICIO === null || HORA_VIG_INICIO === undefined) {
    var f = new Date();
    localStorage.setItem('HORA_VIG_INICIO', f.getHours() + ':' + f.getMinutes());
    HORA_VIG_INICIO = localStorage.getItem('HORA_VIG_INICIO');
}

//cantidad de productos "cart"
var cart = document.querySelector('#cart');
cart.innerHTML = totalproductos;
//lista productos "pcart"
var pcart = document.querySelector("#pcart");
var ptotal = document.querySelector("#ptotal");

//seleccionar producto
function seleccionarProducto(pid) {
    codigo_producto = '#producto' + pid
    console.log('codigoproducto',codigo_producto);
    var cantidad = 1;
    if (codigo_producto != null) {
        //totalproductos = document.querySelector(totalproductos).value;
        var nombre = document.querySelector(codigo_producto).innerHTML;
        var descripcion = '#desc' + pid;
        descripcion = document.querySelector(descripcion).innerHTML;
        var precio = '#valor' + pid;
        precio = document.querySelector(precio).innerHTML;
        var cantidad = '#cantidad' + pid;
        cantidad = document.querySelector(cantidad).value;
        //console.log(cantidad);
        //var otroprecio =precio.replace('$','');
        var orders = JSON.parse(localStorage.getItem('orders'))
        var total = localStorage.getItem('total');
        //console.log('total',total);
        var totalproductos = localStorage.getItem('totalproductos');
        //console.log('totalproductos',totalproductos);
        totalproductos = Number(totalproductos)+Number(cantidad);
        //console.log('totalproductos',totalproductos);
        var cartSize = orders.length;
        //totalproductos = Number(totalproductos) + Number(cantidad);
        //console.log(cartSize);
        //guardar total en localstorage
        var existe = 0;
        for (let i = 0; i < cartSize; i++) {

            if (orders[i][4] == pid) {
                orders[i][3] = Number(orders[i][3]) + Number(cantidad);
                existe = 1;
                console.log(orders[i][3]);
            }
            else {
                console.log('entra1');

            }
        }
        if (existe == 0) {
            orders[cartSize] = [nombre, descripcion, precio, cantidad, pid ];
        }
        if (cartSize == 0) {
            console.log('entra2');
            orders[cartSize] = [nombre, descripcion, precio, cantidad, pid ];
        }
        localStorage.setItem('orders', JSON.stringify(orders));
        localStorage.setItem('total', total);
        total = Number(total) + (Number(precio)*Number(cantidad));
        localStorage.setItem('total', total);
        localStorage.setItem('totalproductos', totalproductos);
        carritocompras();
        //actualizar items en carro de compras
                var cart = document.querySelector('#cart');
                cart.innerHTML = totalproductos;
                //console.log('cart',cart);
        //        boton = '<button class="btn-danger" onclick="borrarProducto(' + cartSize + ')">X</button>';
        //        ptotal.innerHTML = 'TOTAL: ' + '$' + total;
    } else {
    }

}


function borrarTodo() {
    console.log("borra")
    localStorage.clear();
    //pcart.innerHTML = '';
}

function carritocompras() {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartSize = orders.length;
    if (pcart === null || pcart === undefined) {
        console.log("null")
    } else {
        pcart.innerHTML = '';
    }

    for (let i = 0; i < cartSize; i++) {
        boton = '<button class="btn-danger" onclick="borrarProducto(' + i + ')">X</button>';
        pcart.innerHTML += '<li>' + orders[i][0] + ' ' + orders[i][2] + ' cantidad: ' + orders[i][3] + boton + '</li>';
    }
    ptotal.innerHTML = 'Total: ' + '$' + total;

}

carritocompras();

function borrarProducto(n) {
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var totalproductos = localStorage.getItem('totalproductos');
    console.log(total)
    totalproductos = Number(totalproductos) - Number(orders[n][3]);
    total = Number(total) - (Number(orders[n][3])*Number(orders[n][2]));
    orders.splice(n, 1);
    //actualizar carrito
    var cart = document.querySelector('#cart');
    cart.innerHTML = totalproductos;
    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('totalproductos', totalproductos);
    localStorage.setItem('total', total);
    carritocompras();
}