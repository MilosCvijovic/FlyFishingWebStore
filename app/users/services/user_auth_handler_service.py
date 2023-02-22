import time
from typing import Dict
import jwt
from app.config import settings


USER_SECRET = settings.USER_SECRET
JWT_ALGORITHM = settings.ALGORITHM


def signJWT(user_id: str, role: str) -> Dict[str, str]:
    """This function creates a JSON Web Token (JWT) to be used as an access token for authentication purposes.

    :param user_id: The unique identifier of the user.
    :param role: The role of the user.
    :return: A dictionary containing the JWT as the "access_token" key value."""
    payload = {
        "user_id": user_id,
        "role": role,
        "expires": time.time() + 1200
    }
    token = jwt.encode(payload, USER_SECRET, algorithm=JWT_ALGORITHM)

    return {"access_token": token}


def decodeJWT(token: str) -> dict:
    """This function decodes the JWT and returns the claims contained in it, if the token has not expired.

    :param token: The JWT to be decoded.
    :return: A dictionary containing the claims in the JWT, or an empty dictionary if the
    token is invalid or expired."""
    try:
        decoded_token = jwt.decode(token, USER_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except:
        return {}
