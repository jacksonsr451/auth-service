from auth.domain.user import User
from auth.domain.user_repository_interface import UserRepositoryInterface
from auth.domain.user_services_interface import UserServiceInterface


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface):
        self.user_repository = user_repository

    def create_user(self, username: str, password: str, email: str) -> User:
        user = User(username=username, password=password, email=email)
        return self.user_repository.create(user)

    def get_users(self) -> list[User]:
        return self.user_repository.get_all()

    def get_user_by_username(self, username: str) -> User:
        return self.user_repository.get_by_username(username)

    def get_user_by_email(self, email: str) -> User:
        return self.user_repository.get_by_email(email)
