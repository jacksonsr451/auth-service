import click
from flask import Flask
from flask.cli import AppGroup
from werkzeug.security import generate_password_hash


from auth.application.services.user_service import UserService
from auth.infrastructure.repositories.role_repository_impl import \
    RoleRepositoryImpl
from auth.infrastructure.repositories.user_repository_impl import \
    UserRepositoryImpl


def init_app(app: Flask):
    superuser_cli = AppGroup('superuser', help='Create a super user')

    @superuser_cli.command('create')
    @click.option('--username', prompt='Username', help='Super user username')
    @click.option('--email', prompt='Email', help='Super user email')
    @click.option(
        '--password',
        prompt='Password',
        hide_input=True,
        confirmation_prompt=True,
        help='Super user password',
    )
    def create_superuser(username, email, password):
        UserService(UserRepositoryImpl(), RoleRepositoryImpl()).create_user(
            username=username,
            email=email,
            password=generate_password_hash(password),
            role='super_admin',
        )
        print(
            f'Super user created successfully! Username: {username}, Email: {email}'
        )

    app.cli.add_command(superuser_cli)
