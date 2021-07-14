//Funcion solo letras
function SoloLetras(e) {
    key = e.keyCode || e.which;
    teclado = String.fromCharCode(key).toLowerCase();
    letras = "abcdefghijklmnñopqrstuvwxyzáéíóú";
    especiales = "8-37-38-46-164";
    teclado_especial = false;

    for (var i in especiales) {
        if (key == especiales[i]) {
            teclado_especial = true;
            break;
        }
    }

    if (letras.indexOf(teclado) == -1 && !teclado_especial) {
        alert("Ingresar solo letras");
        return false;
    }
}
function generaContraseña(length) {
    var result = '';
    var characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789<=>@#%&+';
    var charactersLength = characters.length;
    for (var i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    document.getElementById("id_clave").value = result;
    console.log(result);
    return result;

}
//clave=generaContraseña(10);
//console.log(clave);
//console.log(generaContraseña(10));


//Funcion solo numeros
function SoloNumeros(evt) {
    if (window.event) {
        keynum = evt.keyCode;
    }
    else {
        keynum = evt.which;
    }

    if ((keynum > 47 && keynum < 58) || keynum == 8 || keynum == 13) {
        return true;
    }
    else {
        alert("Ingresar solo numeros");
        return false;
    }
}

function muestraContraseña() {
    clave = document.getElementById('id_clave')
    clave.type = "text";
    return true;
}

function escondeContraseña() {
    clave = document.getElementById('id_clave')
    if (clave.type = "text") {
        clave.type = "password";
    }
    return true;
}

