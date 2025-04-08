# Chatbot AskMia

# Installation
Personnellement je préfère passer par anaconda pour ne pas saboter mes interpréteurs Python, mais chacun fait comme il veut : https://www.anaconda.com/download/success
Ensuite une fois que c'est installé :
```sh
conda create -n mia python=3.11.9
conda activate mia
```

Les dépendances de Python :
```sh
python -m pip install flask
python -m pip install sqlalchemy
```

Lancer le serveur web :
```sh
git clone https://github.com/AguirChams/ChatbotAskMia.git
cd ChatbotAskMia/Backend
python -m flask run --debug
```
Puis aller sur l'URL ```http://127.0.0.1:5000/``` pour accéder au site (avec à terme des liens entre les routes).
Le mode debug est bien parce que ça rafraîchit en temps réel la page quand des nouvelles modifs sont sauvegardées, pas besoin de relancer à chaque fois.