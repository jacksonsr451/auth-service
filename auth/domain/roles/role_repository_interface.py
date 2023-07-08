from abc import ABC, abstractmethod

from auth.domain.roles.role import Role
from auth.infrastructure.models.role_model import RoleModel


class RoleRepositoryInterface(ABC):
    @abstractmethod
    def create(self, role: Role) -> RoleModel:
        pass
