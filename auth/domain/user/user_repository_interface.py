from abc import ABC, abstractmethod

from auth.domain.user import User


class UserRepositoryInterface(ABC):
    @abstractmethod
    def create(self, user: User) -> User:
        pass

    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def get_by_username(self, username: str) -> User:
        pass

    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass
