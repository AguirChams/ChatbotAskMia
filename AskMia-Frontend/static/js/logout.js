// Fonction de gestion de la déconnexion
function handleLogout(formId, redirectUrl) {
    const form = document.getElementById(formId);
    
    if (form) {
        form.addEventListener("submit", function (e) {
            e.preventDefault();  // Empêche l'envoi du formulaire
            window.location.href = redirectUrl;  // Redirige vers la page de login
        });
    }
}

// Applique la redirection pour la déconnexion après avoir vérifié que le formulaire existe
document.addEventListener("DOMContentLoaded", function() {
    handleLogout("Logout", "/");  // Redirection vers la page Login
});
