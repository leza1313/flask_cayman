document.getElementById("cover").style.textAlign = "left";
turn = document.getElementById("turn");
var urlBase= 'http://localhost:5000/api/';
//var urlBase= 'https://leza1313.hopto.org/api/';

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


//Intento de hacer loading screen
var loadingScreen = {
	scene: new THREE.Scene(),
	camera: new THREE.PerspectiveCamera(90, 1280/720, 0.1, 100),
	sphere: new THREE.Mesh(
		new THREE.SphereGeometry( 0.15, 0.15, 0.15 ),
		new THREE.MeshBasicMaterial({ color:0xbbbbbb })
	)

};
var loadingManager = null;
var RESOURCES_LOADED = false;

// Set up the loading screen's scene.
// It can be treated just like our main scene.
loadingScreen.sphere.position.set(0,0,5);
loadingScreen.camera.lookAt(loadingScreen.sphere.position);
loadingScreen.scene.add(loadingScreen.sphere);

// Create a loading manager to set RESOURCES_LOADED when appropriate.
// Pass loadingManager to all resource loaders.
loadingManager = new THREE.LoadingManager();

loadingManager.onProgress = function(item, loaded, total){
    console.log(item, loaded, total);
};

loadingManager.onLoad = function(){
    console.log("loaded all resources");
		RESOURCES_LOADED = true;
};
//FIN de loading screen
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
piezasguitarra=[];
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
modalName[12]='#modalChapa';
modalName[13]='#modalJack';

var loader = new THREE.STLLoader(loadingManager);
var loaderJSON = new THREE.JSONLoader(loadingManager);

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
                shininess: 20,//con esto parece que refleja, pero como que ciega un poco
                specular: 0x444444,//con esto parece que refleja
                name: myMaterial.split('texturas/')[1].split('-')[1].split('.')[0],
                color: 0xbbbbbb,
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
                if (sufix==0){
                    actualizarDropMaderas(modalName,pieza);
                }
            }
            object.borrar = function (){
                scene.remove(object);
            }

            scene.add( object );
            miguitarra[sufix]=object;
            piezasguitarra[sufix]=pieza;
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

//cambiarTextura(event, miguitarra,1,'static/modelos/stratocaster/texturas/golpeador2.jpg','#modalGolpeador0')
function cambiarTextura(event,obj,parte,nuevo,modalName){
    event.preventDefault();
    $(modalName).modal('hide');
    var urlMatViejo=urlBase + "precio3D/" + piezasguitarra[parte] + "/" + obj[parte].material.name;
    var material2 = new THREE.MeshPhongMaterial({ transparent: false,
        map: THREE.ImageUtils.loadTexture(nuevo),
        shininess: 20,//con esto parece que refleja, pero como que ciega un poco
        specular: 0x444444,//con esto parece que refleja
        name: nuevo.split('/texturas/')[1].split('-')[1].split('.')[0],
        color: 0xbbbbbb,
    });
    obj[parte].material= material2;
    //Cuerpo, si cambia textura no se cambia precio. Solo cambio de modelo, o seleccion de madera
    if(parte==3 || parte==2) {
        //Diapason y mastil, si cambia textura cambia precio
        var material = nuevo.split('/texturas/')[1].split('-')[1].split('.')[0];
        var precioNuevo;
        var precioViejo;
        $('#precio').before('<div id="loaderPrecio" class="loaderPrecio"></div>');
        $('#precio').hide()
        $.when(ajax1(),ajax2()).done(function (a1,a2) {
            $('#precio').show()
            $('#loaderPrecio').remove()
            actualizarPrecio(precioViejo[0].precio, precioNuevo[0].precio);
        });
        function ajax1() {
            return $.ajax({
                    url: urlBase + "precio3D/" + piezasguitarra[parte] + "/" + material,
                    dataType: "json",    // Work with the response
                    crossdomain: true,
                    success: function (response) {
                        precioNuevo = response;
                    },
                    error: function (response) {
                        console.log('ERROR');
                    }
                });
            }
        function ajax2() {
            return $.ajax({
                url: urlMatViejo,
                dataType: "json",    // Work with the response
                crossdomain: true,
                success: function (response) {
                    precioViejo = response;
                },
                error: function (response) {
                    console.log('ERROR');
                }
            });
        }
    }
}

