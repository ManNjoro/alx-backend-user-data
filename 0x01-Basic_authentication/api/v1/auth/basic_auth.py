#!/usr/bin/env python3
"""
Implements basic auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """
    Implementation of the basic authentication method
    """
    def extract_base64_authorization_header(
            self, authorization_header: str) -> str:
        """
        Extracts base64 encoded user and password
        from an Authorization header value
        Args:
        authorization_header (str): The HTTP Authorization header value
        Returns:
        Base64 part of the Authorization header for a Basic Authentication
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.split(" ")[0] == 'Basic':
            return None
        return authorization_header.split(" ")[1]
