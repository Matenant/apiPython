# import the Flask class from the flask module
from flask import Flask, render_template

# create the application object
app = Flask(__name__)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "API pour les cours de l'IUT"  # return a string

@app.get('/infoSvg', methods=['GET'])
def infoSvg():
    infoSvg = flask.jsonify([
        { "id": 1, "chemin": "svg/inspection.svg", "nom": "Inspection", "largeur": 66.86, "hauteur": 69.7, "echelle": 1.7, "origineX": 14.2, "origineY": 69.7 },
        { "id": 2, "chemin": "svg/cn.svg", "nom": "Cn", "largeur": 63.14, "hauteur": 82.689, "echelle": 1.2, "origineX": 17.79, "origineY": 82.689 },
        { "id": 3, "chemin": "svg/perceuse.svg", "nom": "Perceuse", "largeur": 40.58, "hauteur": 79.18, "echelle": 1.6, "origineX": 13.99, "origineY": 79.18 },
        { "id": 4, "chemin": "svg/tour.svg", "nom": "Tour", "largeur": 89.02, "hauteur": 94.63, "echelle": 1.2, "origineX": 17.78, "origineY": 94.63 },
        { "id": 5, "chemin": "svg/foreuse.svg", "nom": "Foreuse", "largeur": 63.25, "hauteur": 97.19, "echelle": 1.35, "origineX": 14.25, "origineY": 97.19 },
        { "id": 6, "chemin": "svg/robot.svg", "nom": "Robot", "largeur": 78.78, "hauteur": 85.51, "echelle": 1.6, "origineX": 29.76, "origineY": 85.51 },
        { "id": 7, "chemin": "svg/fraiseuse.svg", "nom": "Fraiseuse", "largeur": 80.13, "hauteur": 98.88, "echelle": 1.33, "origineX": 15.44, "origineY": 98.88 }
    ])
    infoSvg.headers.add('Access-Control-Allow-ORigin', '*')
    return infoSvg, 200  # render a template

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)