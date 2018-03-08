
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

var light = new THREE.PointLight( 0xffffff, 0.85, 0 );
light.position.copy( camera.position );
light.castShadow = true;
scene.add( light );

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

//declared once at the top of your code
var axis = new THREE.Vector3(1,0,0);//tilted a bit on x and y - feel free to plug your different axis here


function rotar(miobjeto){

    for (var index in miobjeto){
        var pieza = miobjeto[index];
        pieza.borrar();
        group.add(pieza);
    }
    scene.add(group);

    rotateAll(group);
    document.getElementById( "rotar" ).setAttribute( "onClick", "parar();" );
    document.getElementById( "rotar" ).innerHTML='Parar';
}

function parar(){
    mirotation=group.rotation.y;
    console.log();
    scene.remove(group);
    for (var index in miguitarra){
        var pieza = miguitarra[index];
        scene.add(pieza);


    }
    isRotate=0;
    document.getElementById( "rotar" ).setAttribute( "onClick", "rotar(miguitarra);" );
    document.getElementById( "rotar" ).innerHTML='Rotar';
}

var SPEED = 0.01;
rad =0;

group = new THREE.Group();
//Si hago un group, cuando hago scene.add(group), pierdo la opcion de raycast a cada objeto,
//Añade un solo objeto que es el grupo
//Pero entonces puedo hacer rotar al grupo entero
//Si roto la camara es como si la guitarra me diera vueltas a la cabeza, no yo sobre la guitarra
function rotateAll(migroup) {
    rad =0.01;
    isRotate = 1;
    migroup.rotation.y -= SPEED*2;
}

//
//
//
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
//
//
//

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
function myposition(x,y,z){
    this.x=x;
    this.y=y;
    this.z=z;
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
peri = new myperillas('static/modelos/TONO_1.STL','static/modelos/TONO_2.STL','static/modelos/VOLUMEN.STL');
pasti = new mypastillas('static/modelos/PASTILLA_MASTIL.STL','static/modelos/PASTILLA_MEDIO.STL',
    'static/modelos/PASTILLA_PUENTE.STL');

guitarra = new myguitarrastl('static/modelos/CUERPO.STL','static/modelos/GOLPEADOR.STL',
    'static/modelos/MASTIL.STL',pasti.mastil,pasti.medio,pasti.puente,'static/modelos/PUENTE.STL',
    peri.tono,peri.tono2,peri.volumen);

posicionstl= new mypositionstl( //Cuerpo
                                new myposition(5,10,0),
                                //Golpeador
                                new myposition(4.95, 4.778, 3),
                                //Mastil
                                new myposition(30.8, 2.88, 2.09),
                                //Pastillas
                                new myposition(4.9,3.2, 2.65),new myposition(4.9,3.2, 2.65),new myposition(4.9,3.2, 2.65),
                                //Puente
                                new myposition(5,3.1, 0.97),
                                //Perillas
                                new myposition(4.943,-1.033, 3.067),new myposition(4.943,-1.033, 3.067),new myposition(4.943,-1.033, 3.067)
);

miguitarra=[];

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
modalName[3]='#modalPastilla_Mastil';
modalName[4]='#modalPastilla_Medio';
modalName[5]='#modalPastilla_Puente';
modalName[6]='#modalPuente';
modalName[7]='#modalTono_1';
modalName[8]='#modalTono_2';
modalName[9]='#modalVolumen';

var loader = new THREE.STLLoader();

function cargarSTL(mystl,myMaterial,sufix,position,modalName){

    loader.load( mystl, function ( geometry ) {
        var myObject = new THREE.Mesh( geometry, myMaterial);
        myObject.scale.set(0.05, 0.05, 0.05);
        scene.add(myObject);
        myObject.position.set( position.x,position.y,position.z );
        myObject.rotation.set( THREE.Math.degToRad(90),THREE.Math.degToRad(-90), THREE.Math.degToRad(0));

        myObject.callback = function(){
            $(modalName).modal();
        }
        myObject.borrar = function (){
            scene.remove(myObject);
        }
        //Si intento mostrar el objeto desde JS fuera de la funcion no funciona
        //Sin embargo, al llamar a otras funciones de JS desde HTML si que reconoce el objeto.
        miguitarra[sufix]=myObject;

    } );
}
var counter=0;
for(var index in guitarra) {
    var attr = guitarra[index];
    cargarSTL(attr,materiales[counter],counter,posicionstl[index],modalName[counter]);
    counter++;
}


function cambiarCuerpo(event,obj,nuevo,modalName){
    //hace falta poner el event.preventDefault()
    //y pasarselo a la funcion tmbn
    event.preventDefault();
    $(modalName).modal('hide');
    obj[0].borrar();
    //obj[1].borrar();
    cargarSTL(nuevo,obj[0].material,0,posicionstl.cuerpo,modalName);
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