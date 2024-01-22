#!/usr/bin/env python3
"""
auth module
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound


def _hash_password(password: str) -> bytes:
    """
    Hash a password using the bcrypt algorithm
    :param password: The plain text password to hash.
    :return: A byte string of the hashed password.
    """
    import bcrypt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        """
        Constructs an instance of the Auth class.
        """
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Registers a new user in the users table and returns it.
        """
        try:
            existing_user = self._db.find_user_by(email=email)
            if existing_user:
                raise ValueError("User {} already exists.".format(email))
        except NoResultFound:
            hashed_password = _hash_password(password)
            user = self._db.add_user(
                email=email, hashed_password=hashed_password)
            return user
