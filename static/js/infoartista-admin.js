//Codigo que añade un salto de linea, enlace <a href> y concatena el contenido al enlace para pasar parametros por GET
var nombreoriginal = document.getElementById('artist-nombre');

var aTag = document.createElement('a');
//Cargar enlaces en href
aTag.setAttribute('href','');
aTag.setAttribute('data-toggle','modal');
aTag.setAttribute('data-target','#mimodal');
aTag.setAttribute('class',"enlaces-oscuros");
//Cargar el texto entre etiquetas
aTag.innerHTML = "<br>Editar";
//Añadir la etiqueta al elemento tarjeta
nombreoriginal.appendChild(aTag);

var foto = document.getElementsByClassName('mifoto');
//console.log(foto[0]);
var src = document.getElementsByClassName('mifoto');

var nombre = document.URL.split('/')[4]

for (i = 0; i < foto.length; i++) {
    var id=src[i].src.split('/')[3];//
    //console.log(id);
    var aTag3 = document.createElement('a');
    //Cargar clase del enlace
    aTag3.setAttribute('class','enlaces-fotos-info');
    aTag3.innerHTML = 'x';
    aTag3.setAttribute('href','/borrarinfoartistafoto/'+nombre+'/'+id);
    aTag3.setAttribute('data-toggle','confirmation');
    //Añade el elemento aTag3 despues de tarjeta[i]
    foto[i].parentNode.insertBefore(aTag3, foto[i].nextSibling);
}
$('[data-toggle=confirmation]').confirmation({
    rootSelector: '[data-toggle=confirmation]',
    popout: true,
    singleton: true,
    title: '¿Estas seguro?',
    btnOkLabel: 'Si',
});
