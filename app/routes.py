from flask import Blueprint, request, redirect, url_for, render_template_string
from .models import User
from . import db

main = Blueprint('main', __name__)

# HTML básico para o formulário de cadastro
form_html = """
<!doctype html>
<html>
<head><title>Cadastro de Usuário</title></head>
<body>
<h2>Cadastro de Usuário</h2>
<form method="post">
    <label for="username">Nome de Usuário:</label><br>
    <input type="text" id="username" name="username" required><br><br>
    <label for="email">Email:</label><br>
    <input type="email" id="email" name="email" required><br><br>
    <label for="password">Senha:</label><br>
    <input type="password" id="password" name="password" required><br><br>
    <input type="submit" value="Cadastrar">
</form>
</body>
</html>
"""

@main.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('main.index'))
    
    return render_template_string(form_html)
