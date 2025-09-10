from datetime import datetime, timedelta
from jose import jwt, JWTError
from fastapi import HTTPException

SECRET_KEY = "dmLiberyProject"
ALGORITHM = "HS256"
TOKEN_MINUTES = 60 * 17

#create token
def create_token(user_id: int, permissions: str):
    expire = datetime.utcnow() + timedelta(TOKEN_MINUTES)
    payload = {
        "user_id": user_id,
        "permissions": permissions,
        "exp": expire
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token

#chek token is okey
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        permissions = payload.get("permissions")

        if user_id is None or permissions is None:
            raise HTTPException(status_code=401, detail="Invalid token")

        return {"user_id": user_id, "permissions": permissions}
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

