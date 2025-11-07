# app.py

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'votre_cle_secrete_tres_simple' 

# L'IMPORTATION doit être sur sa propre ligne
from routes import *
if __name__ == '__main__':
 
    app.run(debug=True)