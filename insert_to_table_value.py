import sqlite3

conect_db = sqlite3.connect("app/libery_DB_sqlite.db")
cursor = conect_db.cursor()

# insert example into catalog_libery
cursor.execute('''
INSERT INTO catalog_libery (title, author, publishing_year, category)
VALUES ('My Book', 'John Doe', '2025-01-01', 'Fantasy')
''')


# insert example into Exist_Books
cursor.execute('''
INSERT INTO Exist_Books (Exist_Books_id, id_catalog, type)
VALUES (1,1,'book')
''')

# insert example into users
cursor.execute('''
INSERT INTO users (First_Name, Last_Name, Adress, Email, Phone, Password)
VALUES ('Alice', 'Smith', '123 Street', 'a@b.com', '0501234567', 'password123')
''')

# insert example into User_permission
cursor.execute('''
INSERT INTO User_permission (user_id, permission)
VALUES (1, 'USER')
''')

# insert example into borrowed_book
cursor.execute('''
INSERT INTO borrowed_book (Exist_Books_id, id_user, Date_to_take,pay)
VALUES (1, 1, '2025-09-07','okey')
''')
cursor.execute('''
INSERT INTO borrowed_book (Exist_Books_id, id_user, Date_to_take,pay)
VALUES (2, 2, '2025-09-07','okey')
''')

conect_db.commit()
conect_db.close()
