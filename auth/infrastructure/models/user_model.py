from sqlalchemy.orm import relationship

from auth.application.dtos.user_dto import UserDTO
from auth.infrastructure.adapters.database import db


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    role = relationship('RoleModel')

    def __init__(self, username, password, email, role_id):
        self.username = username
        self.password = password
        self.email = email
        self.role_id = role_id

    def to_dto(self) -> UserDTO:
        return UserDTO(
            username=self.username,
            email=self.email,
            role_id=self.role_id,
        )
