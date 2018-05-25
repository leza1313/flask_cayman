document.getElementById("cover").style.textAlign = "left";
turn = document.getElementById("turn");

var show = function() {
 if (screen.orientation.type == 'portrait'){
     turn.style.display = 'block';
     //alert('Gira el movil, porfavor');
 }else if (screen.orientation.type == 'portrait-primary'){
     turn.style.display = 'block';
     //alert('Gira el movil, porfavor');
 }else if (screen.orientation.type == 'portrait-secondary'){
     turn.style.display = 'block';
     //alert('Gira el movil, porfavor');
 }else{
     turn.style.display = 'none';
 }
}
screen.orientation.addEventListener("change", show);
window.onload = show;
var canvas = document.getElementById('mycanvas');
function resizeCanvas() {
    canvas.width = window.innerWidth*0.815;
    canvas.height = window.innerHeight*0.915;
    return [canvas.width,canvas.height];
}
function mobileCanvas() {
    canvas.width = window.innerWidth*1;
    canvas.height = window.innerHeight*0.815;
    return [canvas.width,canvas.height];
}

var renderer = new THREE.WebGLRenderer({canvas: canvas});
var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera( 50, canvas.width/canvas.height, 0.01, 1000 );


document.body.appendChild( renderer.domElement );

camera.position.set( 0, 0, 40 );
camera.rotation.set( 0, 0, 0 );

window.addEventListener( 'resize', onWindowResize, false );
window.addEventListener( 'orientationchange', onWindowResize, false );


if (window.innerWidth<450){

    tamano=mobileCanvas();
    canvas.width = tamano[0];
    canvas.height = tamano[1];
    renderer.setViewport(0, 0, canvas.width, canvas.height);
    renderer.setSize( canvas.width, canvas.height );
    camera.aspect = canvas.width / canvas.height;
    camera.updateProjectionMatrix();
}else {

    tamano=resizeCanvas();
    canvas.width = tamano[0];
    canvas.height = tamano[1];
    renderer.setViewport(0, 0, canvas.width, canvas.height);
    renderer.setSize( canvas.width, canvas.height );
    camera.aspect = canvas.width / canvas.height;
    camera.updateProjectionMatrix();
}


function onWindowResize(){
    if (window.innerWidth<450){

        tamano=mobileCanvas();
        canvas.width = tamano[0];
        canvas.height = tamano[1];
        renderer.setViewport(0, 0, canvas.width, canvas.height);
        renderer.setSize( canvas.width, canvas.height );
        camera.aspect = canvas.width / canvas.height;
        camera.updateProjectionMatrix();
    }else {

        tamano=resizeCanvas();
        canvas.width = tamano[0];
        canvas.height = tamano[1];
        renderer.setViewport(0, 0, canvas.width, canvas.height);
        renderer.setSize( canvas.width, canvas.height );
        camera.aspect = canvas.width / canvas.height;
        camera.updateProjectionMatrix();
    }

}
scene.background = new THREE.Color( 0x72645b );

//Añadir Luz

var amlight = new THREE.AmbientLight( 0xffffff, 0.4);
var light = new THREE.PointLight( 0xffffff, 0.5, 0 );
light.position.copy( camera.position );
light.castShadow = true;
scene.add( light );
scene.add( amlight );

//Set up shadow properties for the light
light.shadow.mapSize.width = 512;  // default
light.shadow.mapSize.height = 512; // default
light.shadow.camera.near = 0.5;       // default
light.shadow.camera.far = 500      // default

controls = new THREE.OrbitControls(camera,renderer.domElement);
controls.rotateSpeed = 0.5;
controls.enableDamping = true;
controls.dampingFactor = 0.25;
controls.enableZoom = true;

//Luz que se fije con la camara, como si la luz seguiria siempre en donde la camara mira
controls.addEventListener( 'change', light_update );

function light_update()
{
    light.position.copy( camera.position );
}

