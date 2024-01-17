#!/usr/bin/env python3
"""
Implements session authentication
"""

import uuid
from api.v1.auth.auth import Auth


class SessionAuth(Auth):
    """Session Authentication Class."""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """Create a new API session for the given user ID and return its
        unique identifier (UUID string)
        Args:
        user_id: The user's unique identifier. Defaults to `None`.
        Returns:
        A UUID string representing the newly-created session's
        unique identifier.
        """
        if user_id is None:
            return None
        if not isinstance(user_id, str):
            return None
        unique_id = str(uuid.uuid4())
        self.user_id_by_session_id[unique_id] = user_id
        return unique_id
