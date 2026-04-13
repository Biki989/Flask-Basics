from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager,create_access_token,jwt_required,get_jwt_identity

app = Flask(__name__)

# Secret key (change in production)
app.config["JWT_SECRET_KEY"] = "super-secret-key"

jwt = JWTManager(app)

# Dummy user database
users = {
    "biki": "1234"
}

# Home route
@app.route("/")
def home():
    return jsonify({"message": "REST API with JWT"})

# Login route
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if users.get(username) == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token)

    return jsonify({"error": "Invalid credentials"}), 401


# Protected route
@app.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user)


if __name__ == "__main__":
    app.run(debug=True)