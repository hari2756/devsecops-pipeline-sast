import sqlite3

# VULNERABILITY 1: Plaintext secret token
API_SECRET_KEY = "sk_live_2026_abcdef1234567890abcdef1234567890"

def query_user(user_input):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # VULNERABILITY 2: SQL Injection via unformatted string concatenation
    query = "SELECT * FROM accounts WHERE username = '%s'" % user_input
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    print("Application loaded.")