function vistaEnfrente(){
    camera.position.set(0,0,40);
    //group.rotation.y =0;
}
function vistaTrasera(){
    camera.position.set(0,0,-40);
    camera.rotation.set(0,180,0);
    //group.rotation.y =0;
}

isRotate=0;

function rotar(miobjeto){
    enlaces=document.getElementsByClassName('editor-a');
    for (i = 0; i < 4; i++){
        enlaces[i].setAttribute('data-toggle','hola');
    }

    for (var index in miobjeto){
        var pieza = miobjeto[index];
        pieza.borrar();
        group.add(pieza);
    }
    scene.add(group);

    rotateAll(group);
    document.getElementById( "rotar" ).setAttribute( "onClick", "parar();" );
    document.getElementById( "rotar" ).innerHTML='Parar';
    document.getElementById( "rotar" ).classList.add('btn-danger');
}

function parar(){
    enlaces=document.getElementsByClassName('editor-a');
    for (i = 0; i < 4; i++){
        enlaces[i].setAttribute('data-toggle','modal');
    }
    mirotation=group.rotation.y;
    scene.remove(group);
    for (var index in miguitarra){
        var pieza = miguitarra[index];
        scene.add(pieza);
    }
    isRotate=0;
    document.getElementById( "rotar" ).setAttribute( "onClick", "rotar(miguitarra);" );
    document.getElementById( "rotar" ).innerHTML='Rotar';
    document.getElementById( "rotar" ).classList.remove('btn-danger');
}

var SPEED = 0.01;

group = new THREE.Group();

function rotateAll(migroup) {
    isRotate = 1;
    migroup.rotation.y -= SPEED*2;
}

/*
// Define a class like this
function Person(name, gender){

   // Add object properties like this
   this.name = name;
   this.gender = gender;
}

// Add methods like this.  All Person objects will be able to invoke this
Person.prototype.speak = function(){
    alert("Howdy, my name is" + this.name);
};

// Instantiate new objects with 'new'
var person = new Person("Bob", "M");

// Invoke methods like this
//person.speak(); // alerts "Howdy, my name is Bob"
//*/

function myposition(x,y,z){
    this.x=x;
    this.y=y;
    this.z=z;
}

