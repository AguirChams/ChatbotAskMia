document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("message-input");
    const chatBox = document.getElementById("chat-box");
    const sendBtn = document.getElementById("send-button");
  
    function ajouterMessage(message, classe) {
      const messageElement = document.createElement("div");
      messageElement.textContent = message;
      messageElement.classList.add(classe);
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
                  ajouterMessage(d.text, "bot-message");
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
  