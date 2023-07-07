from flask import json


class LoginWithGmailRequest:
    def __init__(self, data: json):
        self.id_token = data.get('id_token')
