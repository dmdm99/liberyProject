import os
from urllib.request import Request
from datetime import date
from fastapi import FastAPI, Response, HTTPException
import factory_libery_book
import thing_in_token
import ask_sql

app = FastAPI(title="Libery API", version="1.0.0")

#login to system
@app.post("/auth/login")
def login(user_id: int, password: str):
     permission_login = factory_libery_book.login_check(user_id,password)
     token_login = thing_in_token.create_token(user_id,permission_login)
     response.set_cookie(key="token_login", value=f"Bearer {token_login}", httponly=True, samesite="Lax")
     return {"message": "Login successful"}

#find book spsific
@app.get(" /items")
def items(request: Request, catalog_id: int, title: str, author: str, publishing_year: date, category: str, type: str):
    thing_in_token.verify_token(request)
    return ask_sql.book_free(catalog_id, title, author, publishing_year, category, type)

#Extending the borrow
@app.put(" /items/{id}")
def change_date(request: Request):
    current_user = thing_in_token.verify_token(request)
    if current_user["permissions"] != 'ADMIN':
        raise HTTPException(status_code=401, detail="Bad permission")

    ask_sql.chenge_borrow(id,date.today())

#4
@app.post("/loans")
def new_borrowed_book(request: Request, user_id: int, Exist_Books_id: int):
    current_user = thing_in_token.verify_token(request)

    ask_sql.new_borrow(Exist_Books_id, user_id, date.today())

#5
@app.patch("/loans/{id}")

#6
@app.post("/users")

#7
@app.get("/users")

#8
@app.get("/users/{id}")

#9
@app.patch("/users/{id}")

#10
@app.delete("/users/{id}")
def g():
     return {}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
