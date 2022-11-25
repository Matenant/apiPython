# import the Flask class from the flask module
from flask import Flask, jsonify, request
from pathlib import Path
import base64
from flask_cors import CORS



# create the application object
app = Flask(__name__)
CORS(app)

# use decorators to link the function to a url
@app.route('/')
def home():
    return "API pour les cours de l'IUT"  # return a string

@app.route('/pays')
def pays():
    pays = jsonify([
        { "name": "Nigel Hooper", "birth": "1977-03-23", "country": "Belgium", "nb_child": 1 },
        { "name": "Jessamine Franks", "birth": "1986-11-06", "country": "France", "nb_child": 2 },
        { "name": "Lamar Turner", "birth": "1975-06-03", "country": "Belgium", "nb_child": 3 },
        { "name": "Kieran Palmer", "birth": "1978-10-08", "country": "United Kingdom", "nb_child": 0 },
        { "name": "Irma Glass", "birth": "1980-10-17", "country": "Germany", "nb_child": 2 },
        { "name": "Louis Walsh", "birth": "1984-06-02", "country": "United Kingdom", "nb_child": 3 },
        { "name": "Merritt Witt", "birth": "1998-10-30", "country": "France", "nb_child": 0 },
        { "name": "Carissa Bryan", "birth": "1990-08-14", "country": "United Kingdom", "nb_child": 4 },
        { "name": "Lila Battle", "birth": "1985-01-29", "country": "United Kingdom", "nb_child": 0 },
        { "name": "Abdul Booker", "birth": "1982-04-13", "country": "Belgium", "nb_child": 0 },
        { "name": "Axel Santos", "birth": "1973-12-06", "country": "Germany", "nb_child": 4 },
        { "name": "Chandler Allison", "birth": "1974-05-20", "country": "United Kingdom", "nb_child": 0 },
        { "name": "April Mcneil", "birth": "1970-10-14", "country": "Spain", "nb_child": 0 },
        { "name": "Sybill Oneil", "birth": "1975-04-11", "country": "Belgium", "nb_child": 1 },
        { "name": "Gray Hickman", "birth": "1977-01-10", "country": "France", "nb_child": 0 },
        { "name": "Beau Bond", "birth": "1976-12-28", "country": "Belgium", "nb_child": 4 },
        { "name": "Wade Barker", "birth": "1980-09-26", "country": "Belgium", "nb_child": 2 },
        { "name": "Harlan Lowe", "birth": "1982-02-25", "country": "Spain", "nb_child": 2 },
        { "name": "Chantale Stokes", "birth": "1983-10-18", "country": "Spain", "nb_child": 0 },
        { "name": "Mallory Stuart", "birth": "1994-05-04", "country": "Belgium", "nb_child": 2 },
        { "name": "William Bartlett", "birth": "1999-03-31", "country": "Belgium", "nb_child": 2 },
        { "name": "Oleg Burnett", "birth": "1972-11-21", "country": "Belgium", "nb_child": 1 },
        { "name": "Alyssa Tucker", "birth": "2000-09-23", "country": "United Kingdom", "nb_child": 1 },
        { "name": "Berk Benson", "birth": "1985-03-01", "country": "Belgium", "nb_child": 1 },
        { "name": "Jerry Blankenship", "birth": "1985-07-11", "country": "France", "nb_child": 0 },
        { "name": "Jakeem Todd", "birth": "1985-08-16", "country": "United Kingdom", "nb_child": 2 },
        { "name": "Patricia Branch", "birth": "1991-04-20", "country": "United Kingdom", "nb_child": 1 },
        { "name": "Debra Mendez", "birth": "1992-02-12", "country": "Italy", "nb_child": 0 },
        { "name": "Pascale Shannon", "birth": "1998-08-14", "country": "Germany", "nb_child": 3 },
        { "name": "Shad Wells", "birth": "1992-11-30", "country": "Spain", "nb_child": 3 },
        { "name": "Rose Payne", "birth": "1994-05-10", "country": "United Kingdom", "nb_child": 2 },
        { "name": "Rashad Clements", "birth": "1973-08-10", "country": "Germany", "nb_child": 2 },
        { "name": "Heather Schultz", "birth": "1976-04-19", "country": "France", "nb_child": 3 },
        { "name": "Caryn Morgan", "birth": "1977-03-13", "country": "France", "nb_child": 0 },
        { "name": "Ivana Guthrie", "birth": "1979-12-09", "country": "Germany", "nb_child": 4 },
        { "name": "Dora Rogers", "birth": "1981-01-17", "country": "France", "nb_child": 3 },
        { "name": "Yael Schultz", "birth": "1982-02-20", "country": "Belgium", "nb_child": 1 },
        { "name": "Joel Douglas", "birth": "1985-05-14", "country": "Spain1", "nb_child": 4 },
        { "name": "Leroy Bright", "birth": "1983-03-18", "country": "Spain1", "nb_child": 4 },
        { "name": "Kylan Marks", "birth": "1984-04-02", "country": "United Kingdom", "nb_child": 3 },
        { "name": "Dakota Howe", "birth": "1986-06-22", "country": "United Kingdom", "nb_child": 4 },
        { "name": "Jeremy Cunningham", "birth": "1987-02-09", "country": "France", "nb_child": 0 },
        { "name": "Tanisha Mcgowan", "birth": "1988-12-20", "country": "Italy", "nb_child": 0 },
        { "name": "Tallulah Fowler", "birth": "1989-03-01", "country": "Italy", "nb_child": 0 },
        { "name": "Honorato Lowe", "birth": "1990-09-05", "country": "France", "nb_child": 0 },
        { "name": "Neil Leblanc", "birth": "1998-12-23", "country": "Belgium", "nb_child": 1 },
        { "name": "Roary Stephenson", "birth": "1996-05-11", "country": "Italy", "nb_child": 3 },
        { "name": "August Compton", "birth": "1977-12-11", "country": "United Kingdom", "nb_child": 2 },
        { "name": "Gretchen Kelly", "birth": "1978-09-02", "country": "Germany", "nb_child": 0 },
        { "name": "Thor Frederick", "birth": "1975-11-23", "country": "France", "nb_child": 3 },
        { "name": "Stacy Joseph", "birth": "1980-11-03", "country": "United Kingdom", "nb_child": 4 },
        { "name": "Idona Yates", "birth": "2000-03-02", "country": "Belgium", "nb_child": 1 },
        { "name": "Melyssa Tate", "birth": "1976-01-13", "country": "France", "nb_child": 3 },
        { "name": "Caldwell Frye", "birth": "1982-08-25", "country": "Germany", "nb_child": 1 },
        { "name": "Carlos Mcclain", "birth": "1989-04-06", "country": "Spain1", "nb_child": 4 },
        { "name": "Jorden Ayala", "birth": "1986-08-04", "country": "Italy", "nb_child": 0 },
        { "name": "Shea Welch", "birth": "1978-12-01", "country": "Spain1", "nb_child": 2 },
        { "name": "Lee Landry", "birth": "1997-06-30", "country": "Germany", "nb_child": 3 },
        { "name": "Fredericka Tillman", "birth": "1995-03-19", "country": "Belgium", "nb_child": 4 },
        { "name": "Griffith Mcknight", "birth": "1994-09-12", "country": "France", "nb_child": 1 },
        { "name": "Vera Todd", "birth": "1995-11-03", "country": "Belgium", "nb_child": 1 },
        { "name": "Tate Estes", "birth": "1998-09-25", "country": "Germany", "nb_child": 4 },
        { "name": "Eve Albert", "birth": "1978-01-13", "country": "Spain1", "nb_child": 2 },
        { "name": "Plato Mcdonald", "birth": "1990-11-01", "country": "France", "nb_child": 2 },
        { "name": "Linus Camacho", "birth": "1973-01-05", "country": "United Kingdom", "nb_child": 3 },
        { "name": "Justine Mcintyre", "birth": "1973-07-23", "country": "Italy", "nb_child": 3 },
        { "name": "Bianca Joseph", "birth": "1979-01-29", "country": "France", "nb_child": 0 },
        { "name": "Colton Boone", "birth": "1985-09-28", "country": "Germany", "nb_child": 0 },
        { "name": "Charity Stokes", "birth": "1988-03-26", "country": "Spain1", "nb_child": 3 },
        { "name": "Teagan Jimenez", "birth": "1991-02-08", "country": "Spain1", "nb_child": 2 },
        { "name": "Hilary Lyons", "birth": "1991-02-24", "country": "France", "nb_child": 0 },
        { "name": "Candace Mcfadden", "birth": "1993-05-02", "country": "Spain1", "nb_child": 4 },
        { "name": "Oleg Osborn", "birth": "1993-05-23", "country": "France", "nb_child": 2 },
        { "name": "Jeanette Nichols", "birth": "1993-09-13", "country": "United Kingdom", "nb_child": 0 },
        { "name": "Brianna Huff", "birth": "1993-12-31", "country": "Spain1", "nb_child": 4 },
        { "name": "Riley Gates", "birth": "1994-11-23", "country": "Belgium", "nb_child": 4 },
        { "name": "Louis Pennington", "birth": "1996-10-05", "country": "Germany", "nb_child": 0 },
        { "name": "Dean Alexander", "birth": "1975-02-16", "country": "Spain1", "nb_child": 2 },
        { "name": "Lavinia Mclaughlin", "birth": "1977-08-27", "country": "United Kingdom", "nb_child": 4 },
        { "name": "Veronica Patterson", "birth": "1974-05-19", "country": "Italy", "nb_child": 3 },
        { "name": "Emily Wagner", "birth": "1998-12-18", "country": "Belgium", "nb_child": 4 },
        { "name": "Nina Haley", "birth": "1971-06-14", "country": "Belgium", "nb_child": 3 },
        { "name": "Nina Rodriguez", "birth": "1976-10-22", "country": "Belgium", "nb_child": 0 },
        { "name": "Abel Pacheco", "birth": "1972-09-09", "country": "Belgium", "nb_child": 1 },
        { "name": "Catherine Butler", "birth": "1997-08-29", "country": "France", "nb_child": 3 },
        { "name": "Cody Freeman", "birth": "1996-02-26", "country": "Spain1", "nb_child": 2 },
        { "name": "Azalia Riggs", "birth": "1975-07-04", "country": "Germany", "nb_child": 4 },
        { "name": "Gloria Crawford", "birth": "1980-06-21", "country": "Germany", "nb_child": 1 },
        { "name": "Macey Santos", "birth": "1982-03-27", "country": "Belgium", "nb_child": 1 },
        { "name": "Shaeleigh Gamble", "birth": "1992-08-10", "country": "Germany", "nb_child": 2 },
        { "name": "Ryan Kelley", "birth": "1997-07-23", "country": "Belgium", "nb_child": 3 },
        { "name": "Alisa Solomon", "birth": "1999-06-16", "country": "France", "nb_child": 0 },
        { "name": "Bethany Phillips", "birth": "2000-03-31", "country": "Italy", "nb_child": 0 },
        { "name": "Kadeem Mcfadden", "birth": "1986-09-28", "country": "Italy", "nb_child": 0 },
        { "name": "Jessica Sweet", "birth": "1993-05-20", "country": "Belgium", "nb_child": 1 },
        { "name": "Evan Mcmahon", "birth": "1983-01-08", "country": "Germany", "nb_child": 3 },
        { "name": "Ima Walsh", "birth": "1984-08-28", "country": "France", "nb_child": 3 },
        { "name": "Hyacinth Howe", "birth": "1985-08-04", "country": "Belgium", "nb_child": 3 },
        { "name": "Ezekiel Garrison", "birth": "1993-10-02", "country": "Germany", "nb_child": 1 },
        { "name": "Hermione Mcfarland", "birth": "1989-10-25", "country": "Spain1", "nb_child": 4 }
    ])
    pays.headers.add('Access-Control-Allow-Origin', '*')
    return pays, 200


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