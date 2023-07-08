from auth.domain.roles.role_enum import RoleEnum


class Role:
    def __init__(self, name):
        self.name = self.__validate_role(name=name)

    class Config:
        validate_assignment = True

    def __validate_role(self, name) -> str:
        valid_names = [role.value for role in RoleEnum]
        if name not in valid_names:
            raise ValueError('Invalid role')
        return name
