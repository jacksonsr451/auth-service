from datetime import datetime, timedelta

import dotenv
import jwt
from flask import Blueprint, request
from google.auth.transport import requests as google_requests
from werkzeug.security import check_password_hash, generate_password_hash

from auth.application.dtos.create_user_request import CreateUserRequest
from auth.application.dtos.create_user_response import CreateUserResponse
from auth.application.dtos.get_users_response import GetUsersResponse
from auth.application.dtos.login_request import LoginRequest
from auth.application.dtos.login_response import LoginResponse
from auth.application.dtos.login_with_gmail_request import \
    LoginWithGmailRequest
from auth.application.services.user_service import UserService
from auth.infrastructure.repositories.role_repository_impl import RoleRepositoryImpl
from auth.infrastructure.repositories.user_repository_impl import \
    UserRepositoryImpl

auth_bp = Blueprint('auth', __name__)

dotenv.load_dotenv()

user_service = UserService(UserRepositoryImpl(), RoleRepositoryImpl())


@auth_bp.route('/users', methods=['GET'])
def get_users():
    return GetUsersResponse(users=user_service.get_users()).to_dict()


@auth_bp.route('/users', methods=['POST'])
def create_user():
    data = CreateUserRequest(data=request.get_json())
    hashed_password = generate_password_hash(data.password)
    user = user_service.create_user(
        data.username, hashed_password, data.email, data.role
    )
    return CreateUserResponse(
        username=user.username, email=user.email
    ).to_dict()


@auth_bp.route('/login', methods=['POST'])
def login():
    data = LoginRequest(data=request.get_json())

    if data.username.endswith('@gmail.com'):
        user = user_service.get_user_by_email(data.username)
        if user and check_password_hash(user.password, data.password):
            token = generate_token(user.username)
            return LoginResponse(token=token).to_dict()
    else:
        user = user_service.get_user_by_username(
            data.username)
        if user and check_password_hash(user.password, data.password):
            token = generate_token(user.username)
            return LoginResponse(token=token).to_dict()

    return {'error': 'Invalid username or password'}, 401


@auth_bp.route('/login-with-gmail', methods=['POST'])
def login_with_gmail():
    data = LoginWithGmailRequest(data=request.get_json())

    try:
        token_info = verify_google_token(data.id_token)
        email = token_info.get('email')
        username = email.split('@')[0]
        user = user_service.get_user_by_email(email)

        if not user:
            password = generate_password_hash('gmailuser')
            user = user_service.create_user(
                username, password, email)

        token = generate_token(username)
        return LoginResponse(token=token).to_dict()

    except ValueError:
        return {'error': 'Invalid Google token'}, 401


def verify_google_token(id_token):
    return id_token.verify_oauth2_token(
        id_token,
        google_requests.Request(),
        dotenv.get_key('.env', 'GOOGLE_CLIENT_ID'),
    )


def generate_token(username):
    payload = {
        'username': username,
        'exp': datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(
        payload, dotenv.get_key('.env', 'SECRET_KEY'), algorithm='HS256'
    )
    return token.decode('utf-8')
