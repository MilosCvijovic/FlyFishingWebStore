import time
from typing import Dict

import jwt

from app.config import settings
from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.users.services import decodeJWT


class JWTBearer(HTTPBearer):
    """
    A custom HTTPBearer security scheme implementation that implements JWT authentication mechanism.
    """
    def __init__(self, role: str, auto_error: bool = True):
        """
        Initializes the JWTBearer class by passing the given role and auto_error to the super class HTTPBearer.

        :param role: Role of the user.
        :param auto_error: (Optional) Determines if a response with error status code should be automatically returned.
        """
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.role = role

    async def __call__(self, request: Request):
        """
         Verifies the authentication credentials of the user and returns the user's JWT if the authentication is
        successful.

        Args:
            request (Request): The incoming request to be verified.

        Returns:
            str: The JWT of the user.

        Raises:
            HTTPException: If the authentication fails.
        """
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, detail="Invalid authentication scheme.")
            payload = self.verify_jwt(credentials.credentials)
            if not payload.get("valid"):
                raise HTTPException(status_code=403, detail="Invalid token or expired token.")
            if payload.get("role") != self.role:
                raise HTTPException(status_code=403, detail="User with provided role is not permitted to access this "
                                                            "route.")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, detail="Invalid authorization code.")

    def verify_jwt(self, jwtoken: str) -> dict:
        """
        Verifies the JWT token by decoding it using the `decodeJWT` function.
        Returns a dictionary indicating if the token is valid and the user role.

        :param jwtoken: JWT token to be verified.
        :return: Dictionary indicating if the token is valid and the user role.
        """
        is_token_valid: bool = False
        try:
            payload = decodeJWT(jwtoken)
        except:
            payload = None
        if payload:
            is_token_valid = True
        return {"valid": is_token_valid, "role": payload["role"]}
