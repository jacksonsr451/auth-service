from abc import ABC, abstractmethod

from auth.domain.users.user import User
from auth.infrastructure.models.user_model import UserModel


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> UserModel:
        pass

    @abstractmethod
    def get_all(self) -> list[UserModel]:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> UserModel:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> UserModel:
        pass
