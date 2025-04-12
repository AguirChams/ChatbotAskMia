document.addEventListener("DOMContentLoaded", function () {
  const input = document.getElementById("message-input");
  const chatBox = document.getElementById("chat-box");
  const sendBtn = document.getElementById("send-button");

  // Fonction pour transformer les URLs en liens cliquables
  function ajouterLiens(message) {
    // Expression régulière pour détecter les URLs
    const urlRegex = /https?:\/\/[^\s]+/g;
    return message.replace(urlRegex, function (url) {
      return `<a href="${url}" target="_blank" class="link">${url}</a>`;
    });
  }

  function ajouterMessage(message, classe, isHTML = false) {
    const messageElement = document.createElement("div");
    messageElement.classList.add(classe);

    if (isHTML) {
      // Remplace \n par <br> pour garder les retours à la ligne
      message = ajouterLiens(message);  // Transforme les liens avant l'affichage
      messageElement.innerHTML = message.replace(/\n/g, "<br>");
    } else {
      messageElement.textContent = message;
    }

    chatBox.appendChild(messageElement);
    chatBox.scrollTop = chatBox.scrollHeight;
  }

  function envoyerMessage() {
    const message = input.value.trim();
    if (message !== "") {
      // Affiche le message utilisateur dans la chatbox
      ajouterMessage(message, "user-message");

      // Vide le champ de saisie
      input.value = "";

      // Envoie le message à l'API Flask qui relaye à Rasa
      fetch("/api/chat", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: message }),
      })
        .then((res) => res.json())
        .then((data) => {
          if (Array.isArray(data)) {
            data.forEach((d) => {
              if (d.text) {
                // Affiche les réponses en interprétant les sauts de ligne et en rendant les liens cliquables
                ajouterMessage(d.text, "bot-message", true);
              }
            });
          }
        })
        .catch((err) => {
          console.error("Erreur en contactant le chatbot :", err);
          ajouterMessage("Oups ! Le serveur ne répond pas.", "bot-message");
        });
    }
  }

  // Touche Entrée
  input.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
      e.preventDefault();
      envoyerMessage();
    }
  });

  // Clic sur bouton "Entrer"
  sendBtn.addEventListener("click", envoyerMessage);
});
