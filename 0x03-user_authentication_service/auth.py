#!/usr/bin/env python3
"""
auth module
"""


def _hash_password(password: str) -> bytes:
    """
    Hash a password using the bcrypt algorithm
    :param password: The plain text password to hash.
    :return: A byte string of the hashed password.
    """
    import bcrypt
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt)
