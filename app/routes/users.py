import sqlite3
from flask import Blueprint, request, jsonify, render_template_string

users_bp = Blueprint("users", __name__)

def get_db_connection():
    conn = sqlite3.connect("enterprise_users.db")
    conn.row_factory = sqlite3.Row
    return conn

@users_bp.route("/profile", methods=["GET"])
def get_user_profile():
    user_id = request.args.get("id", "")
    conn = get_db_connection()
    cursor = conn.cursor()

    # VULNERABILITY 4: Raw SQL Injection via string concatenation
    query = "SELECT id, username, email FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()

    if user:
        return jsonify(dict(user)), 200
    return jsonify({"error": "User not found"}), 404

@users_bp.route("/welcome", methods=["GET"])
def welcome_banner():
    name = request.args.get("name", "Guest")
    
    # VULNERABILITY 5: Server-Side Template Injection / Reflected XSS
    template = f"<h1>Welcome back to the portal, {name}!</h1>"
    return render_template_string(template)