import sqlite3

connection = sqlite3.connect('flask_jwt_auth.db')

with open('schema_auth.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.executemany("INSERT INTO users (name, lastname, password, idreal, status) VALUES (?, ?, ?, ?, ?)",
            [
                ('faivre', 'matheo', '1234', '22022000', 100),
                ('blaess', 'maxime', 'blaessmaxime', 32006651, 0),
                ('bonaton', 'leny', 'bonatonleny', 32217227, 0),
                ('chaboissier', 'luca', 'chaboissierluca', 32218303, 0),
                ('dematini', 'loris', 'dematiniloris', 32013264, 0),
                ('echbiki', 'hamza', 'echbikihamza', 32220314, 0),
                ('ferrauto', 'lucas', 'ferrautolucas', 32016571, 0),
                ('huck', 'sylvain', 'hucksylvain', 32205463, 0),
                ('le', 'nam-robert', 'lenam-robert', 32020920, 0),
                ('lefebvre', 'carolane', 'lefebvrecarolane', 31918146, 0),
                ('saner', 'alexandre', 'saneralexandre', 32017961, 0),
                ('schoeni', 'lucie', 'schoenilucie', 32216573, 0),
                ('urbain', 'lucas', 'urbainlucas', 32006751, 0),
                ('zettl', 'pierre', 'zettlpierre', 32005543, 0)
            ]
        )

connection.commit()
connection.close()

connection = sqlite3.connect('database.db')

with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()
cur.executemany("INSERT INTO persons (name, birth, country, nb_child) VALUES (?, ?, ?, ?)",
                [
                    ("Nigel Hooper", "1977-03-23", "Belgium", 1),
                    ("Jessamine Franks", "1986-11-06", "France", 2),
                    ("Lamar Turner", "1975-06-03", "Belgium", 3),
                    ("Kieran Palmer", "1978-10-08", "United Kingdom", 0),
                    ("Irma Glass", "1980-10-17", "Germany", 2),
                    ("Louis Walsh", "1984-06-02", "United Kingdom", 3),
                    ("Merritt Witt", "1998-10-30", "France", 0),
                    ("Carissa Bryan", "1990-08-14", "United Kingdom", 4),
                    ("Lila Battle", "1985-01-29", "United Kingdom", 0),
                    ("Abdul Booker", "1982-04-13", "Belgium", 0),
                    ("Axel Santos", "1973-12-06", "Germany", 4),
                    ("Chandler Allison", "1974-05-20", "United Kingdom", 0),
                    ("April Mcneil", "1970-10-14", "Spain", 0),
                    ("Sybill Oneil", "1975-04-11", "Belgium", 1),
                    ("Gray Hickman", "1977-01-10", "France", 0),
                    ("Beau Bond", "1976-12-28", "Belgium", 4),
                    ("Wade Barker", "1980-09-26", "Belgium", 2),
                    ("Harlan Lowe", "1982-02-25", "Spain", 2),
                    ("Chantale Stokes", "1983-10-18", "Spain", 0),
                    ("Mallory Stuart", "1994-05-04", "Belgium", 2),
                    ("William Bartlett", "1999-03-31", "Belgium", 2),
                    ("Oleg Burnett", "1972-11-21", "Belgium", 1),
                    ("Alyssa Tucker", "2000-09-23", "United Kingdom", 1),
                    ("Berk Benson", "1985-03-01", "Belgium", 1),
                    ("Jerry Blankenship", "1985-07-11", "France", 0),
                    ("Jakeem Todd", "1985-08-16", "United Kingdom", 2),
                    ("Patricia Branch", "1991-04-20", "United Kingdom", 1),
                    ("Debra Mendez", "1992-02-12", "Italy", 0),
                    ("Pascale Shannon", "1998-08-14", "Germany", 3),
                    ("Shad Wells", "1992-11-30", "Spain", 3),
                    ("Rose Payne", "1994-05-10", "United Kingdom", 2),
                    ("Rashad Clements", "1973-08-10", "Germany", 2),
                    ("Heather Schultz", "1976-04-19", "France", 3),
                    ("Caryn Morgan", "1977-03-13", "France", 0),
                    ("Ivana Guthrie", "1979-12-09", "Germany", 4),
                    ("Dora Rogers", "1981-01-17", "France", 3),
                    ("Yael Schultz", "1982-02-20", "Belgium", 1),
                    ("Leroy Bright", "1983-03-18", "Spain", 4),
                    ("Joel Douglas", "1985-05-14", "Spain", 4),
                    ("Kylan Marks", "1984-04-02", "United Kingdom", 3),
                    ("Dakota Howe", "1986-06-22", "United Kingdom", 4),
                    ("Jeremy Cunningham", "1987-02-09", "France", 0),
                    ("Tanisha Mcgowan", "1988-12-20", "Italy", 0),
                    ("Tallulah Fowler", "1989-03-01", "Italy", 0),
                    ("Honorato Lowe", "1990-09-05", "France", 0),
                    ("Neil Leblanc", "1998-12-23", "Belgium", 1),
                    ("Roary Stephenson", "1996-05-11", "Italy", 3),
                    ("August Compton", "1977-12-11", "United Kingdom", 2),
                    ("Gretchen Kelly", "1978-09-02", "Germany", 0),
                    ("Thor Frederick", "1975-11-23", "France", 3),
                    ("Stacy Joseph", "1980-11-03", "United Kingdom", 4),
                    ("Idona Yates", "2000-03-02", "Belgium", 1),
                    ("Melyssa Tate", "1976-01-13", "France", 3),
                    ("Caldwell Frye", "1982-08-25", "Germany", 1),
                    ("Carlos Mcclain", "1989-04-06", "Spain", 4),
                    ("Jorden Ayala", "1986-08-04", "Italy", 0),
                    ("Shea Welch", "1978-12-01", "Spain", 2),
                    ("Lee Landry", "1997-06-30", "Germany", 3),
                    ("Fredericka Tillman", "1995-03-19", "Belgium", 4),
                    ("Griffith Mcknight", "1994-09-12", "France", 1),
                    ("Vera Todd", "1995-11-03", "Belgium", 1),
                    ("Tate Estes", "1998-09-25", "Germany", 4),
                    ("Eve Albert", "1978-01-13", "Spain", 2),
                    ("Plato Mcdonald", "1990-11-01", "France", 2),
                    ("Linus Camacho", "1973-01-05", "United Kingdom", 3),
                    ("Justine Mcintyre", "1973-07-23", "Italy", 3),
                    ("Bianca Joseph", "1979-01-29", "France", 0),
                    ("Colton Boone", "1985-09-28", "Germany", 0),
                    ("Charity Stokes", "1988-03-26", "Spain", 3),
                    ("Teagan Jimenez", "1991-02-08", "Spain", 2),
                    ("Hilary Lyons", "1991-02-24", "France", 0),
                    ("Candace Mcfadden", "1993-05-02", "Spain", 4),
                    ("Oleg Osborn", "1993-05-23", "France", 2),
                    ("Jeanette Nichols", "1993-09-13", "United Kingdom", 0),
                    ("Brianna Huff", "1993-12-31", "Spain", 4),
                    ("Riley Gates", "1994-11-23", "Belgium", 4),
                    ("Louis Pennington", "1996-10-05", "Germany", 0),
                    ("Dean Alexander", "1975-02-16", "Spain", 2),
                    ("Lavinia Mclaughlin", "1977-08-27", "United Kingdom", 4),
                    ("Veronica Patterson", "1974-05-19", "Italy", 3),
                    ("Emily Wagner", "1998-12-18", "Belgium", 4),
                    ("Nina Haley", "1971-06-14", "Belgium", 3),
                    ("Nina Rodriguez", "1976-10-22", "Belgium", 0),
                    ("Abel Pacheco", "1972-09-09", "Belgium", 1),
                    ("Catherine Butler", "1997-08-29", "France", 3),
                    ("Cody Freeman", "1996-02-26", "Spain", 2),
                    ("Azalia Riggs", "1975-07-04", "Germany", 4),
                    ("Gloria Crawford", "1980-06-21", "Germany", 1),
                    ("Macey Santos", "1982-03-27", "Belgium", 1),
                    ("Shaeleigh Gamble", "1992-08-10", "Germany", 2),
                    ("Ryan Kelley", "1997-07-23", "Belgium", 3),
                    ("Alisa Solomon", "1999-06-16", "France", 0),
                    ("Bethany Phillips", "2000-03-31", "Italy", 0),
                    ("Kadeem Mcfadden", "1986-09-28", "Italy", 0),
                    ("Jessica Sweet", "1993-05-20", "Belgium", 1),
                    ("Evan Mcmahon", "1983-01-08", "Germany", 3),
                    ("Ima Walsh", "1984-08-28", "France", 3),
                    ("Hyacinth Howe", "1985-08-04", "Belgium", 3),
                    ("Ezekiel Garrison", "1993-10-02", "Germany", 1),
                    ("Hermione Mcfarland", "1989-10-25", "Spain", 4)
                ]
            )

