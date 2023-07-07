from auth.application.dtos.user_dto import UserDTO


class GetUsersResponse:
    def __init__(self, users):
        self.users = users

    def to_dict(self):
        return {
            'users': [
                UserDTO(username=user.username, email=user.email)
                for user in self.users
            ]
        }
