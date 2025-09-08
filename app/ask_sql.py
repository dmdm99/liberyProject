import sqlite3

def get_connection():
  connect_db = sqlite3.connect("libery_DB_sqlite.db")
  return connect_db

# ADD
#add user to data + permission
def add_user(first_name, last_name, addres, emaill, phone, password, permission):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''INSERT INTO USERS (First_Name, Last_Name, Adress, Email, Phone, Password) 
                   VALUES (?,?,?,?,?,?)''', (first_name, last_name, addres, emaill, phone, password,)
                  )
   cursor.execute('''INSERT INTO User_permission (user_id, permission) 
                      VALUES (?,?)''', (cursor.lastrowid, permission,)
                  )
   connect_db.commit()
   connect_db.close()

#add new borrow
def new_borrow(Exist_Books_id, user_id, date):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''INSERT INTO borrowed_book (Exist_Books_id, id_user, Date_to_take) 
                  VALUES (?,?,?)''', (Exist_Books_id, user_id, date,))


#  DELETE
#delete borrow
def delete_borrow(ID_user,id_book):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''DELETE FROM borrowed_book WHERE id_user = ? AND Exist_Books_id = ?''', (ID_user,id_book,))
   connect_db.commit()
   connect_db.close()

#delete user
def delete_users(user_id):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''DELETE FROM users WHERE user_id = ?''', (user_id,))
    connect_db.commit()
    connect_db.close()


# CANGE
#change permission
def permission(user_id, permission_change):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''UPDATE users SET permission = ? WHERE user_id = ?''', (permission_change, user_id,))
   connect_db.commit()
   connect_db.close()


#change borrow
def chenge_borrow(Exist_Books_id,new_date):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''UPDATE borrowed_book SET Date_to_take = ? WHERE Exist_Books_id = ?''', (new_date, Exist_Books_id,))
   connect_db.commit()
   connect_db.close()

#FINND SAMTING
#get user spechific
def get_user(user_id):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''SELECT * FROM users 
                  LEFT JOIN User_permission ON users.user_id = User_permission.user_id 
                  WHERE users.user_id = ?''', (user_id,))
   result = cursor.fetchall()
   connect_db.close()
   return result

#get all user
def get_all_users():
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT * FROM users 
        LEFT JOIN User_permission ON users.user_id = User_permission.user_id ''')
    result = cursor.fetchall()
    connect_db.close()
    return result

#get spsific book free
def book_free(catalog_id):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT * FROM Exist_Books WHERE catalog_id = ? 
                   AND Exist_Books_id NOT IN ( SELECT Exist_Books_id FROM borrowed_book)
                   ''', (catalog_id,))
    result = cursor.fetchall()
    return result

#get book borrowed by user spsific
def user_borrowed(user_id):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT * FROM borrowed_book where id_user = ?''', (user_id,))
    result = cursor.fetchall()
    return result





