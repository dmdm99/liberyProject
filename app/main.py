import os
from fastapi import FastAPI
import factory_libery_book
import token
from app.ask_sql import permission

app = FastAPI(title="Libery API", version="1.0.0")

#1
@app.post("/auth/login")
def login(user_id: int, password: str):
     permission_login = factory_libery_book.login_check(user_id,password)
     token_login = token.create_token(user_id,permission_login)
     return #need to insert to cookies
#2
@app.get(" /items")

#3
@app.put(" /items/{id}")

#4
@app.post("/loans")

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


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", "8080")))
