import logging
from logging.handlers import RotatingFileHandler
from flask import current_app as app

formatter = logging.Formatter(
        "[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - \n%(message)s\n-------------------------\n")
handler = RotatingFileHandler('/var/prueba/foo.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)
app.logger.addHandler(handler)
mylogger = app.logger