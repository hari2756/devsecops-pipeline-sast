import sqlite3
from flask import Flask, request
 
app = Flask(__name__)
 
# VULNERABILITY 1: Hardcoded password / secret
DB_PASSWORD = "SuperSecret123!"
API_KEY = "sk-test-1234567890abcdef"
 
 
@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
 
    # VULNERABILITY 2: SQL injection (user input concatenated into query)
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    cursor.execute(query)
 
    return str(cursor.fetchall())
 
 
if __name__ == "__main__":
    app.run(debug=True)