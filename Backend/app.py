from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
from pathlib import Path
import datetime
import models
import hashlib
import requests

directoryBack = os.getcwd()
directoryFront = str(Path(directoryBack).parents[0]) + os.sep + "AskMia-Frontend"
app = Flask(__name__,
            template_folder=directoryFront,
            static_folder=os.path.join(directoryFront, "static"))

CORS(app)

# Page d'accueil
@app.route("/")
def page_principale():
    return render_template("Index.html")

@app.route("/connexion")
def page_connexion():
    return render_template("Login.html")

@app.route("/creerCompte")
def creer_compte():
    return render_template("Create-account.html")

# ----------- Create account API ----------- #
@app.route("/api/create_account", methods=["POST"])
def api_create_account():
    data = request.get_json()

    try:
        nom = data.get("surname")
        prenom = data.get("name")
        birthdate = data.get("birthdate")
        classe = data.get("class")
        password = data.get("password")

        new_id = models.get_next_etudiant_id()
        print("Nouvel ID étudiant :", new_id)

        birthdate_dt = datetime.datetime.strptime(birthdate, "%Y-%m-%d")

        success = models.create_new_etudiant(new_id, nom, prenom, birthdate_dt, password, classe)

        if success:
            return jsonify({"success": True, "message": "Compte créé avec succès."})
        else:
            return jsonify({"success": False, "message": "Échec de la création du compte."})

    except Exception as e:
        print("Erreur lors de la création du compte :", str(e))
        return jsonify({"success": False, "message": "Erreur interne", "error": str(e)}), 500

    
    if success:
        return "compte créé"
        return jsonify({"success": True, "message": "Compte créé avec succès."} )
        
    else:
        return jsonify({"success": False, "message": "Échec de la création du compte."}, {"data" : data})


# ----------- Login API ----------- #
@app.route("/api/login/student", methods=["POST"])
def login_student():
    data = request.get_json()
    student_id = int(data.get("student_id"))
    password = data.get("password")

    password_hash = hashlib.sha256(password.encode()).hexdigest()
    stored_password = models.get_mdp_from_etudiant(student_id)

    if stored_password == password_hash:
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

@app.route("/api/login/admin", methods=["POST"])
def login_admin():
    data = request.get_json()
    admin_id = data.get("admin_id")
    if admin_id == "admin123":
        return jsonify({"success": True})
    else:
        return jsonify({"success": False})

# ----------- Chatbot Rasa API ----------- #
RASA_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/api/chat", methods=["POST"])
def chat_with_rasa():
    user_message = request.json.get("message")
    response = requests.post(RASA_URL, json={"message": user_message})
    rasa_response = response.json()
    return jsonify(rasa_response)

# Debug pages
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
    html = "<h2>Admins enregistrés :</h2><ul>"
    for a in admins:
        html += f"<li>ID: {a.clef}</li>"
    html += "</ul>"
    return html

@app.route("/debug/create")
def debug_create_account_debug():
    models.create_new_etudiant(123, "Dupont", "Jean", datetime.datetime(2000, 1, 1), "password123", "Informatique")
    return "Compte créé (debug)"

@app.route("/debug/createAdmin")
def debug_create_admin_debug():
    models.create_new_clef_admin(1)
    return "Admin créé (debug)"

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/profil")
def page_profil():
    return render_template("profile.html")
