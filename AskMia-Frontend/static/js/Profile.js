window.onload = function () {
  const studentId = localStorage.getItem("student_id");
  if (!studentId) return;

  fetch(`http://localhost:5000/api/student/${studentId}`)
    .then((response) => response.json())
    .then((data) => {
      if (data.error) {
        document.body.innerHTML = "Erreur : étudiant introuvable";
      } else {
        document.getElementById("nom").innerText = data.nom;
        document.getElementById("prenom").innerText = data.prenom;
        document.getElementById("classe").innerText = data.classe;
        document.getElementById("naissance").innerText = data.dateDeNaissance;
        document.getElementById("idEtudiant").innerText = data.numeroEtudiant;
      }
      console.log(data);
    });
};

function afficherFormulaire() {
  document.getElementById("formulaire-mdp").style.display = "block";
}

function handleChangePassword(redirectUrl) {
  document
    .getElementById("formulaire-mdp")
    .addEventListener("submit", function (e) {
      e.preventDefault();

      const ancienMdp = document.getElementById("ancien-mdp").value;
      const nouveauMdp = document.getElementById("nouveau-mdp").value;
      const confirmationMdp = document.getElementById("confirmation-mdp").value;
      const studentId = localStorage.getItem("student_id"); // Assure-toi que c’est bien stocké
      console.log(ancienMdp, nouveauMdp, confirmationMdp);
      if (!studentId) {
        alert("Erreur : Identifier vous.");
        window.location.href = "/connexion";
        return;
      } else if (nouveauMdp !== confirmationMdp) {
        alert("Les mots de passe ne correspondent pas.");
        return;
      } else {
        fetch("http://localhost:5000/api/change-password", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            student_id: studentId,
            ancien_mdp: ancienMdp,
            nouveau_mdp: nouveauMdp,
            confirmation_mdp: confirmationMdp
          }),
        })
          .then((res) => res.json())
          .then((data) => {
            if (data.success) {
              alert("Mot de passe mis à jour avec succès !");
              document.getElementById("formulaire-mdp").reset();
              window.location.href = redirectUrl;
            } else {
              alert("Erreur : " + data.message);
            }
          })
          .catch((err) => {
            console.error("Erreur fetch :", err);
            alert("Une erreur est survenue. Veuillez réessayer.");
          });
      }
    });
}
handleChangePassword("/connexion");
