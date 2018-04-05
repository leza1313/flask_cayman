var tarjeta = document.getElementsByClassName('card-title');

var nombre = document.getElementsByClassName('card-title');

for (i = 0; i < tarjeta.length; i++) {
    var nuevalinea=document.createElement('br');
    tarjeta[i].appendChild(nuevalinea);
    //Añadido enlace a borrar bajos
    var aTag3 = document.createElement('a');
    //Cargar clase del enlace
    aTag3.setAttribute('class','enlaces');
    aTag3.innerHTML = 'Borrar Bajo ';
    aTag3.setAttribute('href','borrarbajo/'+nombre[i].childNodes[0].textContent);
    aTag3.setAttribute('data-toggle','confirmation');
    tarjeta[i].appendChild(aTag3);

}
$('[data-toggle=confirmation]').confirmation({
    rootSelector: '[data-toggle=confirmation]',
    popout: true,
    singleton: true,
    title: '¿Estas seguro?',
    btnOkLabel: 'Si',
});


//Añadido enlace a añadir bajos. Este solo se pone una vez, independientemente del numero de bajos que haya
var seccion = document.getElementById('productos');
//seccion.appendChild(nuevalinea);
seccion.appendChild(document.createElement('hr'));
var aTag2 = document.createElement('a');
aTag2.setAttribute('href','nuevobajo');
aTag2.setAttribute('class','btn btn-info');
aTag2.innerHTML = '<br>Añadir bajo<br><br>';
seccion.appendChild(aTag2);
var nuevalinea2=document.createElement('br');
seccion.appendChild(nuevalinea2);
var nuevalinea3=document.createElement('br');
seccion.appendChild(nuevalinea3)

