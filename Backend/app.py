from flask import *
import os
from pathlib import Path
import datetime
import requests

import models

RASA_API_URL= 'http://localhost:5005/webhooks/rest/webhook'

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

@app.route('/webhook', methods=['POST'])
def webhook():
    user_message=request.json['message']
    print("User Message:", user_message)

    rasa_response = requests.post(RASA_API_URL, json={'message' : user_message})
    rasa_response_json = rasa_response.json()

    print("Rasa Resoonse:", rasa_response_json)

    bot_response = rasa_response_json[0]['text'] if rasa_response_json else "Désolé, je n'ai pas compris."
    return jsonify({'response': bot_response})

    
# à mettre dans des routes selon le js
"""models.create_new_etudiant(
    22101371, "Lampin", "Vivien", datetime.datetime(2003, 10, 4), "test", "IATIC3")
print(models.get_mdp_from_etudiant(22101371))
models.update_mdp_etudiant(22101371, "test2")
print(models.get_mdp_from_etudiant(22101371))
models.delete_etudiant(22101371)
print(models.get_mdp_from_etudiant(22101371))
models.update_mdp_etudiant(22101371, "test2")
"""

