var foto = document.getElementsByClassName('mifoto');

var nombre = document.getElementsByClassName('mifoto');

for (i = 0; i < foto.length; i++) {
    //var nuevalinea=document.createElement('br');
    //tarjeta[i].appendChild(nuevalinea);
    //Añadido enlace a borrar bajos
    var id=nombre[i].childNodes[0].src.split('/')[3];

    var aTag3 = document.createElement('a');
    //Cargar clase del enlace
    aTag3.setAttribute('class','enlaces-fotos');
    aTag3.innerHTML = 'x';
    aTag3.setAttribute('href','borrarfoto/'+id);
    //Añade el elemento aTag3 despues de tarjeta[i]
    foto[i].parentNode.insertBefore(aTag3, foto[i].nextSibling);
}
