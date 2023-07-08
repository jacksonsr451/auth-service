from abc import ABC, abstractmethod

from auth.application.dtos.user_dto import UserDTO


class UserServiceInterface(ABC):
    @abstractmethod
    def create_user(self, username: str, password: str, email: str) -> UserDTO:
        pass

    @abstractmethod
    def get_users(self) -> list[UserDTO]:
        pass

    @abstractmethod
    def get_user_by_username(self, username: str) -> UserDTO:
        pass

    @abstractmethod
    def get_user_by_email(self, email: str) -> UserDTO:
        pass
