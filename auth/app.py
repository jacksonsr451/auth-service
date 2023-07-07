from flask import Flask

from auth.interfaces.controllers.user_controller import auth_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(auth_bp, url_prefix='/v1')
    return app
