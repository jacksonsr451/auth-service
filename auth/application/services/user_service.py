from auth.domain.roles.role import Role
from auth.domain.roles.role_repository_interface import RoleRepositoryInterface
from auth.domain.users.user import User
from auth.domain.users.user_repository_interface import UserRepositoryInterface
from auth.domain.users.user_services_interface import UserServiceInterface


class UserService(UserServiceInterface):
    def __init__(self, user_repository: UserRepositoryInterface, role_repository: RoleRepositoryInterface):
        self.user_repository = user_repository
        self.role_repository = role_repository

    def create_user(self, username: str, password: str, email: str, role: str) -> User:
        role = self.role_repository.create(Role(name=role))
        user = self.user_repository.create(
            User(username=username, password=password,
                 email=email, role=role.name),
            role_id=role.id)
        return user.to_entity()

    def get_users(self) -> list[User]:
        users = self.user_repository.get_all()
        return [user.to_entity() for user in users]

    def get_user_by_username(self, username: str) -> User:
        user = self.user_repository.get_by_username(username)
        return user.to_entity()

    def get_user_by_email(self, email: str) -> User:
        user = self.user_repository.get_by_email(email)
        return user.to_entity()
