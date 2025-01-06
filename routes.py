from flask import jsonify, render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash
from models import db, User  # Importar la base de datos y el modelo User

# Ruta para la página de login
from werkzeug.security import generate_password_hash, check_password_hash

# Función para crear un usuario
def create_user(username, password):
    hashed_password = generate_password_hash(password)
    new_user = User(username=username, password=hashed_password, victorias = 0, derrotas = 0, empates = 0)
    db.session.add(new_user)
    db.session.commit()

# Ruta para la página de login
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        error = None
        
        # Buscar al usuario en la base de datos
        user = User.query.filter_by(username=username).first()
        
        # Verificar la contraseña con el hash
        if user and check_password_hash(user.password, password):
            #Prevenir en el login que las estadísticas no sean null, si lo son las cambiamos a 0
            if user.victorias is None:
                user.victorias = 0
            if user.derrotas is None:
                user.derrotas = 0
            if user.empates is None:
                user.empates = 0
                #Logeamos
            login_user(user)
            #Entramos al index
            return redirect(url_for("dashboard"))
        else:
            return render_template("login.html", error = "Ha ocurrido un error, es posible que el usuario y la contraseña no coincidan")
    return render_template("login.html")

#Función para registrarse
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        
        # Revisa si el usuario existe, y si existe nos muestra el error
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            return render_template("signup.html", error="El nombre de usuario ya existe.")
        
        # Si no existe lo crea
        create_user(username, password)
        return redirect(url_for("login"))
    
    return render_template("signup.html")

# Esto asegura que solo los usuarios logueados puedan acceder al dashboard
@login_required
def dashboard():
    # Renderiza la plantilla del dashboard y pasa el usuario actual como contexto
    return render_template('index.html', active_page = "Home", user=current_user)

@login_required
def UserInfo():
    # Renderiza la plantilla de la informacion y pasa el usuario actual como contexto
    return render_template('UserInfo.html', active_page = "UserInfo" ,user=current_user)

#Funciones que devuelven las páginas de error
def error404(e):
    return render_template('error/404.html', active_page="error404", user=current_user), 404

def error500(e):
    return render_template('error/500.html', active_page="error500", user=current_user), 500

def error403(e):
    return render_template('error/403.html', active_page="error403", user=current_user), 500

# Ruta para cerrar sesión
def logout():
    logout_user()
    return redirect(url_for("login"))

#Actualiza las estadísticas tras una partida
@login_required
def update_statistics():
    data = request.json
    result = data.get('result')

    if result == 'victory':
        current_user.victorias = (current_user.victorias or 0) + 1
    elif result == 'defeat':
        current_user.derrotas = (current_user.derrotas or 0) + 1
    elif result == 'draw':
        current_user.empates = (current_user.empates or 0) + 1

    db.session.commit()
    return jsonify({"status": "success"})