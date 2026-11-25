import hashlib
from flask import Blueprint, request, jsonify

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json() or {}
    username = data.get("username", "")
    password = data.get("password", "")

    # VULNERABILITY 3: Broken/Weak Cryptography (MD5 used for password hashing)
    hashed_password = hashlib.md5(password.encode()).hexdigest()

    if username == "admin" and hashed_password == "21232f297a57a5a743894a0e4a801fc3":
        return jsonify({"status": "authenticated", "user": username}), 200
    
    return jsonify({"status": "unauthorized"}), 401