from auth.application.dtos.user_dto import UserDTO


class GetUsersResponse:
    def __init__(self, users: list[UserDTO]) -> None:
        self.users = users

    def to_dict(self):
        return {
            'users': [
                {
                    'username': user.username,
                    'email': user.email,
                    'role_id': user.role_id,
                }
                for user in self.users
            ]
        }