/*
function myguitarrastl(cuerpo,golpeador,mastil,p_mastil,p_medio,p_puente,puente,per_tono,per_tono2,per_volumen){
    this.cuerpo=cuerpo;
    this.golpeador=golpeador;
    this.mastil=mastil;
    this.p_mastil=p_mastil;
    this.p_medio=p_medio;
    this.p_puente=p_puente
    this.puente=puente;
    this.per_tono=per_tono;
    this.per_tono2=per_tono2;
    this.per_volumen=per_volumen;
}
function mypastillas(mastil,medio,puente){
    this.mastil=mastil;
    this.medio=medio;
    this.puente=puente;
}
function myperillas(tono,tono2,volumen){
    this.tono=tono;
    this.tono2=tono2;
    this.volumen=volumen;
}

function mypositionstl(cuerpo,golpeador,mastil,p_mastil,p_medio,p_puente,puente,per_tono,per_tono2,per_volumen){
    this.cuerpo=cuerpo;
    this.golpeador=golpeador;
    this.mastil=mastil;
    this.p_mastil=p_mastil;
    this.p_medio=p_medio;
    this.p_puente=p_puente
    this.puente=puente;
    this.per_tono=per_tono;
    this.per_tono2=per_tono2;
    this.per_volumen=per_volumen;
}

peri = new myperillas('static/modelos/stratocaster/TONO_1.STL',
    'static/modelos/stratocaster/TONO_2.STL',
    'static/modelos/stratocaster/VOLUMEN.STL');

pasti = new mypastillas('static/modelos/stratocaster/PASTILLA_MASTIL.STL',
    'static/modelos/stratocaster/PASTILLA_MEDIO.STL',
    'static/modelos/stratocaster/PASTILLA_PUENTE.STL');
//telecaster/CUERPO TELECASTER
//stratocaster/CUERPO
guitarra = new myguitarrastl('static/modelos/stratocaster/CUERPO.STL',
    'static/modelos/stratocaster/GOLPEADOR.STL',
    'static/modelos/stratocaster/MASTIL.STL',
    pasti.mastil,pasti.medio,pasti.puente,
    'static/modelos/stratocaster/PUENTE.STL',
    peri.tono,peri.tono2,peri.volumen);

posicionstl= new mypositionstl( //Cuerpo
                                new myposition(5, 10, -20.75),
                                //Golpeador
                                new myposition(4.95, 4.778, 3),
                                //Mastil
                                new myposition(30.8, 2.88, 2.09),
                                //Pastillas
                                new myposition(4.9,3.2, 2.65),
                                new myposition(4.9,3.2, 2.65),
                                new myposition(4.9,3.2, 2.65),
                                //Puente
                                new myposition(5,3.1, 0.97),
                                //Perillas
                                new myposition(4.943,-1.033, 3.067),
                                new myposition(4.943,-1.033, 3.067),
                                new myposition(4.943,-1.033, 3.067)
);
*/
miguitarra=[];
/*
function Miguitarra(cuerpo,golpeador,mastil,p_mastil,p_medio,p_puente,puente,per_tono,per_tono2,per_volumen){
    this.cuerpo=cuerpo;
    this.golpeador=golpeador;
    this.mastil=mastil;
    this.p_mastil=p_mastil;
    this.p_medio=p_medio;
    this.p_puente=p_puente
    this.puente=puente;
    this.per_tono=per_tono;
    this.per_tono2=per_tono2;
    this.per_volumen=per_volumen;
}
prueba = new Miguitarra();*/
/*
//Estos metodos no consiguen hacer que cargue/devuelva los objetos dentro del js.
//Desde afuera (funciones llamadas desde html) es igual utilizar el set o get Cuerpo que prueba.cuerpo
Miguitarra.prototype.setCuerpo = function(micuerpo){
    this.cuerpo=micuerpo;
};
Miguitarra.prototype.getCuerpo = function(){
    console.log(this.cuerpo);
    return this.cuerpo;
};*/

materiales=[];
materiales[0] = new THREE.MeshPhongMaterial( { color: 0xffaa00} );
materiales[1] = new THREE.MeshPhongMaterial( { color: 0x00aaff} );
materiales[2] = new THREE.MeshPhongMaterial( { color: 0x00ff6c} );
materiales[3] = new THREE.MeshPhongMaterial( { color: 0xd8ff00} );
materiales[4] = new THREE.MeshPhongMaterial( { color: 0x588600} );
materiales[5] = new THREE.MeshPhongMaterial( { color: 0x001cf7} );
materiales[6] = new THREE.MeshPhongMaterial( { color: 0xa900f4} );
materiales[7] = new THREE.MeshPhongMaterial( { color: 0xf400e1} );
materiales[8] = new THREE.MeshPhongMaterial( { color: 0xf40067} );
materiales[9] = new THREE.MeshPhongMaterial( { color: 0xf40000} );

modalName=[];
modalName[0]='#modalModelo';
modalName[1]='#modalGolpeador';
modalName[2]='#modalMastil';
modalName[3]='#modalDiapason';
modalName[4]='#modalPastilla_Mastil';
modalName[5]='#modalPastilla_Medio';
modalName[6]='#modalPastilla_Puente';
modalName[7]='#modalPuente';
modalName[8]='#modalTono_1';
modalName[9]='#modalTono_2';
modalName[10]='#modalVolumen';
modalName[11]='#modalTapa';

var loader = new THREE.STLLoader();
var loaderJSON = new THREE.JSONLoader();

