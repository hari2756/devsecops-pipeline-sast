import os
import sqlite3
from flask import Flask, request

app = Flask(__name__)

# FIXED: secrets come from environment variables, not the source code
DB_PASSWORD = os.environ.get("DB_PASSWORD")
API_KEY = os.environ.get("API_KEY")


@app.route("/user")
def get_user():
    username = request.args.get("username")
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # FIXED: parameterized query, user input is never joined into the SQL string
    cursor.execute("SELECT * FROM users WHERE name = ?", (username,))

    return str(cursor.fetchall())


if __name__ == "__main__":
    app.run(debug=False)