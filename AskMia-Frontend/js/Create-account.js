function handleLogin(formId, redirectUrl) {
  document.getElementById(formId).addEventListener("submit", function (e) {
    e.preventDefault();
    window.location.href = redirectUrl;
  });
}

handleLogin("Logout", "Login.html");
handleLogin("Create-acc", "create-account.html");