/*
function cargarSTL(mystl,myMaterial,sufix,position,modalName) {

    loader.load(mystl, function (geometry) {
        var myObject = new THREE.Mesh(geometry, myMaterial);
        myObject.scale.set(0.05, 0.05, 0.05);
        myObject.position.set(position.x, position.y, position.z);
        myObject.rotation.set(THREE.Math.degToRad(90), THREE.Math.degToRad(-90), THREE.Math.degToRad(0));

        myObject.callback = function () {
            $(modalName).modal();
        }
        myObject.borrar = function () {
            scene.remove(myObject);
        }
        //Si intento mostrar el objeto desde JS fuera de la funcion no funciona
        //Sin embargo, al llamar a otras funciones de JS desde HTML si que reconoce el objeto.
        scene.add(myObject);
        miguitarra[sufix] = myObject;
        //Si de aqui guardo por cada iteracion la pieza correspondiente en el objeto de clase Miguitarra
        // Desde afuera(el html) puedo llamar a funciones pasando como argumento el objeto.cuerpo (prueba.cuerpo)
        //prueba.cuerpo=myObject;
    });
}*/
function cargarJSON(nombre,mystl,myMaterial,sufix,position,pieza,modalName){


    loaderJSON.load(mystl,

        //TODO load the 1st option for that part in "opcionesPartes3D" db
        function onLoad( geometry, materials ) {
            var material = new THREE.MeshPhongMaterial({ transparent: false,
                map: THREE.ImageUtils.loadTexture(myMaterial),
                shininess: 30,//con esto parece que refleja, pero como que ciega un poco
                specular: 0x444444,//con esto parece que refleja
                //color: 0xffffff,
                //roughness: 0.5,//esto es para MeshStandardMaterial, agranda o achica el foco
                //metalness: 0.8//esto es para MeshStandardMaterial, cantidad de luz que devuelve
            });

            var object = new THREE.Mesh( geometry, material );
            object.name=nombre;
            //object.position.set( 22.52, 12.46, 0);
            object.scale.set( 0.05, 0.05, 0.05);
            object.position.set(position.x, position.y, position.z);
            object.rotation.set( THREE.Math.degToRad(-180),THREE.Math.degToRad(0), THREE.Math.degToRad(90));
            object.callback = function(){
                $(modalName).modal();
                actualizarBody2(pieza,modalName);
            }
            object.borrar = function (){
                scene.remove(object);
            }
            scene.add( object );
            miguitarra[sufix]=object;
        },

        // onProgress callback
        function onProgress( xhr ) {
            console.log( (xhr.loaded / xhr.total * 100) + '% loaded' );
        },

        // onError callback
        function onError( err ) {
            console.error( 'An error happened' );
    });
}
var counter=0;
/*
for(var index in guitarra) {
    var attr = guitarra[index];
    if (counter!=0){
    cargarSTL(attr,materiales[counter],counter,posicionstl[index],modalName[counter]);}
    counter++;
}*/
//cargarJSON('static/modelos/prueba/strat cuerpo.json',materiales[0],0,posicionstl.cuerpo,'#modalCuerpo0');

function cambiarCuerpo(event,obj,parte,nuevo,modalName){
    //hace falta poner el event.preventDefault()
    //y pasarselo a la funcion tmbn
    event.preventDefault();
    $(modalName).modal('hide');
    obj[parte].borrar();
    //obj[1].borrar();
    cargarSTL(nuevo,obj[parte].material,0,posicionstl.cuerpo,modalName);
}
function cambiarTextura(event,obj,parte,nuevo,modalName){
    //hace falta poner el event.preventDefault()
    //y pasarselo a la funcion tmbn
    event.preventDefault();
    $(modalName).modal('hide');
    console.log(nuevo);
    var material2 = new THREE.MeshPhongMaterial({ transparent: false,
        map: THREE.ImageUtils.loadTexture(nuevo),
        shininess: 30,//con esto parece que refleja, pero como que ciega un poco
        specular: 0x444444,//con esto parece que refleja
        //color: 0xffffff,
        //roughness: 0.5,//esto es para MeshStandardMaterial, agranda o achica el foco
        //metalness: 0.8//esto es para MeshStandardMaterial, cantidad de luz que devuelve
    });
    obj[parte].material= material2;
    //modeloGuit = nuevo.split('modelos/')[1].split('/')[0];
    //acabadoParte = nuevo.split('modelos/')[1].split('/')[1];
    actualizarPrecio(250,100);
}

