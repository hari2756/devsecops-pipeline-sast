import sqlite3

# VULNERABILITY 1: Hardcoded credential / secret
API_SECRET_KEY = "sk_live_secretToken9988776655"

def query_user(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABILITY 2: SQL Injection via unescaped string formatting
    query = f"SELECT * FROM accounts WHERE username = '{user_input}'"
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print("Application loaded successfully.")