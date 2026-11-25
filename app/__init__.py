from flask import Flask
from app.config import Config
from app.routes.auth import auth_bp
from app.routes.users import users_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(users_bp, url_prefix="/api/users")

    @app.route("/health")
    def health_check():
        return {"status": "healthy"}, 200

    return app