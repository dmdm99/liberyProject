import ask_sql
from fastapi import HTTPException

# chek this exist
def login_check(user_id: int, password: str):
    result = ask_sql.get_user_password(password)
    user_result = result[0]
    if not result  or user_result[0] == int(user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return user_result[7]

#