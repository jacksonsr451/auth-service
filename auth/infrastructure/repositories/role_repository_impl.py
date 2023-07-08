from auth.domain.roles.role import Role
from auth.domain.roles.role_repository_interface import RoleRepositoryInterface
from auth.infrastructure.adapters.database import session
from auth.infrastructure.models.role_model import RoleModel


class RoleRepositoryImpl(RoleRepositoryInterface):
    def create(self, role: Role) -> RoleModel:
        role_model = RoleModel.query.filter_by(name=role.name).first()
        if role_model is None:
            role_model = RoleModel(name=role.name)
            session.add(role_model)
            session.commit()
        return role_model
