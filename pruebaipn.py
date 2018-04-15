import urllib.parse

from flask import Blueprint, request, current_app
from werkzeug.datastructures import ImmutableOrderedMultiDict


'''This module processes PayPal Instant Payment Notification messages (IPNs).'''
from flask import current_app as app
import requests, calendar, datetime

pruebaipn = Blueprint('pruebaipn', __name__)

@pruebaipn.route("/pruebaipn", methods=['POST'])
def pruebaipn2():

    VERIFY_URL_PROD = 'https://ipnpb.paypal.com/cgi-bin/webscr'
    VERIFY_URL_TEST = 'https://ipnpb.sandbox.paypal.com/cgi-bin/webscr'

    # Switch as appropriate
    VERIFY_URL = VERIFY_URL_TEST

    # CGI preamble
    app.logger.warning('content-type: text/plain')
    app.logger.warning("{}".format(request.form))


    # Read and parse query string
    param_str = request.form
    params = urllib.parse.parse_qsl(param_str)

    # Add '_notify-validate' parameter
    params.append(('cmd', '_notify-validate'))

    # Post back to PayPal for validation

    headers = {'content-type': 'application/x-www-form-urlencoded',
               'user-agent': 'Python-IPN-Verification-Script'}
    r = requests.post(VERIFY_URL, params=params, headers=headers, verify=True)
    r.raise_for_status()

    # Check return message and take action as needed
    if r.text == 'VERIFIED':
        app.logger.warning("VERIFIED")
    elif r.text == 'INVALID':
        app.logger.warning("INVALID")