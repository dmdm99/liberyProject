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
   user_id = cursor.lastrowid
   cursor.execute('''INSERT INTO User_permission (user_id, permission) 
                      VALUES (?,?)''', (user_id, permission,)
                  )
   connect_db.commit()
   connect_db.close()
   return user_id

#add new borrow
def new_borrow(Exist_Books_id, user_id, date):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''INSERT INTO borrowed_book (Exist_Books_id, id_user, Date_to_take) 
                  VALUES (?,?,?)''', (Exist_Books_id, user_id, date,))
   connect_db.commit()
   connect_db.close()

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


# CHANGE
#change permission
def permission(user_id, permission_change):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''UPDATE User_permission SET permission = ? WHERE user_id = ?''', (permission_change, user_id,))
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
#get user spechific from id
def get_user_id(user_id):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''SELECT users.* ,User_permission.permission FROM users 
                    INNER JOIN User_permission ON users.user_id = User_permission.user_id 
                    WHERE users.user_id = ?''', (user_id,))
   result = cursor.fetchall()
   connect_db.close()
   return result

#get user spechific password
def get_user_password(Password):
   connect_db = get_connection()
   cursor = connect_db.cursor()
   cursor.execute('''SELECT users.* ,User_permission.permission FROM users 
                    INNER JOIN User_permission ON users.user_id = User_permission.user_id 
                    WHERE users.Password = ?''', (Password,))
   result = cursor.fetchall()
   connect_db.close()
   return result

#get all user
def get_all_users():
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT users.user_id, users.First_Name, users.Last_Name, users.Adress, users.Email, users.Phone, users.Password, User_permission.permission FROM users 
                   INNER JOIN User_permission ON users.user_id = User_permission.user_id ''')
    result = cursor.fetchall()
    connect_db.close()
    return result

#get spesific book free
def book_free(catalog_id=None, title="", author="", publishing_year="", category="", type_of_this=""):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT catalog_libery.*, Exist_Books.Exist_Books_id, Exist_Books.type FROM catalog_libery 
                   LEFT JOIN Exist_Books ON catalog_libery.catalog_id = Exist_Books.id_catalog
                   WHERE (catalog_libery.catalog_id = ? )
                   AND (catalog_libery.title = ? OR ? = '')
                   AND (catalog_libery.author = ? OR ? = '')
                   AND (catalog_libery.publishing_year = ? OR ? = '')
                   AND (catalog_libery.category = ? OR ? = '') 
                   AND (Exist_Books.type = ? OR ? = '')
                   AND Exist_Books.Exist_Books_id NOT IN ( SELECT Exist_Books_id FROM borrowed_book)
                   ''', (catalog_id,
                         title, title,
                         author, author,
                         publishing_year, publishing_year,
                         category, category,
                         type_of_this, type_of_this, ))
    result = cursor.fetchall()
    connect_db.close()
    return result

#get book borrowed by user spesific
def user_borrowed(user_id):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT * FROM borrowed_book where id_user = ?''', (user_id,))
    result = cursor.fetchall()
    connect_db.close()
    return result

#get type from id
def get_type(Exist_Books_id):
    connect_db = get_connection()
    cursor = connect_db.cursor()
    cursor.execute('''SELECT Exist_Books.TYPE
                   FROM borrowed_book INNER JOIN Exist_Books
                   ON borrowed_book.Exist_Books_id = Exist_Books.Exist_Books_id 
                   WHERE Exist_Books.Exist_Books_id = ?''', (Exist_Books_id,))
    result = cursor.fetchall()
    connect_db.close()
    return result


