from flask import Flask, render_template, request, jsonify
from IA_algorithm import find_best_move
from flask_login import LoginManager
from models import User, db
import config
from routes import *
app = Flask(__name__)


# Cargar la configuración desde el archivo config.py
app.config.from_object(config.Config)

# Inicializar la base de datos
db.init_app(app)

# Inicializar Flask-Login
login_manager = LoginManager(app)
# Redirige a la página de login si el usuario no está autenticado
login_manager.login_view = "login"

# Cargar el usuario desde la base de datos por ID
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registrar las rutas
app.add_url_rule('/login', view_func=login, methods=["GET", "POST"])
app.add_url_rule('/', view_func=dashboard)
app.add_url_rule('/logout', view_func=logout)
app.add_url_rule('/UserInfo', view_func=UserInfo)
app.add_url_rule('/update_statistics', view_func=update_statistics, methods=["POST"])
app.add_url_rule('/signup', view_func=signup, methods=["GET", "POST"])

#Registrar los errores
app.register_error_handler(404, error404)
app.register_error_handler(403, error403)
app.register_error_handler(500, error500)

@app.route("/ai_move", methods=["POST"])
def ai_move():
    data = request.json
    board = data["board"]

    # Encuentra el mejor movimiento usando Minimax
    move = find_best_move(board)
    #devuelve el json con el index del movimiento
    return jsonify({"move": move})

if __name__ == "__main__":
    #Esta opción permite que dispositivos de tu red accedan a este proyecto, si no quieres que sea así descomentalo y comenta la opción que hay debajo
    app.run(host='0.0.0.0', port=5000, debug=True)
    # app.run(debug=True)
