from abc import ABC, abstractmethod

from auth.domain.user import User


class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, password: str, email: str) -> User:
        pass

    @abstractmethod
    def get_users(self) -> list[User]:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> User:
        pass
