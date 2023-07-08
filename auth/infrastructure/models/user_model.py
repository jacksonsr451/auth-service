from auth.domain.users.user import User
from auth.infrastructure.adapters.database import db
from sqlalchemy.orm import relationship


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = relationship("RoleModel")

    def __init__(self, username, password, email, role_id):
        self.username = username
        self.password = password
        self.email = email
        self.role_id = role_id

    def to_entity(self) -> User:
        return User(
            username=self.username,
            password=self.password,
            email=self.email,
            role_id=self.role
        )
