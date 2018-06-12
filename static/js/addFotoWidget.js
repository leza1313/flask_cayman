var cont=1;
function addFotoWidget(){
    var mas = document.getElementById('anadirfoto');

    var hr = document.createElement('hr');
    mas.parentNode.insertBefore(hr,mas);

    var label = document.createElement('label');
    label.setAttribute('for','myfoto'+cont);
    label.innerHTML = 'Titulo para foto nº'+cont+': ';
    mas.parentNode.insertBefore(label, mas);

    var inputAlt = document.createElement('input');
    inputAlt.setAttribute('type','text');
    inputAlt.setAttribute('name','alt'+cont);
    inputAlt.setAttribute('class','form-control');
    inputAlt.setAttribute('placeholder','Titulo');
    mas.parentNode.insertBefore(inputAlt, mas);

    var br = document.createElement('br');
    mas.parentNode.insertBefore(br,mas);

    var widget = document.createElement('input');
    widget.setAttribute('type','hidden');
    widget.setAttribute('role','uploadcare-uploader');
    widget.setAttribute('name','myfoto'+cont);
    cont++;
    widget.setAttribute('data-crop','510x382 minimum');
    widget.setAttribute('data-images-only','true');
    mas.parentNode.insertBefore(widget, mas);
    var br2 = document.createElement('br');
    mas.parentNode.insertBefore(br2,mas);
}

