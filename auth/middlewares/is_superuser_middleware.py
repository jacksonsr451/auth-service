from functools import wraps

import dotenv
import jwt
from flask import jsonify, request

from auth.infrastructure.models.role_model import RoleModel


def __decode_jwt(token, secret_key):
    try:
        decoded_token = jwt.decode(token, secret_key, algorithms=['HS256'])
        return decoded_token
    except jwt.exceptions.InvalidTokenError:
        return None


def __is_superuser(token):
    secret_key = dotenv.get_key('.env', 'SECRET_KEY')

    decoded_token = __decode_jwt(token, secret_key)
    if not decoded_token:
        return False

    role_id = decoded_token.get('role_id')
    if not role_id:
        return False

    role = RoleModel.query.get(role_id)
    if not role or role.name != 'super_admin':
        return False

    return True


def jwt_superadmin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return jsonify({'message': 'Missing token'}), 401

        if not __is_superuser(token):
            return jsonify({'message': 'Unauthorized'}), 401

        return f(*args, **kwargs)

    return decorated_function
