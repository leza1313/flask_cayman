from flask import Blueprint, request, current_app
from werkzeug.datastructures import ImmutableOrderedMultiDict
from models.pedidos import PedidosModel
from models.guitarras import GuitarrasModel
from models.bajos import BajosModel

'''This module processes PayPal Instant Payment Notification messages (IPNs).'''
from flask import current_app as app
import requests, calendar, datetime

paypal_ipn = Blueprint('paypal_ipn', __name__)

@paypal_ipn.route("/paypal_ipn", methods=['POST'])
def paypal_ipn2():
    arg = ''
    request.parameter_storage_class = ImmutableOrderedMultiDict
    values = request.form

    app.logger.warning("{}".format(request.form))
    for x, y in values.items():
        arg += "&{x}={y}".format(x=x.__str__(), y=y.__str__())
    validate_url = 'https://www.sandbox.paypal.com' \
                   '/cgi-bin/webscr?cmd=_notify-validate{arg}' \
        .format(arg=arg)
    r = requests.get(validate_url)

    if r.text == 'VERIFIED':
        app.logger.warning("VERIFIED")
        #Serial number generator. 0418001-> 04 (Aprl)/ 18 (Year)/ 001 (Number of guitar made that month)
        lastPedido = PedidosModel.find_last()
        if lastPedido:
            serial = lastPedido.numero_serie
            month = int(serial[0]+serial[1])
            year = int("20"+serial[2]+serial[3])
            num = int(serial[4]+serial[5]+serial[6])

            today=datetime.date.today()

            if today.year == year:
                newYear = today.year - 2000
                if today.month == month:
                    newMonth = today.month
                    newNum = num+1
                elif today.month>month:
                    newMonth = today.month
                    newNum=1
            elif today.year > year:
                newYear = today.year - 2000
                newMonth = today.month
                newNum = 1

            newMonth=newMonth.__str__()
            newYear=newYear.__str__()
            newNum=newNum.__str__()

            if len(newMonth)==1:
                newMonth = "0"+newMonth
            if len(newNum)==1:
                newNum = "00"+newNum
            elif len(newNum)==2:
                newNum = "0"+newNum
            numero_serie = newMonth+newYear+newNum
        #Couldn't find the last order, so we don't have anything to compare to
        else:
            numero_serie= "0110001"

        #se pueden pasar valores extra en el form del boton del paypal
        custom = values['custom']

        producto=custom.split('&')[0].split('=')[1]
        modelo = custom.split('&')[1].split('=')[1]

        if producto=="bajo":
            mymodelo = BajosModel.find_by_name(modelo)
        elif producto=="guitarra":
            mymodelo = GuitarrasModel.find_by_name(modelo)

        if mymodelo:
            acabado= mymodelo.acabado
            pastillas= mymodelo.pastillas
            puente= mymodelo.puente
            electronica= mymodelo.electronica
            clavijero= mymodelo.clavijero
        else:
            acabado="error, no se ha conseguido recoger los datos del modelo"
            pastillas="error"
            puente="error"
            electronica="error"
            clavijero="error"

        nombre= (values['address_name'])
        direccion= (values['address_street']+', '+values['address_city']+', '+values['address_zip']+', '
                    +values['address_state']+', '+values['address_country'])

        if 'contact_phone' in values:
            telefono=values['contact_phone']
        else:
            telefono="000000000"
        email=values['payer_email']


        precio_neto=float(values['mc_gross'])
        if 'tax' in values:
            impuesto=float(values['tax'])
        else:
            impuesto=0.00

        if 'shipping' in values:
            envio = float(values['shipping'])
        else:
            envio=0.00
        comision_paypal = float(values['mc_fee'])

        precio=(precio_neto-comision_paypal-envio-impuesto).__str__()

        fecha = datetime.datetime.now().__str__()

        #TODO maybe add a new table in the db with reparations and/or notes
        observaciones="Campo para rellenar con observaciones"

        pago_id=values['txn_id']

        if values['payer_status']=='verified':
            if 'invoice' in values:
                factura=values['invoice']
            else:
                factura="0000"
        else:
            if 'receipt_id' in values:
                factura=values['receipt_id']
            else:
                factura = "0000"

        mypedido = PedidosModel(pago_id,factura,numero_serie,modelo,acabado,pastillas,puente,electronica,clavijero,
                                nombre,direccion,telefono,email,
                                precio,fecha,observaciones)
        mypedido.insert_to_db()

    else:
        app.logger.warning("INVALID")
    return r.text
