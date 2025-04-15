# 🤖 AskMia — Chatbot Universitaire pour l'ISTY

Bienvenue sur **AskMia**, le chatbot intelligent conçu pour assister les étudiants et visiteurs de l'**ISTY** 🏫 !  
Que vous ayez besoin de connaître les horaires du CROUS 🥗 ou d'en apprendre davantage sur les spécialités proposées à l'école 💼, **AskMia** est là pour vous répondre rapidement et efficacement !

---

## 🚀 Fonctionnalités

- 📅 Connaître les **horaires d'ouverture du CROUS**
- 📚 Découvrir les **spécialités disponibles à l'ISTY**
- 🤔 Obtenir des **informations utiles sur la vie universitaire**
- Et bien plus encore...

---

## ⚙️ Installation (Ubuntu uniquement)

Suivez les étapes ci-dessous pour installer et lancer AskMia sur votre machine Ubuntu 👇

### 1. 🔧 Installer Python (version ≤ 3.10)

```bash
sudo apt update
sudo apt install python3.10 python3.10-venv python3.10-pip
```

### 2. 🧪 Créer un environnement virtuel (optionnel mais recommandé)

```bash
python3.10 -m venv venv
source venv/bin/activate
```

### 3. 📦 Installer les dépendances

```bash
pip install flask sqlalchemy rasa-sdk
```

### 4. 🧬 Cloner le dépôt Git

```bash
git clone https://github.com/AguirChams/ChatbotAskMia.git
cd ChatbotAskMia/Backend
```

---

## 🟢 Démarrage

### 1. Lancer le serveur Flask

```bash
python -m flask run --debug
```

### 2. Lancer le serveur Rasa

Dans un **autre terminal**, depuis le dossier `ChatbotAskMia/Backend/rasa_project` :

```bash
rasa run --enable-api
rasa run actions
```

## 🌐 Accès au chatbot

Rendez-vous sur [http://127.0.0.1:5000/](http://127.0.0.1:5000/) dans votre navigateur pour discuter avec **AskMia** 💬

---

### 📫 Contact

Développé par des étudiants de l'ISTY.
