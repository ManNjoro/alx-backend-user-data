#!/usr/bin/env python3
"""
Password encryption
"""

import bcrypt


def hash_password(password: str) -> bytes:
    """Hash a password using the bcrypt algorithm."""
    salt = bcrypt.gensalt()  # Generate a random salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Check if a plaintext password matches a stored hashed password."""
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password)