function iluminar(parte){
    parte.currentHex = parte.material.emissive.getHex();
    parte.material.emissive.setHex( 0x333333 );
}
function apagar(parte){
    parte.material.emissive.setHex(parte.currentHex );
}

//Colorear el objeto que esta debajo del raton.
{
//Raycaster para seleccionar con el raton
var raycaster = new THREE.Raycaster();
var mouse = new THREE.Vector2();
var INTERSECTED;

function onDoubleClick( event ) {
    event.preventDefault();

    mouse.x = ( event.offsetX/ canvas.clientWidth ) * 2 - 1;
    mouse.y = - ( event.offsetY / canvas.clientHeight ) * 2 + 1;

    raycaster.setFromCamera( mouse, camera );

    var intersects = raycaster.intersectObjects( scene.children);

    if ( intersects.length > 0 ) {

        intersects[0].object.callback();

    }

}

function onMouseMove( event ) {
    // calculate mouse position in normalized device coordinates
    // (-1 to +1) for both components
    event.preventDefault();

    mouse.x = ( event.offsetX / canvas.clientWidth) * 2 - 1;
    mouse.y = - ( event.offsetY / canvas.clientHeight ) * 2 + 1;

}
function seIlumina(intersects){
    //Se ilumina el objeto Seleccionado
    if ( intersects.length > 0 ) {
        if ( INTERSECTED != intersects[ 0 ].object ) {
            if ( INTERSECTED ) apagar(INTERSECTED);
            INTERSECTED = intersects[ 0 ].object;
            iluminar(INTERSECTED);
        }
    } else {
        if ( INTERSECTED ) apagar(INTERSECTED);
        INTERSECTED = null;
    }
}

function render() {
    // update the picking ray with the camera and mouse position
    raycaster.setFromCamera( mouse, camera );
    // calculate objects intersecting the picking ray
    var intersects = raycaster.intersectObjects( scene.children );
    seIlumina(intersects);
    if (isRotate==1){ rotateAll(group)}

    renderer.render( scene, camera );
}

window.addEventListener( 'mousemove', onMouseMove, false );
renderer.domElement.ondblclick=onDoubleClick;
window.requestAnimationFrame(render);

}



var animate = function () {
    requestAnimationFrame( animate );
    controls.update();

    renderer.render(scene, camera);
    render();
};

animate();

var opciones3D;
function getOpciones3D(pieza){
    $.ajax({
    url: "http://localhost:5000/api/opciones3D/"+pieza,
    dataType: "jsonp",    // Work with the response
    success: function (response) {
        //$('#precio').html('555');
        console.log('AJAX SUCCESS - Revisar codigo');
        opciones3D = JSON.parse(response.responseText);
    },
    error: function (response) {
        //console.log('ERROR');
        opciones3D = JSON.parse(response.responseText);
        console.log(opciones3D);
        //return opciones3D;
    }
    });
}
/*var precios3D;
$.ajax({
    url: "http://localhost:5000/api/precios3D/1",
    dataType: "jsonp",    // Work with the response
    success: function (response) {
        $('#precio').html('555');
        console.log('A');
        console.log(response); // server response
    },
    error: function (response) {
        //console.log('ERROR');
        opciones3D = JSON.parse(response.responseText);
    }
});*/

