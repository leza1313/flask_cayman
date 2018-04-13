from flask import Blueprint,render_template, request, redirect, url_for, flash
from flask_login import login_required
from models.pedidos import PedidosModel


pedidos = Blueprint('pedidos', __name__)

@pedidos.route('/pedidos')
@login_required
def html():
    mypedidos = PedidosModel.query.all()
    return render_template('pedidos.html', mytitle='Pedidos', mypedidos=mypedidos)

@pedidos.route('/borrarpedidosfoto/<string:id>')
@login_required
def borrar(id):

    flash('Error: No se ha conseguido eliminar el pedido')
    return redirect(url_for('html'))

@pedidos.route('/nuevapedidosfoto', methods=['POST'])
@login_required
def nuevo():
    flash('Exito: Se ha anadido correctamente el pedido')
    return redirect(url_for('html'))
