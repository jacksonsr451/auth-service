from re import U
from auth.domain.user import User
from auth.domain.user_repository_interface import UserRepositoryInterface
from auth.domain.user_services_interface import UserServiceInterface
from auth.infrastructure.models.user_model import UserModel


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, username: str, password: str, email: str) -> User:
        user = self.user_repository.create(
            UserModel(username=username, password=password, email=email))
        return User(username=user.username, password=user.password, email=user.email)

    def get_users(self) -> list[User]:
        users = self.user_repository.get_all()
        return [User(username=user.username, password=user.password, email=user.email) for user in users]

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.get_by_username(username)
        return User(username=user.username, password=user.password, email=user.email)

    def get_user_by_email(self, email: str) -> User:
        user = self.user_repository.get_by_email(email)
        return User(username=user.username, password=user.password, email=user.email)
