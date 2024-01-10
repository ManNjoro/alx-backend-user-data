#!/usr/bin/env python3
"""
Password encryption
"""

import bcrypt


def hash_password(password: str) -> str:
    """Hash a password using the bcrypt algorithm."""
    salt = bcrypt.gensalt()  # Generate a random salt
    return bcrypt.hashpw(password.encode('utf-8'), salt)
