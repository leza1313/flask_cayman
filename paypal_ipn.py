from flask import Blueprint, request, current_app
from werkzeug.datastructures import ImmutableOrderedMultiDict

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
    else:
        app.logger.warning("INVALID")
    return r.text
