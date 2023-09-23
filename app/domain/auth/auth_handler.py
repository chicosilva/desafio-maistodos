import time
from typing import Dict, Optional

import jwt

from app.internal.config.settings import JWT_ALGORITHM, JWT_SECRET


def token_response(token: str):
    return {"access_token": token}


def decode_jwt(token: str) -> Optional[dict]:
    try:
        decoded_token = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        return decoded_token if decoded_token["expires"] >= time.time() else None
    except (jwt.exceptions.InvalidTokenError, KeyError):
        return None


def signJWT(user_id: str) -> Dict[str, str]:
    payload = {"user_id": user_id, "expires": time.time() + 3600}
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)

    return token_response(token)
