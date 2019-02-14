document.getElementById("cover").style.textAlign = "left";
turn = document.getElementById("turn");
//var urlBase= 'http://localhost:5000/api/';
var urlBase= 'https://leza1313.hopto.org/api/';

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
    //console.log(item, loaded, total);
};

loadingManager.onLoad = function(){
    //console.log("loaded all resources");
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
    for (i = 0; i < 5; i++){
        enlaces[i].setAttribute('data-toggle','hola');
    }

    for (var index in miobjeto){
        var pieza = miobjeto[index];
        if (pieza!=null){
            pieza.borrar();
            group.add(pieza);
        }
    }
    scene.add(group);

    rotateAll(group);
    document.getElementById( "rotar" ).setAttribute( "onClick", "parar();" );
    document.getElementById( "rotar" ).innerHTML='Parar';
    document.getElementById( "rotar" ).classList.add('btn-danger');
}

function parar(){
    enlaces=document.getElementsByClassName('editor-a');
    for (i = 0; i < 5; i++){
        enlaces[i].setAttribute('data-toggle','modal');
    }
    mirotation=group.rotation.y;
    scene.remove(group);
    for (var index in miguitarra){
        var pieza = miguitarra[index];
        if (pieza != null){
            scene.add(pieza);
        }
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

function myposition(x,y,z){
    this.x=x;
    this.y=y;
    this.z=z;
}

miguitarra=[];
piezasguitarra=[];

var loader = new THREE.STLLoader(loadingManager);
var loaderJSON = new THREE.JSONLoader(loadingManager);

var miacabado;
function cargarJSON(nombre,mystl,sufix,position,pieza,modalName){

    loaderJSON.load(mystl,

        //TODO load the 1st option for that part in "opcionesPartes3D" db
        function onLoad( geometry, materials ) {
            /*var material = new THREE.MeshPhongMaterial({ transparent: false,
                map: THREE.ImageUtils.loadTexture(myMaterial),
                shininess: 20,//con esto parece que refleja, pero como que ciega un poco
                specular: 0x444444,//con esto parece que refleja
                name: 'pieza'+sufix,
                color: 0xbbbbbb,
                //roughness: 0.5,//esto es para MeshStandardMaterial, agranda o achica el foco
                //metalness: 0.8//esto es para MeshStandardMaterial, cantidad de luz que devuelve
            });*/
            var material = materials[0];
            var object = new THREE.Mesh( geometry, material );
            object.name=nombre;
            //object.position.set( 22.52, 12.46, 0);
            object.scale.set( 0.05, 0.05, 0.05);
            object.position.set(position.x, position.y, position.z);
            object.rotation.set( THREE.Math.degToRad(-180),THREE.Math.degToRad(0), THREE.Math.degToRad(90));

            object.callback = function(){
                $(modalName).modal();
                actualizarBody2(sufix,pieza,modalName);
            }
            object.borrar = function (){
                scene.remove(object);
            }

            scene.add( object );
            var oldPieza = piezasguitarra[sufix] || 5;
            miguitarra[sufix]=object;
            piezasguitarra[sufix]=pieza;
            if (sufix==0){
                miacabado='brillo';
                hacerGloss(material);
                actualizarDropMaderaCuerpo(piezasguitarra[0]);
            }else
            if (sufix==1){
                hacerMate(material);
            }else
            if (sufix==2){
                actualizarDropMaderaMastil(piezasguitarra[2]);
                hacerMate(material);
            }else
            //If the second request finish the last one, it makes de AJAX without knowing the id of the
            // diapason, so it ends with the dropDiapason empty.MOVED TO-> after cargarJSON() for 1st time
            // Now it only loads the dropDowns with the last item involved in wood selection. the Diapason
            if (sufix==3){
                actualizarDropMaderaDiapason(piezasguitarra[3]);
                hacerMate(material);
            }else
            if (sufix==4){
                actualizarDropPastillaMastil(piezasguitarra[4],oldPieza);
                hacerMate(material);
            }else
            if (sufix==5){
                actualizarDropPastillaMedio(piezasguitarra[5],oldPieza);
                hacerMate(material);
            }else
            if (sufix==6){
                actualizarDropPastillaPuente(piezasguitarra[6],oldPieza);
                hacerMate(material);
            }else
            if (sufix==7){
                hacerGloss(material);
            }else
            if (sufix==8){
                hacerMate(material);
            }else
            if (sufix==9){
                hacerMate(material);
            }else
            if (sufix==10){
                hacerMate(material);
            }else
            if (sufix==11){
                hacerMate(material);
            }else
            if (sufix==12){
                hacerGloss(material);
            }else
            if (sufix==13){
                hacerGloss(material);
            }else
            if (sufix==14){
                hacerGloss(material);
            }else
            if (sufix==15){
                hacerMate(material);
            }else
            if (sufix==16){
                hacerMate(material);
            }
        },

        // onProgress callback
        function onProgress( xhr ) {
            //console.log( (xhr.loaded / xhr.total * 100) + '% loaded' );
        },

        // onError callback
        function onError( err ) {
            console.error( 'An error happened' );
    });
    //If the part to load was null, not existed then remove the drop of the middle pickup
    if (sufix==5 && mystl==''){
        actualizarDropPastillaMedio(99,99);
    }
}
var counter=0;

function cambiarParte(event,myPartes3D,parte,pieza,position,modalname,obj){
    //hace falta poner el event.preventDefault()
    //y pasarselo a la funcion tmbn
    event.preventDefault();
    $(modalname).modal('hide');
    obj[parte].borrar();
    $.when(ajax1()).done(function (a1) {
        var index = myPartes3D.findIndex(x => x.id==pieza);
        cargarJSON(myPartes3D[index].nombre, myPartes3D[index].rutaJSON,
            parte, position, myPartes3D[index].id, modalname);
    });
    function ajax1(){
        return $.ajax({
            url: urlBase+"opciones3D/"+pieza,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                myOpciones3D = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
function cambiarModelo(event,modelo) {
    quitarGuitarra();
    cargarModeloDefecto(modelo);
    actualizarModalPastillas(4,modelo);
    actualizarModalPastillas(5,modelo);
    actualizarModalPastillas(6,modelo);
    actualizarComponentes(modelo);
}
function quitarGuitarra() {
    for (var i=0;i<=16;i++){
        if (miguitarra[i] != null){
            miguitarra[i].borrar();
            miguitarra[i]=null;
        }
    }
}

function cambiarTextura(event,obj,parte,color,nuevo,modalName){
    event.preventDefault();
    $(modalName).modal('hide');
    //var urlMatViejo=urlBase + "precio3D/" + piezasguitarra[parte] + "/" + obj[parte].material.name;
    var material2 = new THREE.MeshPhongMaterial({ transparent: false,
        map: THREE.ImageUtils.loadTexture(nuevo),
        shininess: 20,//con esto parece que refleja, pero como que ciega un poco
        specular: 0x444444,//con esto parece que refleja
        name: color,
        color: 0xbbbbbb,
    });
    //Cuerpo, si cambia textura no se cambia precio. Solo cambio de modelo, o seleccion de madera
    if(parte==3 || parte==2) {
        //Diapason y mastil, si cambia textura cambia precio y opcion del select del menu derecho
        //TODO si no es stratocaster y telecaster, hay que cambiar la ruta de la textura o NO?
        var matNuevo=nuevo.split('/texturas/')[1].split('-')[1].split('.')[0];
        if (parte==3){
            $('#dropDiapason').triggerHandler( "focus" );
            $('#dropDiapason').val(matNuevo);
            $('#dropDiapason').trigger('change');
        }else if(parte==2){
            $('#dropMastil').triggerHandler( "focus" );
            $('#dropMastil').val(matNuevo);
            $('#dropMastil').trigger('change');
        }
    }else{
        obj[parte].material= material2;
        if (parte==0){
            hacerGloss(obj[parte].material);
            miacabado='brillo';
        }else
        if (parte==7){
            hacerGloss(obj[parte].material);
        }else
        if (parte==12){
            hacerGloss(obj[parte].material);
        }else
        if (parte==13){
            hacerGloss(obj[parte].material);
        }else
        if (parte==14){
            hacerGloss(obj[parte].material);
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

        t += 0.05;
        loadingScreen.sphere.position.x = 2*Math.cos(t) + 0;
        loadingScreen.sphere.position.y = 2*Math.sin(t) + 0;

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

var partes3D;
var partes3Ddefecto;
function cargarModeloDefecto(modelo){
    $.when(ajaxP1(),ajaxP2()).done(function (a1,a2) {
        var myposicion;

        for (var i=0;i<partes3Ddefecto.length;i++){
            myposicion= {'x':partes3Ddefecto[i].x,'y':partes3Ddefecto[i].y,'z':partes3Ddefecto[i].z};
            cargarJSON(partes3Ddefecto[i].nombre, partes3Ddefecto[i].rutaJSON, i, myposicion, partes3Ddefecto[i].id, '#modal' + partes3Ddefecto[i].pieza + '0');

        }
        $('#precio').html('1500');
    });
    function ajaxP1() {
        return $.ajax({
            url: urlBase+"piezasModelo/"+modelo,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                partes3Ddefecto = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
    function ajaxP2(){
        return $.ajax({
            url: urlBase+"partes3D/",
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                partes3D = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
cargarModeloDefecto('stratocaster');
actualizarModalPastillas(4,'stratocaster');
actualizarModalPastillas(5,'stratocaster');
actualizarModalPastillas(6,'stratocaster');
actualizarComponentes('stratocaster');

function actualizarPrecio(restarPrecio,sumarPrecio) {
    precio=$('#precio').html()-restarPrecio+sumarPrecio;
    $('#precio').html(precio);
}
function actualizarBody2(parte,pieza,modalname){
    $(modalname+'Body2').before('<div id="loaderBody2" class="loader"></div>');
    $(modalname+'Body2').hide();
    //Peticion ajax
    $.when(ajax1()).done(function (a1) {
        $(modalname+'Body2').show();
        $('#loaderBody2').remove();
        var html='';
        for (var i=0;i<opciones3D.length;i++) {
            html=html.concat('<a onclick="cambiarTextura(event, miguitarra,'+parte+',');
            html=html.concat("'"+opciones3D[i].nombre+"',");
            html=html.concat("'"+opciones3D[i].rutaTextura+"'");
            html=html.concat(',\''+modalname+'\')');
            html=html.concat('"><img class=\'myimage\' src=static/img/'+opciones3D[i].foto+' ' );
            html=html.concat('data-toggle='+modalname+' data-dismiss=\'modal\' width=\'200\' height=\'115\'>' );
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
function actualizarDropMaderaCuerpo(parteCuerpo){
    var preciosCuerpo;
    var modalBody= '#dropCuerpo';
    var html=$(modalBody).html();
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax1()).done(function (a1){
        $(modalBody).show();
        $('#loaderBody3').remove();
        html='';
        html=html.concat('Escoge madera para el Cuerpo: ');
        html=html.concat('<select id="dropCuerpo" onchange="cambioMaderaCuerpo(this.value)" onfocus="valViejo(this.value)">');
        for (var i=0;i<preciosCuerpo.length;i++){
            html=html.concat('<option data-dismiss="modal" value="'+preciosCuerpo[i].material+'">'+preciosCuerpo[i].material+' '+preciosCuerpo[i].precio+'€</option>');
        }
        html=html.concat('</select><br>');
        $(modalBody).html(html);
    });
    function ajax1(){
        //TODO aqui da el fallo de JSON.parse
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+parteCuerpo,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosCuerpo = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}

function actualizarDropMaderaDiapason(parteDiapason){
    var preciosDiapason;
    var modalBody= '#dropDiapason';
    var html=$(modalBody).html();
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax2()).done(function (a2) {
        $(modalBody).show();
        $('#loaderBody3').remove();
        html = '';
        //Diapason
        html = ('<select id="dropDiapason" onchange="cambioMaderaDiapasonMastil(3,this.value)" onfocus="valViejo(this.value)">');
        for (var i = 0; i < preciosDiapason.length; i++) {
            html = html.concat('<option data-dismiss="modal" value="' + preciosDiapason[i].material + '">' + preciosDiapason[i].material + ' ' + preciosDiapason[i].precio + '€</option>');
        }
        html = html.concat('</select><br>')
        $(modalBody).html(html);
    });


    function ajax2(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+parteDiapason,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosDiapason = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}
function actualizarDropMaderaMastil(parteMastil){
    var precioMastil;
    var modalBody= '#dropMastil';
    var html=$(modalBody).html();
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax3()).done(function (a3) {
        $(modalBody).show();
        $('#loaderBody3').remove();
        html = '';
        //Mastil
        html = html.concat('Escoge madera para el Mastil: ');
        html = html.concat('<select id="dropMastil" onchange="cambioMaderaDiapasonMastil(2,this.value)" onfocus="valViejo(this.value)">');
        for (var i = 0; i < preciosMastil.length; i++) {
            html = html.concat('<option data-dismiss="modal" value="' + preciosMastil[i].material + '">' + preciosMastil[i].material + ' ' + preciosMastil[i].precio + '€</option>');
        }
        html = html.concat('</select>');
        $(modalBody).html(html);
    });
    function ajax3(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+parteMastil,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosMastil = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}
function actualizarDropPastillaMastil(partePastillaMastil,oldPieza){
    var preciosPastillaMastil,precioViejo,precioNuevo;
    var modalBody= '#dropPastillaMastil';
    var html=$(modalBody).html();
    var optOld=$(modalBody).val() || 'fender';
    var optNew;
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax1()).done(function (a1) {
        $(modalBody).show();
        $('#loaderBody3').remove();
        html = '';
        //Pastillas Mastil
        html = ('<select id="dropPastillaMastil" onchange="cambioPastillaMedio(this.value)" onfocus="valViejo(this.value)">');
        for (var i = 0; i < preciosPastillaMastil.length; i++) {
            html = html.concat('<option data-dismiss="modal" value="' + preciosPastillaMastil[i].material + '">' + preciosPastillaMastil[i].material + ' ' + preciosPastillaMastil[i].precio + '€</option>');
        }
        html = html.concat('</select><br>')
        $(modalBody).html(html);
        optNew=$(modalBody).val();

        $.when(ajax2(),ajax3()).done(function (a2,a3) {
            actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
        });
        function ajax2() {
            return $.ajax({
                    url: urlBase + "precio3D/" + piezasguitarra[4] + "/" + optNew,
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
        function ajax3() {
            return $.ajax({
                    url: urlBase + "precio3D/" + oldPieza + "/" + optOld,
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
    });
    function ajax1(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+partePastillaMastil,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosPastillaMastil = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}
function actualizarDropPastillaMedio(partePastillaMedio,oldPieza){
    var preciosPastillaMedio,precioViejo,precioNuevo;
    var modalBody= '#dropPastillaMedio';
    var html=$(modalBody).html();
    var optOld=$(modalBody).val() || 'fender';
    var optNew;
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax1()).done(function (a1) {
        $(modalBody).show();
        $('#loaderBody3').remove();
        html = '';
        //Pastillas Mastil
        html = ('<select id="dropPastillaMedio" onchange="cambioPastilla(this.value,5)" onfocus="valViejo(this.value)">');
        for (var i = 0; i < preciosPastillaMedio.length; i++) {
            html = html.concat('<option data-dismiss="modal" value="' + preciosPastillaMedio[i].material + '">' + preciosPastillaMedio[i].material + ' ' + preciosPastillaMedio[i].precio + '€</option>');
        }
        html = html.concat('</select><br>')
        $(modalBody).html(html);
        optNew=$(modalBody).val();

        $.when(ajax2(),ajax3()).done(function (a2,a3) {
            actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
        });
        function ajax2() {
            return $.ajax({
                    url: urlBase + "precio3D/" + piezasguitarra[5] + "/" + optNew,
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
        function ajax3() {
            return $.ajax({
                    url: urlBase + "precio3D/" + oldPieza + "/" + optOld,
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
    });
    function ajax1(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+partePastillaMedio,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosPastillaMedio = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}
function actualizarDropPastillaPuente(partePastillaPuente,oldPieza){
    var preciosPastillaPuente,precioViejo,precioNuevo;
    var modalBody= '#dropPastillaPuente';
    var html=$(modalBody).html();
    var optOld=$(modalBody).val() || 'fender';
    var optNew;
    $(modalBody).before('<div id="loaderBody3" class="loader"></div>');
    $(modalBody).hide();
    $.when(ajax1()).done(function (a1) {
        $(modalBody).show();
        $('#loaderBody3').remove();
        html = '';
        //Pastillas Mastil
        html = ('<select id="dropPastillaPuente" onchange="cambioPastilla(this.value,6)" onfocus="valViejo(this.value)">');
        for (var i = 0; i < preciosPastillaPuente.length; i++) {
            html = html.concat('<option data-dismiss="modal" value="' + preciosPastillaPuente[i].material + '">' + preciosPastillaPuente[i].material + ' ' + preciosPastillaPuente[i].precio + '€</option>');
        }
        html = html.concat('</select><br>')
        $(modalBody).html(html);
        optNew=$(modalBody).val();

        $.when(ajax2(),ajax3()).done(function (a2,a3) {
            actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
        });
        function ajax2() {
            return $.ajax({
                    url: urlBase + "precio3D/" + piezasguitarra[6] + "/" + optNew,
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
        function ajax3() {
            return $.ajax({
                    url: urlBase + "precio3D/" + oldPieza + "/" + optOld,
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
    });
    function ajax1(){
        //Loading...
        return $.ajax({
            url: urlBase+"todosPrecio3D/"+partePastillaPuente,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                preciosPastillaPuente = response;
            },
            error: function (response) {
                console.log('ERROR');
                //precios3D = response;
            }
        });
    }
}
function hacerGloss(material){
    miacabado='brillo';
    material.setValues({shininess: 100,color: 0xbbbbbb,specular:0x999999});
}
function hacerMate(material){
    miacabado='mate';
    material.setValues({shininess: 20,color: 0xbbbbbb,specular:0x444444});
}
function valViejo(val) {
    $(this).data('val', val);
}
function cambioMaderaCuerpo(val){
    var oldValue = $(this).data('val');
    var newValue= val;
    var precioViejo;
    var precioNuevo;
    $('#precio').before('<div id="loaderPrecio" class="loaderPrecio"></div>');
    $('#precio').hide()
    $.when(ajax1(),ajax2()).done(function (a1,a2) {
        $('#precio').show()
        $('#loaderPrecio').remove()
        actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
    });
    function ajax1() {
        return $.ajax({
                url: urlBase + "precio3D/" + piezasguitarra[0] + "/" + oldValue,
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
    function ajax2() {
        return $.ajax({
            url: urlBase + "precio3D/" + piezasguitarra[0] + "/" + newValue,
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
}
function cambioMaderaDiapasonMastil(DoM,val){
    //DoM= Diapason = 3 o Mastil = 2
    //It's the number of item in the guitar. piezasguitarra[DoM] miguitarra[DoM]
    var oldValue = $(this).data('val');
    var newValue= val;
    var precioViejo;
    var precioNuevo;
    var tipo;
    var texturePath;


    $('#precio').before('<div id="loaderPrecio" class="loaderPrecio"></div>');
    $('#precio').hide()
    $.when(ajax1(DoM),ajax2(DoM),ajax3(DoM)).done(function (a1,a2,a3) {
        $('#precio').show()
        $('#loaderPrecio').remove()
        actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
        if (DoM==3){
            texturePath= 'static/modelos/'+tipo[0].modelo+'/texturas/diapason-'+newValue+'.jpg';
        }else if (DoM==2){
            texturePath= 'static/modelos/'+tipo[0].modelo+'/texturas/mastil-'+newValue+'.jpg';
        }
        //Cambiar textura
        var material2 = new THREE.MeshPhongMaterial({ transparent: false,
            map: THREE.ImageUtils.loadTexture(texturePath),
            shininess: 20,//con esto parece que refleja, pero como que ciega un poco
            specular: 0x444444,//con esto parece que refleja
            name: texturePath.split('/texturas/')[1].split('-')[1].split('.')[0],
            color: 0xbbbbbb,
        });
        miguitarra[DoM].material=material2;
    });
    function ajax1(DoM) {
        return $.ajax({
                url: urlBase + "precio3D/" + piezasguitarra[DoM] + "/" + oldValue,
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
    function ajax2() {
        return $.ajax({
            url: urlBase + "precio3D/" + piezasguitarra[DoM] + "/" + newValue,
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
    function ajax3() {
        //This ajax request is to get the type of guitar of the item (stratocaster, telecaster....)
        //With that we add to the path for the texture change
        return $.ajax({
            url: urlBase + "parte3D/" + piezasguitarra[DoM],
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                tipo = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
function cambioPastilla(val,past){
    var oldValue = $(this).data('val');
    var newValue= val;
    var precioViejo;
    var precioNuevo;
    $('#precio').before('<div id="loaderPrecio" class="loaderPrecio"></div>');
    $('#precio').hide()
    $.when(ajax1(),ajax2()).done(function (a1,a2) {
        $('#precio').show()
        $('#loaderPrecio').remove()
        actualizarPrecio(precioViejo[0].precio,precioNuevo[0].precio);
    });
    function ajax1() {
        return $.ajax({
                url: urlBase + "precio3D/" + piezasguitarra[past] + "/" + oldValue,
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
    function ajax2() {
        return $.ajax({
            url: urlBase + "precio3D/" + piezasguitarra[past] + "/" + newValue,
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
}
function actualizarModalPastillas(past,modelo) {
    var modalname='#pastillas';
    var modalname2='#modalPastilla'
    var pastModelo;
    var pastilla='Pastilla';
    if (past==4){
        modalname=modalname.concat('Mastil');
        modalname2=modalname2.concat('Mastil0');
        pastilla=pastilla.concat('Mastil');
    }else if (past==5){
        modalname=modalname.concat('Medio');
        modalname2=modalname2.concat('Medio0');
        pastilla=pastilla.concat('Medio');
    }else if(past==6){
        modalname=modalname.concat('Puente');
        modalname2=modalname2.concat('Puente0');
        pastilla=pastilla.concat('Puente');
    }
    $(modalname).before('<div id="loaderPastillas" class="loader"></div>');
    $(modalname).hide();
    //Peticion ajax
    $.when(ajax1()).done(function (a1) {
        $(modalname).show();
        $('#loaderPastillas').remove();
        var html='';
        for (var i=0;i<pastModelo.length;i++) {
            var myPosicion="{'x':"+pastModelo[i].x+",'y':"+pastModelo[i].y+",'z':"+pastModelo[i].z+"}";
            html=html.concat('<a onclick="cambiarParte(event, partes3D,'+past+',');
            html=html.concat(""+pastModelo[i].id+",");
            html=html.concat(myPosicion);
            html=html.concat(',\''+modalname2+'\',');
            html=html.concat("miguitarra)");
            html=html.concat('"><img class=\'myimage\' src=static/img/'+pastModelo[i].foto+' ' );
            html=html.concat('width=\'200\' height=\'115\'>' );
            html=html.concat('</a>');
        }
        $(modalname).html(html);
    });
    function ajax1(){
        return $.ajax({
            url: urlBase+"pastModelo/"+modelo+'/'+pastilla,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                pastModelo = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
function actualizarComponentes(modelo) {
    var modalname='#componentesBody';
    var componentes;
    var parte;
    $(modalname).before('<div id="loaderComponentes" class="loader"></div>');
    $(modalname).hide();
    //Peticion ajax
    $.when(ajax1()).done(function (a1) {
        $(modalname).show();
        $('#loaderComponentes').remove();
        var html='';
        for (var i=0;i<componentes.length;i++) {
            var myPosicion="{'x':"+componentes[i].x+",'y':"+componentes[i].y+",'z':"+componentes[i].z+"}";
            parte=pieza2parte(componentes[i].pieza)
            html=html.concat('<a onclick="cambiarParte(event, partes3D,'+(parte-1) +',');
            html=html.concat(""+componentes[i].id+",");
            html=html.concat(myPosicion);
            html=html.concat(',\'#modal'+componentes[i].pieza+'0\',');
            html=html.concat("miguitarra)");
            html=html.concat('"><img class=\'myimage\' src=static/img/'+componentes[i].foto+' ' );
            html=html.concat(' data-dismiss=\'modal\'width=\'200\' height=\'115\'>' );
            html=html.concat('</a>');
        }
        $(modalname).html(html);
    });
    function ajax1(){
        return $.ajax({
            url: urlBase+"componentesModelo/"+modelo,
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                componentes = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }
}
function pieza2parte(pieza){
    var parte;
    if(pieza=='Cuerpo'){
        parte=1;
    }else if(pieza=='Golpeador'){
        parte=2;
    }else if(pieza=='Mastil'){
        parte=3;
    }else if(pieza=='Diapason'){
        parte=4;
    }else if(pieza=='PastillaMastil'){
        parte=5;
    }else if(pieza=='PastillaMedio'){
        parte=6;
    }else if(pieza=='PastillaPuente'){
        parte=7;
    }else if(pieza=='Puente'){
        parte=8;
    }else if(pieza=='Tono1'){
        parte=9;
    }else if(pieza=='Tono2'){
        parte=10;
    }else if(pieza=='Volumen'){
        parte=11;
    }else if(pieza=='Tapa'){
        parte=12;
    }else if(pieza=='Chapa'){
        parte=13;
    }else if(pieza=='Jack'){
        parte=14;
    }else if(pieza=='Clavijero'){
        parte=15;
    }else if(pieza=='Cejuela'){
        parte=16;
    }else if(pieza=='Switch'){
        parte=17;
    }else{
        parte=99;
    }
    return parte;
}
function cargarForm() {
    var modelo;
    $.when(ajax1()).done(function (a1) {
        modelo=tipo[0].modelo;
        $('<input>').attr({
            type: 'hidden',
            name: 'modelo',
            value: modelo,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'maderaCuerpo',
            value: $('#dropCuerpo').val(),
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'maderaDiapason',
            value: $('#dropDiapason').val(),
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'maderaMastil',
            value: $('#dropMastil').val(),
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'mastil',
            value: miguitarra[2].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'pastillaMastil',
            value: miguitarra[4].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'pastillaMedio',
            value: miguitarra[5].name,
        }).appendTo('form');

        /*$('<input>').attr({
            type: 'hidden',
            name: 'pastillaPuente',
            value: miguitarra[6].name,
        }).appendTo('form');*/ //PastillaPuente

        /*$('<input>').attr({
            type: 'hidden',
            name: 'puente',
            value: miguitarra[7].name,
        }).appendTo('form');*/ //Puente

        $('<input>').attr({
            type: 'hidden',
            name: 'tono1',
            value: miguitarra[8].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'tono2',
            value: miguitarra[9].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'volumen',
            value: miguitarra[10].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'tapa',
            value: miguitarra[11].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'chapa',
            value: miguitarra[12].name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'jack',
            value: miguitarra[13].name,
        }).appendTo('form');

        /*$('<input>').attr({
            type: 'hidden',
            name: 'clavijero',
            value: miguitarra[14].name,
        }).appendTo('form');*/ //Clavijero

        $('<input>').attr({
            type: 'hidden',
            name: 'acabado',
            value: miacabado,
        }).appendTo('form');

        //COLORES
        $('<input>').attr({
            type: 'hidden',
            name: 'colorCuerpo',
            value: miguitarra[0].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorGolpeador',
            value: miguitarra[1].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorPastillaMastil',
            value: miguitarra[4].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorPastillaMedio',
            value: miguitarra[5].material.name,
        }).appendTo('form');

        /*$('<input>').attr({
            type: 'hidden',
            name: 'colorPastillaPuente',
            value: miguitarra[6].material.name,
        }).appendTo('form');*/ //ColorPastillaPuente

        /*$('<input>').attr({
            type: 'hidden',
            name: 'colorPuente',
            value: miguitarra[7].material.name,
        }).appendTo('form');*/ //ColorPuente

        $('<input>').attr({
            type: 'hidden',
            name: 'colorTono1',
            value: miguitarra[8].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorTono2',
            value: miguitarra[9].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorVolumen',
            value: miguitarra[10].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorTapa',
            value: miguitarra[11].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorChapa',
            value: miguitarra[12].material.name,
        }).appendTo('form');

        $('<input>').attr({
            type: 'hidden',
            name: 'colorJack',
            value: miguitarra[13].material.name,
        }).appendTo('form');

    });
    function ajax1() {
        //This ajax request is to get the type of guitar of the item (stratocaster, telecaster....)
        //With that we add to the path for the texture change
        return $.ajax({
            url: urlBase + "parte3D/" + piezasguitarra[0],
            dataType: "json",    // Work with the response
            crossdomain: true,
            success: function (response) {
                tipo = response;
            },
            error: function (response) {
                console.log('ERROR');
            }
        });
    }


}