var partes3D;
$.ajax({
    url: "http://localhost:5000/api/partes3D/",
    dataType: "jsonp",    // Work with the response
    success: function (response) {
        $('#precio').html('555');
        console.log('A');
        console.log(response); // server response
    },
    error: function (response) {
        //console.log('ERROR');
        //TODO cargar el resto de piezas de la primera guitarra (por defecto) aqui.
        // Una vez cargado la primera guitarra tras la peticion AJAX,
        // Ya tenemos todas las partes3D en la variable.
        // Una vez se hace un cambio de modelo json, cambiar con javascript el modal
        //
        // Si se cambia el cuerpo cambiar modal entero
        //
        // Si se cambia cualquier otra pieza solo cambiar las opciones del modal de esa pieza.
        // Para esto hacer una peticion AJAX al server para saber las opciones de esa pieza
        // /api/opciones3D/<string:parte3D>
        partes3D = JSON.parse(response.responseText);
        var myposicion= {'x':partes3D[0].x,'y':partes3D[0].y,'z':partes3D[0].z};
        var myposicionPastillaMastil= {'x':partes3D[4].x,'y':partes3D[4].y,'z':partes3D[4].z};


        $.ajax({
            url: "http://localhost:5000/api/todasOpciones3D/",
            dataType: "jsonp",    // Work with the response
            success: function (response) {
                //$('#precio').html('555');
                console.log('AJAX SUCCESS - Revisar codigo');
                opciones3D = JSON.parse(response.responseText);
            },
            error: function (response) {
                //console.log('ERROR');
                opciones3D = JSON.parse(response.responseText);
                console.log(opciones3D);
                //return opciones3D;
            }
        });

        setTimeout(function () {
            cargarJSON(partes3D[0].pieza,partes3D[0].rutaJSON,opciones3D[0].rutaTextura,0,myposicion,partes3D[0].id,'#modalCuerpo0');
            cargarJSON(partes3D[1].pieza,partes3D[1].rutaJSON,opciones3D[2].rutaTextura,1,myposicion,partes3D[1].id,'#modalGolpeador0');
            cargarJSON(partes3D[2].pieza,partes3D[2].rutaJSON,opciones3D[3].rutaTextura,2,myposicion,partes3D[2].id,'#modalMastil0');
            cargarJSON(partes3D[3].pieza,partes3D[3].rutaJSON,opciones3D[7].rutaTextura,3,myposicion,partes3D[3].id,'#modalDiapason0');
            cargarJSON(partes3D[4].pieza,partes3D[4].rutaJSON,opciones3D[6].rutaTextura,4,myposicionPastillaMastil,partes3D[4].id,'#modalPastillaMastil0');
            cargarJSON(partes3D[5].pieza,partes3D[5].rutaJSON,opciones3D[9].rutaTextura,5,myposicion,partes3D[5].id,'#modalPastillaMedio0');
        },1000);


    }
});


function actualizarPrecio(restarPrecio,sumarPrecio) {
    precio=$('#precio').html()-restarPrecio+sumarPrecio;
    $('#precio').html(precio);
}
function actualizarBody2(pieza,modalname){
    getOpciones3D(pieza);
    //qw = JSON.parse(opciones3D.responseText);
    setTimeout(function(){
    //do what you need here
        //console.log(opciones3D);
        var html='';
        for (var i=0;i<opciones3D.length;i++) {
            html=html.concat('<a onclick="cambiarTextura(event, miguitarra,'+String(Number(pieza)-1)+',');
            html=html.concat("'"+opciones3D[i].rutaTextura+"'");
            html=html.concat(',\''+modalname+'\')');
            html=html.concat('"><img src=static/img/'+opciones3D[i].foto+' ' );
            html=html.concat('data-toggle='+modalname+' data-dismiss=\'modal\' height=\'200\'>' );
            html=html.concat('</a>');
        }
        $(modalname+'Body2').html(html);
        /*<div id="{{ item.id }}Body1" class="modal-body">
            {% for modelo in item.opcionesModelo %}
                <script>modelo.push('{{ modelo.modelo }}')</script>
                <a onclick="cambiarCuerpo(event, miguitarra,{{ outer_loop.index-1 }},'static/modelos/{{ modelo.modelo }}',{{ item.id }})"><img src='static/img/{{ modelo.foto }}' data-toggle='{{ item.id }}' data-dismiss='modal' height='200'></a>
            {% endfor %}
        </div>*/

        //Tiempo que espera para ejecutar el codigo de arriba, igual hay que anadir algo mas
    }, 200);
}