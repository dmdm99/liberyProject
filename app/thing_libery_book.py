import ask_sql
from fastapi import HTTPException



# chek this exist
def login_check(user_id: int, password: str):
    user_result = ask_sql.get_user_password(password)
    if  user_result[0][0] != (user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return user_result[0][7]





