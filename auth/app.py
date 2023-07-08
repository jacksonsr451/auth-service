from flask import Flask

from auth.infrastructure.adapters import database, migrate
from auth.interfaces.controllers.user_controller import auth_bp
from commands import create_superuser


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/v1/auth')
    database.init_app(app)
    migrate.init_app(app)
    create_superuser.init_app(app)
    return app
