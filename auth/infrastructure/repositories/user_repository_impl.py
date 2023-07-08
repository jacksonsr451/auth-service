from auth.domain.users.user_repository_interface import UserRepositoryInterface
from auth.infrastructure.adapters.database import session
from auth.infrastructure.models.user_model import UserModel


class UserRepositoryImpl(UserRepositoryInterface):

    def create(self, user: UserModel) -> UserModel:
        session.add(user)
        session.commit()
        return user

    def get_all(self) -> list[UserModel]:
        return session.query(UserModel).all()

    def get_by_username(self, username: str) -> UserModel | None:
        return session.query(UserModel).filter_by(username=username).first()

    def get_by_email(self, email: str) -> UserModel | None:
        return session.query(UserModel).filter_by(email=email).first()
