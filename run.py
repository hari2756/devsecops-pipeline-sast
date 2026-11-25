from app import create_app

app = create_app()

if __name__ == "__main__":
    # VULNERABILITY 6: Binding to all interfaces (0.0.0.0) with debug=True
    app.run(host="0.0.0.0", port=5000, debug=True)