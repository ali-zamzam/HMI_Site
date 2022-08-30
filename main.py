from flask import Flask,render_template,request,redirect,url_for,session,g,flash
from random import choice, randint
from service.Module_profile import user

import service.prediction as predict

user_profile = user()

alphabet_min = [ chr(i) for i in range(97,123) ]
alphabet_maj = [ chr(i) for i in range(65,91) ]
chiffres = [ chr(i) for i in range(48,58) ]
caracteres_speciaux = [ '%','_','-','!','$','&']


def pwd(n, min=True, maj=True, chif=True, cs=True):
    alphabets = dict()
    key = 0
    if min:
        alphabets[key] = alphabet_min
        key += 1
    if maj:
        alphabets[key] = alphabet_maj
        key += 1
    if chif:
        alphabets[key] = chiffres
        key += 1
    if cs:
        alphabets[key] = caracteres_speciaux
        key += 1
    mdp = ''
    for i in range(n):
        s = randint(0, key - 1)
        mdp += choice(alphabets[s])

    return mdp


app = Flask(__name__)
app.secret_key=b'T\xa21\x8f\x9e{\x91\xaa\x05\x83v7 \x94,\xb6'

dic={}


@app.route('/')
def index():
    return render_template('log_in.html')

@app.route('/log_in',methods=['POST'])
def set_saisie():
    if request.method == 'POST':
        pseudo = request.form["pseudo"]
        password = request.form["password"]
        print(pseudo,password)
        val = user_profile.uservalidation(pseudo,password)
        if val[0]:
            return render_template("index.html", profile=val[1])
        else:
            flash('Votre pseudo est incorrect ou inexistant')
            return redirect(url_for('index'))
    return render_template('log_in.html')



@app.route('/index/<key>/')
def home(key):
    return render_template('index.html',profile=key)

@app.route('/visualisation/<key>/')
def predictions(key):
    return render_template('visualisation.html',profile=key)

@app.route('/Mention_legale')
def Mention_legale():
        return render_template('Mention_legale.html',profile="00")

@app.route('/Mention_legales/<key>/')
def Mention_legales(key):
    return render_template('Mention_legales.html', profile=key)

@app.route('/prediction/<key>/')
def modele_predictive(key):
    return render_template('prediction.html', profile=key)

@app.route('/parametre/<key>/')
def parametre(key):
    return render_template('parametre.html', profile=key)

@app.route('/parametresave/<key>',methods=['POST'])
def parametresave(key):
    if request.method == 'POST':
        liste = {}
        liste["key"]= str(request.form["keykey"])
        liste["pseudo"] = str(request.form["pseudo"])
        liste["password"] = str(request.form["password"])
        ret = user_profile.savejson(liste)
        return render_template("parametresave.html",profile=key,retour=ret)

@app.route('/results/<key>',methods=['POST'])
def results(key):
    if request.method == 'POST':
        s = float(request.form["surface"])
        nh = float(request.form["habitants"])
        nc = float(request.form["commerce"])
        nb = float(request.form["arrets"])
        nv = float(request.form["voyageurs"])

        estimation,interet = predict.prediction(s,nh,nc,nb,nv)
        return render_template("visualisation.html",profile=key,estimation=estimation,interet=interet)

@app.route('/log_out')
def log_out():
    return render_template('log_in.html')


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('index.html'), 404


# https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)


