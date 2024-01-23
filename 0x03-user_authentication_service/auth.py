#!/usr/bin/env python3
"""
auth module
"""
from db import DB
from user import User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """
    Hash a password using the bcrypt algorithm
    :param password: The plain text password to hash.
    :return: A byte string of the hashed password.
    """
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def _generate_uuid() -> str:
    """
    Generates a unique UUID.
    Returns:
    A string representation of a UUID4.
    """
    return str(uuid.uuid4())


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

    def valid_login(self, email: str, password: str) -> bool:
        """Checks whether login credentials are correct or not.
        Args:
        email (str): The email address of the user attempting to log in.
        password (str): The password provided by the user.
        Returns:
        True if the login is successful, False otherwise.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                return bcrypt.checkpw(
                    password.encode('utf-8'), user.hashed_password)
        except Exception:
            return False

    def create_session(self, email: str) -> str:
        """Creates a session token for a given user's email.
        Args:
        email (str): The email address of the user logging in.
        Returns:
        A new session token as a string.
        """
        try:
            user = self._db.find_user_by(email=email)
            if user:
                session_id = _generate_uuid()
                self._db.update_user(user.id, session_id=session_id)
                return session_id
        except Exception:
            return None
