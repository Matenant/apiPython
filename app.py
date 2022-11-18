# import the Flask class from the flask module
from flask import Flask, jsonify, request
from pathlib import Path
import base64

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "API pour les cours de l'IUT"  # return a string

@app.get('/infoSvg')
def infoSvg():
    infoSvg = jsonify([
        { "id": 1, "name": "inspection.svg", "nom": "Inspection", "largeur": 66.86, "hauteur": 69.7, "echelle": 1.7, "origineX": 14.2, "origineY": 69.7 },
        { "id": 2, "name": "cn.svg", "nom": "Cn", "largeur": 63.14, "hauteur": 82.689, "echelle": 1.2, "origineX": 17.79, "origineY": 82.689 },
        { "id": 3, "name": "perceuse.svg", "nom": "Perceuse", "largeur": 40.58, "hauteur": 79.18, "echelle": 1.6, "origineX": 13.99, "origineY": 79.18 },
        { "id": 4, "name": "tour.svg", "nom": "Tour", "largeur": 89.02, "hauteur": 94.63, "echelle": 1.2, "origineX": 17.78, "origineY": 94.63 },
        { "id": 5, "name": "foreuse.svg", "nom": "Foreuse", "largeur": 63.25, "hauteur": 97.19, "echelle": 1.35, "origineX": 14.25, "origineY": 97.19 },
        { "id": 6, "name": "robot.svg", "nom": "Robot", "largeur": 78.78, "hauteur": 85.51, "echelle": 1.6, "origineX": 29.76, "origineY": 85.51 },
        { "id": 7, "name": "fraiseuse.svg", "nom": "Fraiseuse", "largeur": 80.13, "hauteur": 98.88, "echelle": 1.33, "origineX": 15.44, "origineY": 98.88 }
    ])
    infoSvg.headers.add('Access-Control-Allow-Origin', '*')
    return infoSvg, 200  # render a template

@app.post('/file')
def getCN():
    json = request.get_json()
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

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)