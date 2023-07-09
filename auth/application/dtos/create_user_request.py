from flask import json


class CreateUserRequest:
    def __init__(self, data: json):
        self.username = data.get('username')
        self.password = data.get('password')
        self.email = data.get('email')
        self.role = data.get('role')
