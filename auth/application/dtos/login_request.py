from flask import json


class LoginRequest:
    def __init__(self, data: json):
        self.username = data.get('username')
        self.password = data.get('password')