function iluminar(parte){
    parte.currentHex = parte.material.emissive.getHex();
    parte.material.emissive.setHex( 0x772200);
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


var t=0;
var texto=0;
var animate = function () {
    if( RESOURCES_LOADED == false ){
		requestAnimationFrame(animate);
		if (texto==0){
		    $('#cover').append('<div id="carga" style=" color: #bbbbbb;position: absolute; top: 51%;right: 8%;width: 100%;text-align: center;z-index: 10000;display:block;">Cargando</div>');
		    texto=1;
        }


		//loadingScreen.sphere.rotation.x += 0.005;
        //loadingScreen.sphere.rotation.y += 0.005;
        t += 0.05;
        loadingScreen.sphere.position.x = 2*Math.cos(t) + 0;
        loadingScreen.sphere.position.y = 2*Math.sin(t) + 0;
		//loadingScreen.sphere.position.x -= 0.05;
		//if( loadingScreen.sphere.position.x < -10 ) loadingScreen.sphere.position.x = 10;
		//loadingScreen.sphere.position.y = Math.sin(loadingScreen.sphere.position.x);

		renderer.render(loadingScreen.scene, loadingScreen.camera);
		return; // Stop the function here.
    }
    if (texto==1){
        $('#carga').remove();
        texto=0;
    }

    requestAnimationFrame( animate );
    controls.update();

    renderer.render(scene, camera);
    render();
};

animate();

var opciones3D;

/*var precios3D;
$.ajax({
    url: urlBase+"precios3D/1",
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
$.when(ajaxP1(),ajaxP2()).done(function (a1,a2) {
    var myposicion= {'x':partes3D[0].x,'y':partes3D[0].y,'z':partes3D[0].z};
    var myposicionPastillaMastil= {'x':partes3D[4].x,'y':partes3D[4].y,'z':partes3D[4].z};
    var myposicionTono2= {'x':partes3D[9].x,'y':partes3D[9].y,'z':partes3D[9].z};
    var myposicionPuente= {'x':partes3D[7].x,'y':partes3D[7].y,'z':partes3D[7].z};

    cargarJSON(partes3D[0].pieza,partes3D[0].rutaJSON,opciones3D[0].rutaTextura,0,myposicion,partes3D[0].id,'#modalCuerpo0');
    cargarJSON(partes3D[1].pieza,partes3D[1].rutaJSON,opciones3D[2].rutaTextura,1,myposicion,partes3D[1].id,'#modalGolpeador0');
    cargarJSON(partes3D[2].pieza,partes3D[2].rutaJSON,opciones3D[3].rutaTextura,2,myposicion,partes3D[2].id,'#modalMastil0');
    cargarJSON(partes3D[3].pieza,partes3D[3].rutaJSON,opciones3D[7].rutaTextura,3,myposicion,partes3D[3].id,'#modalDiapason0');
    cargarJSON(partes3D[4].pieza,partes3D[4].rutaJSON,opciones3D[6].rutaTextura,4,myposicionPastillaMastil,partes3D[4].id,'#modalPastillaMastil0');
    cargarJSON(partes3D[5].pieza,partes3D[5].rutaJSON,opciones3D[9].rutaTextura,5,myposicion,partes3D[5].id,'#modalPastillaMedio0');
    //cargarJSON(partes3D[6].pieza,partes3D[6].rutaJSON,opciones3D[].rutaTextura,6,myposicion,partes3D[6].id,'#modalPastillaPuente0');
    //cargarJSON(partes3D[7].pieza,partes3D[7].rutaJSON,opciones3D[12].rutaTextura,7,myposicionPuente,partes3D[7].id,'#modalPuente0');
    cargarJSON(partes3D[8].pieza,partes3D[8].rutaJSON,opciones3D[14].rutaTextura,8,myposicion,partes3D[8].id,'#modalTono10');
    cargarJSON(partes3D[9].pieza,partes3D[9].rutaJSON,opciones3D[16].rutaTextura,9,myposicionTono2,partes3D[9].id,'#modalTono20');
    cargarJSON(partes3D[10].pieza,partes3D[10].rutaJSON,opciones3D[18].rutaTextura,10,myposicion,partes3D[10].id,'#modalVolumen0');
    cargarJSON(partes3D[11].pieza,partes3D[11].rutaJSON,opciones3D[20].rutaTextura,11,myposicion,partes3D[11].id,'#modalTapa0');
    cargarJSON(partes3D[12].pieza,partes3D[12].rutaJSON,opciones3D[22].rutaTextura,12,myposicion,partes3D[12].id,'#modalChapa0');
    cargarJSON(partes3D[13].pieza,partes3D[13].rutaJSON,opciones3D[23].rutaTextura,13,myposicion,partes3D[13].id,'#modalJack0');
});
function ajaxP1() {
    return $.ajax({
        url: urlBase+"partes3D/",
        dataType: "json",    // Work with the response
        crossdomain: true,
        success: function (response) {
            partes3D = response;
        },
        error: function (response) {
            console.log('ERROR');
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
        }
    });
}
function ajaxP2() {
    return  $.ajax({
            url: urlBase+"todasOpciones3D/",
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                opciones3D = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
}



function actualizarPrecio(restarPrecio,sumarPrecio) {
    precio=$('#precio').html()-restarPrecio+sumarPrecio;
    $('#precio').html(precio);
}
function actualizarBody2(pieza,modalname){
    $(modalname+'Body2').before('<div id="loaderBody2" class="loader"></div>');
    $(modalname+'Body2').hide();
    //Peticion ajax
    $.when(ajax1()).done(function (a1) {
        $(modalname+'Body2').show();
        $('#loaderBody2').remove();
        var html='';
        for (var i=0;i<opciones3D.length;i++) {
            html=html.concat('<a onclick="cambiarTextura(event, miguitarra,'+String(Number(pieza)-1)+',');
            html=html.concat("'"+opciones3D[i].rutaTextura+"'");
            html=html.concat(',\''+modalname+'\')');
            html=html.concat('"><img src=static/img/'+opciones3D[i].foto+' ' );
            html=html.concat('data-toggle='+modalname+' data-dismiss=\'modal\' width=\'200\'>' );
            html=html.concat('</a>');
        }
        $(modalname+'Body2').html(html);
    });
    function ajax1(){
        return $.ajax({
            url: urlBase+"opciones3D/"+pieza,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                opciones3D = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
function actualizarDropMaderas(modalname,parte3D){
    var precios3D;
    var html=$(modalname+'Header2').html();
    $.when(ajax1()).done(function (a1){
        html=$(modalname+'Header2').html();
        html=html.concat(' - ');
        $(modalname+'Header2').html(html);
        html=$(modalname+'Header2').html().split(' - ')[0];
        html=html.concat(' - ');
        html=html.concat('<select>');
        for (var i=0;i<precios3D.length;i++){
            html=html.concat('<option value="'+precios3D[i].material+'">'+precios3D[i].material+' '+precios3D[i].precio+'€</option>');
        }
        html=html.concat('</select>');
        $(modalname+'Header2').html(html);

    });
    function ajax1(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+parte3D,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                precios3D = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }


    /*setTimeout(function(){
        //Tiempo que espera para ejecutar el codigo de arriba, igual hay que anadir algo mas
    }, 400);*/
}

function hacerGloss(material){
    material.setValues({shininess: 100,color: 0xbbbbbb,specular:0x999999});
}
function hacerMate(material){
    material.setValues({shininess: 20,color: 0xbbbbbb,specular:0x444444});
}