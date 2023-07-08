from auth.application.dtos.user_dto import UserDTO
from auth.domain.roles.role import Role
from auth.domain.roles.role_repository_interface import RoleRepositoryInterface
from auth.domain.users.user import User
from auth.domain.users.user_repository_interface import UserRepositoryInterface
from auth.domain.users.user_services_interface import UserServiceInterface


class UserService(UserServiceInterface):
    def __init__(
        self,
        user_repository: UserRepositoryInterface,
        role_repository: RoleRepositoryInterface,
    ):
        self.user_repository = user_repository
        self.role_repository = role_repository

    def create_user(
        self, username: str, password: str, email: str, role: str
    ) -> UserDTO:
        role = self.role_repository.create(Role(name=role))
        user = self.user_repository.create(
            User(
                username=username,
                password=password,
                email=email,
                role=role.name,
            ),
            role_id=role.id,
        )
        return user.to_dto()

    def get_users(self) -> list[UserDTO]:
        users = self.user_repository.get_all()
        return [user.to_dto() for user in users]

    def get_user_by_username(self, username: str) -> UserDTO:
        user = self.user_repository.get_by_username(username)
        return user.to_dto()

    def get_user_by_email(self, email: str) -> UserDTO:
        user = self.user_repository.get_by_email(email)
        return user.to_dto()
