from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de datos en memoria
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
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
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", ""),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

if __name__ == "__main__":
    app.run(debug=True)