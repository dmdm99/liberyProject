import os
from datetime import date
from fastapi import FastAPI, Request,Response , HTTPException
import thing_libery_book
import thing_in_token
import ask_sql

app = FastAPI(title="Libery API", version="1.0.0")

#login to system
@app.post("/auth/login")
def login(response: Response, user_id: int, password: str):
     permission_login = thing_libery_book.login_check(user_id,password)
     token_login = thing_in_token.create_token(user_id,permission_login)
     response.set_cookie(key="token_login", value=f"Bearer {token_login}", httponly=True, samesite="Lax")
     return {"message": "Login successful"}

#find book spsific
@app.get("/items")
def items(request: Request, catalog_id: int, title: str, author: str, publishing_year: date, category: str, type_of_this: str):
    thing_in_token.verify_token(request)
    return ask_sql.book_free(catalog_id, title, author, publishing_year, category, type_of_this)

#Extending the borrow
@app.put("/items/{id}")
def change_date(id: int,request: Request):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    if ask_sql.get_type(id) != 'book' or ask_sql.get_type(id) != 'magazine':
        raise HTTPException(status_code=401, detail="Bad options")
    ask_sql.chenge_borrow(id,date.today())

#create a new borrow
@app.post("/loans")
def new_borrowed_book(request: Request, user_id: int, Exist_Books_id: int):
    thing_in_token.verify_token(request)
    if ask_sql.get_type(id) != 'ebook':
        raise HTTPException(status_code=401, detail="Bad options")
    ask_sql.new_borrow(Exist_Books_id, user_id, date.today())

#delete borrow
@app.patch("/loans/{id}")
def delete_borrow(id: int,request: Request, Exist_Books_id: int):
    current_user = thing_in_token.verify_token(request)
    if ask_sql.get_type(Exist_Books_id) != 'ebook':
        if current_user["permissions"] != 'ADMIN':
            raise HTTPException(status_code=401, detail="Bad permission")
    ask_sql.delete_borrow(id, Exist_Books_id)

#create a new user
@app.post("/users")
def new_user(request: Request, first_name: str, last_name: str,addres: str, emaill: str, phone: str, password: str, permission: str):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    new_user_id = ask_sql.add_user(first_name, last_name, addres, emaill, phone, password, permission)
    return new_user_id

#comeback all users
@app.get("/users")
def all_users(request: Request):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    return ask_sql.get_all_users()

#from id to all informition abut this user
@app.get("/users/{id}")
def spesific_user(id: int,request: Request):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    idd = int(id)
    user_g = ask_sql.get_user_id(idd)
    return user_g



#change permission to the user
@app.patch("/users/{id}")
def change_permission(id: int,request: Request, permission: str):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    ask_sql.permission(id, permission)

#10
@app.delete("/users/{id}")
def delete_user(id: int,request: Request):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")
    ask_sql.delete_users(id)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
