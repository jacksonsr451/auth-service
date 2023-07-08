from auth.domain.roles.role import Role
from auth.infrastructure.adapters.database import session
from auth.domain.roles.role_repository_interface import RoleRepositoryInterface
from auth.infrastructure.models.role_model import RoleModel


class RoleRepositoryImpl(RoleRepositoryInterface):
    def create(self, role: Role) -> RoleModel:
        role = RoleModel.query.filter_by(name=role.name).first()
        if role is None:
            role = RoleModel(name=role.name)
            session.add(role)
            session.commit()
        return role
