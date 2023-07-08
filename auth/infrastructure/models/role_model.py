from auth.domain.roles.role import Role
from auth.infrastructure.adapters.database import db


class RoleModel(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, name):
        self.name = name

    def to_entity(self) -> Role:
        return Role(name=self.name)
