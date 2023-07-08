import dotenv
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()


def init_app(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = dotenv.get_key(
        '.env', 'SQLALCHEMY_DATABASE_URI'
    )
    db.init_app(app)
    app.db = db


engine = create_engine(dotenv.get_key('.env', 'SQLALCHEMY_DATABASE_URI'))
Session = sessionmaker(bind=engine)

session = Session()
