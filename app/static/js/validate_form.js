function validateForm() {
    var password = document.getElementById("password").value;
    var confirm = document.getElementById("confirm").value;

    if (password.length < 8) {
        alert("A senha deve ter pelo menos 8 caracteres.");
        return false;
    }

    if (password !== confirm) {
        alert("A senha e a confirmação de senha não correspondem.");
        return false;
    }

    return true; // Prosseguir com o envio do formulário se tudo estiver certo
}