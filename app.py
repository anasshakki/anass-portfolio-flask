# app.py

from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'votre_cle_secrete_tres_simple' 

# L'IMPORTATION doit être sur sa propre ligne
from routes import * # L'instruction 'if __name__' doit être sur une nouvelle ligne
if __name__ == '__main__':
    # Lance l'application
    app.run(debug=True)