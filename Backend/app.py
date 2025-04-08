from flask import *
import os
from pathlib import Path
import datetime

import models

directoryBack = os.getcwd()
directoryFront = str(
    Path(directoryBack).parents[0]) + os.sep + "AskMia-Frontend"
app = Flask(__name__, template_folder=directoryFront)


@app.route("/")
def page_principale():
    return render_template("Index.html")


@app.route("/connexion")
def page_connexion():
    return render_template("Create-account.html")


# à mettre dans des routes selon le js
models.create_new_etudiant(
    22101371, "Lampin", "Vivien", datetime.datetime(2003, 10, 4), "test", "IATIC3")
print(models.get_mdp_from_etudiant(22101371))
models.update_mdp_etudiant(22101371, "test2")
print(models.get_mdp_from_etudiant(22101371))
models.delete_etudiant(22101371)
print(models.get_mdp_from_etudiant(22101371))
models.update_mdp_etudiant(22101371, "test2")
