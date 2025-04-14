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

@app.route("/profil")
def page_profil():
    return render_template("profile.html")

# ----------- Update Password API ----------- #
@app.route("/api/change-password", methods=["POST"])
def change_password():
    data = request.get_json()

    student_id = int(data.get("student_id"))
    ancien_mdp = data.get("ancien_mdp")
    nouveau_mdp = data.get("nouveau_mdp")
    confirmation_mdp = data.get("confirmation_mdp")

    if nouveau_mdp != confirmation_mdp:
        return jsonify({"success": False, "message": "Les mots de passe ne correspondent pas."})

    # Vérifier l'ancien mot de passe
    ancien_mdp_hash = hashlib.sha256(ancien_mdp.encode()).hexdigest()
    stored_password = models.get_mdp_from_etudiant(student_id)

    if stored_password != ancien_mdp_hash:
        return jsonify({"success": False, "message": "Ancien mot de passe incorrect."})

    # Hacher et enregistrer le nouveau mot de passe
    nouveau_mdp_hash = hashlib.sha256(nouveau_mdp.encode()).hexdigest()
    updated = models.update_password_etudiant(student_id, nouveau_mdp_hash)

    if updated:
        return jsonify({"success": True, "message": "Mot de passe mis à jour avec succès."})
    else:
        return jsonify({"success": False, "message": "Erreur lors de la mise à jour du mot de passe."})

# ----------- Fetch Profile API ----------- #
@app.route("/api/student/<int:student_id>", methods=["GET"])
def get_student_by_id(student_id):
    etudiant = models.get_etudiant_by_id(student_id)
    if etudiant:
        return jsonify({
            "numeroEtudiant": etudiant.numeroEtudiant,
            "nom": etudiant.nom,
            "prenom": etudiant.prenom,
            "dateDeNaissance": etudiant.dateDeNaissance.strftime("%Y-%m-%d"),
            "classe": etudiant.classe
        })
    else:
        return jsonify({"error": "Étudiant introuvable"}), 404


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
    try:
        data = request.get_json()
        print("Requête reçue :", data)

        student_id = int(data.get("student_id"))
        password = data.get("password")

        password_hash = hashlib.sha256(password.encode()).hexdigest()
        stored_password = models.get_mdp_from_etudiant(student_id)

        print(f"[DEBUG] Tentative de connexion avec ID: {student_id}")
        print(f"[DEBUG] Mot de passe entré: {password}")
        print(f"[DEBUG] Hash calculé: {password_hash}")
        print(f"[DEBUG] Hash stocké: {stored_password}")

        if stored_password == password_hash:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})
    except Exception as e:
        print("❌ ERREUR :", str(e))
        return jsonify({"success": False, "message": "Erreur interne", "error": str(e)}), 500


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


