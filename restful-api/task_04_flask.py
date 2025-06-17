from flask import Flask, jsonify, request

app = Flask(__name__)

# INICIALIZAR USUARIOS VACÍOS (no incluir datos de prueba)
users = {}


@app.route("/")
def home():
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    # Devolver lista de nombres de usuario (keys del diccionario)
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    # Validar que se proporcionó username
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Validar si el usuario ya existe
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Crear nuevo usuario con estructura completa
    new_user = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }

    # Guardar usuario
    users[username] = new_user

    return jsonify({
        "message": "User added",
        "user": new_user
    }), 201


if __name__ == "__main__":
    app.run(debug=True)
