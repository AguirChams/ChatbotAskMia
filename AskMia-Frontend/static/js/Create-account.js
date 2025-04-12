function handleLogin(formId, redirectUrl) {
  document.getElementById(formId).addEventListener("submit", function (e) {
    e.preventDefault();
    
    
    const student = {
      surname: document.getElementById("surname").value,
      name: document.getElementById("name").value,
      birthdate: document.getElementById("birthdate").value,
      class: document.getElementById("class").value,
      password: document.getElementById("password").value,
    };

    try {
    const response = await fetch("/api/create_account", {
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
      alert("Erreur : " + result.message);
    }
  } catch (error) {
    console.error("Erreur réseau :", error);
    alert("Erreur lors de la création du compte.");
  }
    window.location.href = redirectUrl;
  });
}

handleLogin("Logout", "/connexion");
handleLogin("Create-acc", "/creerCompte");
