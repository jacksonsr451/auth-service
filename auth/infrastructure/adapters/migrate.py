from flask_migrate import Migrate

from auth.infrastructure.adapters.database import db

migrate = Migrate()


def init_app(app):
    migrate.init_app(app, db)
    return migrate
