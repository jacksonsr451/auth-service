from auth.domain.user import User
from auth.domain.user_repository_interface import UserRepositoryInterface
from auth.infrastructure.adapters.database import db


class UserRepositoryImpl(UserRepositoryInterface):
    def create(self, user: User) -> User:
        cursor = db.connection.cursor()
        cursor.execute(
            'INSERT INTO users (username, password, email) VALUES (?, ?, ?)',
            (user.username, user.password, user.email),
        )
        db.connection.commit()
        return user

    def get_all(self) -> list[User]:
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM users')
        rows = cursor.fetchall()
        users = [
            User(username=row[1], password=row[2], email=row[3])
            for row in rows
        ]
        return users

    def get_by_username(self, username: str) -> User | None:
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE username=?', (username,))
        row = cursor.fetchone()
        if row:
            return User(username=row[1], password=row[2], email=row[3])
        return None

    def get_by_email(self, email: str) -> User | None:
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE email=?', (email,))
        row = cursor.fetchone()
        if row:
            return User(username=row[1], password=row[2], email=row[3])
        return None