cur.executemany("INSERT INTO regions (name, code, taux) VALUES (?, ?, ?)",
                [
                    ("Auvergne-Rhône-Alpes", "FR-ARA", 21),
                    ("Bourgogne-Franche-Comté", "FR-BFC", 31),
                    ("Bretagne", "FR-BRE", 33),
                    ("Corse", "FR-COR", 12),
                    ("Centre-Val de Loire", "FR-CVL", 18),
                    ("Grand Est", "FR-GES", 22),
                    ("Hauts-de-France", "FR-HDF", 38),
                    ("Île-de-France", "FR-IDF", 34),
                    ("Normandie", "FR-NOR", 4),
                    ("Nouvelle-Aquitaine", "FR-NAQ", 17),
                    ("Occitanie", "FR-OCC", 28),
                    ("Pays de la Loire", "FR-PDL", 30),
                    ("Provence-Alpes-Côte d'Azur", "FR-PAC", 9)
                ]
            )

cur.executemany("INSERT INTO svgs (name, nom, largeur, hauteur, echelle, origineX, origineY) VALUES (?, ?, ?, ?, ?, ?, ?)",
                [
                    ("inspection.svg", "Inspection", 66.86, 69.7, 1.7, 14.2, 69.7),
                    ("cn.svg", "Cn", 63.14, 82.689, 1.2, 17.79, 82.689),
                    ("perceuse.svg", "Perceuse", 40.58, 79.18, 1.6, 13.99, 79.18),
                    ("tour.svg", "Tour", 89.02, 94.63, 1.2, 17.78, 94.63),
                    ("foreuse.svg", "Foreuse", 63.25, 97.19, 1.35, 14.25, 97.19),
                    ("robot.svg", "Robot", 78.78, 85.51, 1.6, 29.76, 85.51),
                    ("fraiseuse.svg", "Fraiseuse", 80.13, 98.88, 1.33, 15.44, 98.88)
                ]
            )

connection.commit()
connection.close()