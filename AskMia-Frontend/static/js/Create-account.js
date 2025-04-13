function createAccount(formId, redirectUrl) {
  document.getElementById(formId).addEventListener("submit", async function (e) {
    e.preventDefault();

    const surnameInput = document.getElementById("surname");
    const nameInput = document.getElementById("name");
    const classInput = document.getElementById("class");
    const isAlphabetic = /^[A-Za-z]+$/;

    let value = surnameInput.value.trim();

    if (!isAlphabetic.test(value)) {
      alert("Le nom doit être alphabétique.");
      return;
    }

    value = nameInput.value.trim();

    if (!isAlphabetic.test(value)) {
      alert("Le prénom doit être alphabétique.");
      return;
    }

    value = classInput.value.trim().toLowerCase();

    if (!["iatic 3", "iatic 4", "iatic 5"].includes(value)) {
      alert("La classe doit être IATIC 3, IATIC 4 ou IATIC 5.");
      return;
    }

    const student = {
      surname: document.getElementById("surname").value,
      name: document.getElementById("name").value,
      birthdate: document.getElementById("birthdate").value,
      class: document.getElementById("class").value,
      password: document.getElementById("password").value,
    };

    try {
      const response = await fetch("http://localhost:5000/api/create_account", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(student),
      });

      const result = await response.json();

      if (result.success) {
        alert("Compte créé avec succès !");
        window.location.href = redirectUrl;
      } else {
        alert("Erreur : " + result.message );
      }
    } catch (error) {
      console.log("Erreur réseau :", error);
      alert("Erreur lors de la création du compte.");
      
    }
  });
}


createAccount("Logout", "/connexion");
createAccount("Create-acc", "/creerCompte");
