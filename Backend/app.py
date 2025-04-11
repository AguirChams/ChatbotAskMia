from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from pathlib import Path
import datetime
import models
import hashlib

directoryBack = os.getcwd()
directoryFront = str(Path(directoryBack).parents[0]) + os.sep + "AskMia-Frontend"
app = Flask(__name__, 
            template_folder=directoryFront, 
            static_folder=os.path.join(directoryFront, "static"))

CORS(app)  # Pour permettre à JS (frontend) de communiquer avec Flask

@app.route("/")
def page_principale():
    return render_template("Index.html")

@app.route("/connexion")
def page_connexion():
    return render_template("Login.html")

@app.route("/debug/create")
def debug_create_account():
    models.create_new_etudiant(123, "Dupont", "Jean", datetime(2000, 1, 1), "password123", "Informatique")

# -------- ROUTES API -------- #
@app.route("/api/login/student", methods=["POST"])
def login_student():
    data = request.get_json()
    student_id = int(data.get("student_id"))
    password = data.get("password")

    # Hasher le mot de passe entré par l'utilisateur
    password_hash = hashlib.sha256(password.encode()).hexdigest()

    stored_password = models.get_mdp_from_etudiant(student_id)

    print("Mot de passe stocké :", stored_password)
    print("Mot de passe hashé saisi :", password_hash)

    if stored_password == password_hash:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})



@app.route("/api/login/admin", methods=["POST"])
def login_admin():
    data = request.get_json()
    admin_id = data.get("admin_id")

    # Ici tu peux ajouter ta logique admin plus tard
    if admin_id == "admin123": 
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route("/debug/etudiants")
def debug_etudiants():
    etudiants = models.get_all_etudiants()
    html = "<h2>Étudiants enregistrés :</h2><ul>"
    for e in etudiants:
        html += f"<li>ID: {e.numeroEtudiant}, Nom: {e.nom}, Prénom: {e.prenom}, MDP hashé: {e.motDePasse}, Classe: {e.classe}</li>"
    html += "</ul>"
    return html

@app.route("/debug/admins")
def debug_admins():
    admins = models.get_all_admins()
    html = "<h2>admins enregistrés :</h2><ul>"
    for a in admins:
        html += f"<li>ID: {a.clef}</li>"
    html += "</ul>"
    return html

if __name__ == "__main__":
    app.run(debug=True)
