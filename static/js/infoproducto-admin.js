//Codigo que añade un salto de linea, enlace <a href> y concatena el contenido al enlace para pasar parametros por GET
var nombreoriginal = document.getElementById('product-nombre');

var aTag = document.createElement('a');
//Cargar enlaces en href
aTag.setAttribute('href','');
aTag.setAttribute('data-toggle','modal');
aTag.setAttribute('data-target','#mimodal');
aTag.setAttribute('class',"enlaces");
//Cargar el texto entre etiquetas
aTag.innerHTML = "<br>Editar";
//Añadir la etiqueta al elemento tarjeta
nombreoriginal.appendChild(aTag);
