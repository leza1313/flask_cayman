from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.pedidos import PedidosModel


pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos')
@login_required
def html():
    mypedidos = PedidosModel.query.order_by(PedidosModel.fecha.desc()).all()
    return render_template('pedidos.html', mytitle='Pedidos', mypedidos=mypedidos)

@pedidos.route('/borrarpedidos/<string:id>')
@login_required
def borrar(id):
    mypedido = PedidosModel.find_by_id(id)
    if mypedido:
        mypedido.delete_from_db()
        flash('Exito: Se ha eliminado correctamente el pedido')
        return redirect(url_for('pedidos.html'))
    flash('Error: No se ha conseguido eliminar el pedido')
    return redirect(url_for('pedidos.html'))

@pedidos.route('/nuevopedido', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        if request.form['factura']=='':
            factura = None
        else:
            factura = request.form['factura']
        numero_serie = request.form['numero_serie']
        modelo = request.form['modelo']
        acabado = request.form['acabado']
        pastillas = request.form['pastillas']
        puente = request.form['puente']
        electronica = request.form['electronica']
        clavijero = request.form['clavijero']
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        telefono = request.form['telefono']
        email = request.form['email']
        precio = request.form['precio']
        fecha = request.form['fecha']
        observaciones = request.form['obser']
        mypedido = PedidosModel(None,factura,numero_serie,modelo,acabado,pastillas,puente,electronica,clavijero,nombre,direccion,telefono,email,precio,fecha,observaciones)
        mypedido.insert_to_db()
        flash('Exito: Se ha anadido correctamente el pedido')
        return redirect(url_for('pedidos.html'))
    mypedido= PedidosModel.find_last()
    return render_template('nuevopedido.html',mytitle='Nuevo pedido',lastSerial=mypedido.numero_serie)

@pedidos.route('/editarpedido/<string:id>', methods=['POST'])
@login_required
def editar(id):
    pedido = PedidosModel.find_by_id(id)
    if pedido:
        pedido.factura = request.form['factura']
        pedido.numero_serie = request.form['numero_serie']
        pedido.modelo = request.form['modelo']
        pedido.acabado = request.form['acabado']
        pedido.pastillas = request.form['pastillas']
        pedido.puente = request.form['puente']
        pedido.electronica = request.form['electronica']
        pedido.clavijero = request.form['clavijero']
        pedido.nombre = request.form['nombre']
        pedido.direccion = request.form['direccion']
        pedido.telefono = request.form['telefono']
        pedido.email = request.form['email']
        pedido.precio = request.form['precio']
        pedido.fecha = request.form['fecha']
        pedido.observaciones = request.form['obser']
        pedido.fecha_salida = request.form['fecha_salida']
        pedido.actualizar()
        flash('Exito: Se ha actualizado correctamente el pedido: '+id)
        return redirect(url_for('pedidos.html'))
    flash('Error: No se ha actualizado el pedido: '+id)
    return redirect(url_for('pedidos.html'))
