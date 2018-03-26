from flask import Blueprint,render_template, request, redirect, url_for
from flask_login import login_required
from models.galeria import GaleriaModel


galeria = Blueprint('galeria', __name__)

@galeria.route('/galeria')
def html():
    mygaleria = GaleriaModel.query.all()
    return render_template('galeria.html', mygaleria=mygaleria, mytitle='Galeria')

@galeria.route('/borrarfoto/<string:id>')
@login_required
def borrar(id):
    url = 'https://ucarecdn.com/'+id+'/'
    mifoto = GaleriaModel.find_by_name(url)
    if mifoto:
        mifoto.delete_from_db()
    return redirect(url_for('galeria.html'))

@galeria.route('/nuevafoto', methods=['GET','POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        url = request.form['myfoto']
        alt = request.form['alt']
        #Check if url is filled or not,
        # To DO, send message to alert the admin he need to fill the image
        if url is '':
            return redirect(url_for('galeria.html'))
        mifoto = GaleriaModel.find_by_name(url)
        if mifoto is None:
            mifoto = GaleriaModel(url,alt)
            #print(mibajo)name
            mifoto.insert_to_db()

    return redirect(url_for('galeria.html'))
