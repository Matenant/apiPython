# import the Flask class from the flask module
from flask import Flask, jsonify, request
from pathlib import Path
import base64
from flask_cors import CORS
import sqlite3
from datetime import date
import model as user

# create the application object
app = Flask(__name__)
CORS(app)


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn
def get_auth_connection():
    conn = sqlite3.connect('flask_jwt_auth.db')
    conn.row_factory = sqlite3.Row
    return conn

# use decorators to link the function to a url
@app.get('/')
def home():
    return "API pour les cours de l'IUT"  # return a string

@app.get('/pays')
def pays():
    json = request.get_json()
    
    tok = user.login_token(json)
    if (tok != True):
        return tok

    conn = get_db_connection()
    persons = conn.execute('SELECT * FROM persons').fetchall()
    conn.close()

    data = []
    for person in persons:
        element = list(person)
        data.append({ "id": element[0], "created": element[1], "name": element[2], "birth": element[3], "country": element[4], "nb_child": element[5] })
    pays = jsonify(data)
    pays.headers.add('Access-Control-Allow-Origin', '*')
    return pays, 200

@app.post('/addPays')
def addPays():

    data = {
        "message": [],
        "success": True
    }
    message = []
    json = dict()
    json = request.get_json()

    tok = user.login_token(json)
    if (tok != True):
        return tok
    
    if (not ('birth' in json) or not checkDate(json['birth'])):
        message.append("L'attribut 'birth' est indéfini où mal défini")
        data['success'] = False
    if (not ('name' in json) or json['name'] == "" or type(json['name']) is not str):
        message.append("L'attribut 'name' est indéfini où mal défini")
        data['success'] = False
    if (not ('country' in json) or json['country'] == "" or type(json['country']) is not str):
        message.append("L'attribut 'country' est indéfini où mal défini")
        data['success'] = False
    if (not ('nb_child' in json) or type(json['nb_child']) is not int):
        message.append("L'attribut 'nb_child' est indéfini où mal défini")
        data['success'] = False

    if (not data['success']):
        data['message'] = message
        result = jsonify(data)
        result.headers.add('Access-Control-Allow-Origin', '*')
        return result, 400

    conn = get_db_connection()
    conn.execute("INSERT INTO persons (name, birth, country, nb_child) VALUES (?, ?, ?, ?)",
                    (json["name"], json["birth"], json["country"], json["nb_child"])
                )
    conn.commit()
    conn.close()

    message.append("Information enregistrée")
    data["message"] = message
    result = jsonify(data)
    result.headers.add('Access-Control-Allow-Origin', '*')
    return result, 200

@app.post('/france')
def france():

    json = request.get_json()

    tok = user.login_token(json)
    if (tok != True):
        return tok

    conn = get_db_connection()
    regions = conn.execute('SELECT * FROM regions').fetchall()
    conn.close()

    data = []
    for region in regions:
        element = list(region)
        data.append({ "id": element[0], "created": element[1], "name": element[2], "code": element[3], "taux": element[4] })
    france = jsonify(data)
    france.headers.add('Access-Control-Allow-Origin', '*')
    return france, 200

@app.get('/infoSvg')
def infoSvg():

    json = request.get_json()

    tok = user.login_token(json)
    if (tok != True):
        return tok

    conn = get_db_connection()
    svgs = conn.execute('SELECT * FROM svgs').fetchall()
    conn.close()

    data = []
    for svg in svgs:
        element = list(svg)
        data.append({ "id": element[0], "created": element[1], "name": element[2], "nom": element[3], "largeur": element[4], "hauteur": element[5], "echelle": element[6], "origineX": element[7], "origineY": element[8] })
    infoSvg = jsonify(data)
    infoSvg.headers.add('Access-Control-Allow-Origin', '*')
    return infoSvg, 200  # render a template

@app.post('/file')
def getCN():
    json = request.get_json()

    tok = user.login_token(json)
    if (tok != True):
        return tok

    path = 'files/' + json["fileName"]

    obj = Path(path)

    if obj.exists():
        file = open(path, 'rb')

        encoded_string = base64.b64encode(file.read())
        svg = jsonify({
            "success": True,
            "fileName": json["fileName"],
            "file": encoded_string.decode("utf-8")
        })
        code = 200
    else:
        svg = jsonify({
            "success": False,
            "message": "Erreur lors de la récupération du fichier"
        })
        code = 404 
    svg.headers.add('Access-Control-Allow-Origin', '*')
    return svg, code

@app.post('/login')
def login():
    json = request.get_json()

    if (not 'name' in json or not 'password' in json):
        result = jsonify({'messages': ["Nom ou/et mot de passe incorrect"]})
        result.headers.add('Access-Control-Allow-Origin', '*')
        return result, 400
    
    conn = get_auth_connection()
    person = conn.execute('SELECT * FROM users WHERE name == "'+json['name']+ '" AND password == "'+json['password']+'"').fetchall()
    conn.close()

    result = jsonify({"token": user.encode_auth_token(list(person[0])[5])})
    result.headers.add('Access-Control-Allow-Origin', '*')
    return result, 200

def checkDate(strDate):
    try:
        date.fromisoformat(strDate)
        return True
    except ValueError:
        return False

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)