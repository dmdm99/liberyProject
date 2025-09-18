import ask_sql
from fastapi import HTTPException
from datetime import date, datetime
from rule import rule


# chek this exist
def login_check(user_id: int, password: str):
    user_result = ask_sql.get_user_password(password)
    if  user_result[0][0] != (user_id):
        raise HTTPException(status_code=404, detail="User not found")
    return user_result[0][7]

# how much time left from the boroow
def time_left(exit_book,user_i):
   books = ask_sql.user_borrowed(user_i)
   type_of_book = ask_sql.get_type(exit_book)
   for book in books:
       if book[1] == exit_book:
           time_to_take = datetime.strptime(book[2], "%Y-%m-%d").date()
           day_left = (date.today() - time_to_take).days
           tule_takre = rule()

           if type_of_book == 'book':
               type_this_book = tule_takre.get_book_time()
           elif type_of_book == 'magazine':
               type_this_book = tule_takre.get_Magazine_time()
           else:
               type_this_book = tule_takre.get_Ebook_time()
           if day_left < type_this_book:
               time_over = type_this_book - day_left
               return ('okey')
           else:
               return ('penalty')



