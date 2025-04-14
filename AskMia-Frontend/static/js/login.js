function handleLogin(formId, redirectUrl) {
  document.getElementById(formId).addEventListener("submit", function (e) {
    e.preventDefault();

    if (formId === "student-login") {
      const studentId = document.getElementById("Student_id").value.trim();
      const password = document.getElementById("password").value;
 
      fetch("http://127.0.0.1:5000/api/login/student", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          student_id: studentId,
          password: password
        })
      })
      .then(res => res.json())
      .then(data => {
        console.log("Réponse serveur :", data);
        if (data.success) {
          localStorage.setItem("student_id", studentId); // stocke l’ID dans le localStorage
          window.location.href = redirectUrl;
        }else {
          alert("Identifiants invalides");
        }
      })
      .catch(err => {
        console.error("Erreur fetch :", err);
      });

    } else if (formId === "admin-login") {
      const adminId = document.getElementById("Admin_id").value;

      fetch("http://localhost:5000/api/login/admin", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          admin_id: adminId
        })
      })
      .then(res => res.json())
      .then(data => {
        if (data.success) {
          window.location.href = redirectUrl;
        } else {
          alert("ID admin incorrect");
        }
      })
      .catch(err => {
        console.error("Erreur fetch admin :", err);
      });
    }
  });
}

handleLogin("student-login", "/chatbot");
handleLogin("admin-login", "/creerCompte");


/*créér compte : models.create_new_etudiant(22101371, "Lampin", "Vivien", datetime.datetime(2003, 10, 4), "test123", "IATIC3")*/
