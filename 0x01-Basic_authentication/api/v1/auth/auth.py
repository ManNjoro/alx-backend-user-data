#!/usr/bin/env python3
"""
manages the API authentication.
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """
    Manage API Authentication.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Check if a user is authenticated for a given endpoint.
        Args:
        path (str): The current URL being requested.
        excluded_paths (List[str]): A list of URLs that do not require
        authentication to access. If the current URL matches one in this list,
        return True.
        Returns:
        Bool: True if the user is authenticated; False otherwise.
        Raises:
        401 Unauthorized: If no auth token was provided or it's invalid.
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Gets the authorization header field from the request.
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Gets the current user
        """
        return None
