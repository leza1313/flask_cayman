from flask import Blueprint, request, current_app
from werkzeug.datastructures import ImmutableOrderedMultiDict
from models.pedidos import PedidosModel

'''This module processes PayPal Instant Payment Notification messages (IPNs).'''
from flask import current_app as app
import requests

paypal_ipn = Blueprint('paypal_ipn', __name__)

@paypal_ipn.route("/paypal_ipn", methods=['POST'])
def paypal_ipn2():
    arg = ''
    request.parameter_storage_class = ImmutableOrderedMultiDict
    values = request.form

    app.logger.warning("{}".format(request.form))
    for x, y in values.items():
        arg += "&{x}={y}".format(x=x, y=y)
    validate_url = 'https://www.sandbox.paypal.com' \
                   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
        .format(arg=arg)
    r = requests.get(validate_url)

    if r.text == 'VERIFIED':
        app.logger.warning("VERIFIED")
        #TODO
        numero_serie = 112233
        modelo = "mississpi"
        acabado="acabado1"
        pastillas="pastillas1"
        puente="puente1"
        electronica="electronica1"
        clavijero="clavijero1"

        nombre= (values['first_name']+values['last_name'])
        direccion= (values['address_street']+values['address_city']+values['address_state']+values['address_country'])
        #TODO
        telefono=666777888
        email=values['payer_email']

        precio=values['mc_gross']
        fecha=values['payment_date']

        #TODO
        observaciones="Campo para rellenar con observaciones"

        mypedido = PedidosModel(numero_serie,modelo,acabado,pastillas,puente,electronica,clavijero,
                                nombre,direccion,telefono,email,
                                precio,fecha,observaciones)
        mypedido.insert_to_db()

    else:
        app.logger.warning("INVALID")
    return r.text
