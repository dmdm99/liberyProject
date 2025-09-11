import sqlite3

connect_db = sqlite3.connect("app/libery_DB_sqlite.db")
cursor = connect_db.cursor()


# create table catalog_libery
cursor.execute('''
 CREATE TABLE IF NOT EXISTS catalog_libery(
  catalog_id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  author TEXT,
  publishing_year DATE,
  category TEXT CHECK(category IN ('Fantasy', 'Science Fiction', 'Romance', 'History', 'Biography', 
      'Philosophy', 'Non-Fiction', 'Religion', 'Guides', 'Children', 
      'Young Adult', 'Poetry', 'Drama', 'Thriller', 'Crime', 
      'Detective', 'Comics', 'Graphic Novels', 'Art', 'Essays', 
      'Satire', 'Popular Science', 'Health', 'Cooking', 'Travel', 
      'Adventure', 'Politics', 'Economics', 'Education', 'Society', 
      'Psychology', 'Technology', 'Medicine', 'Sports', 'Military'))
  )
''')

# create table Exist_Books
cursor.execute('''
 CREATE TABLE IF NOT EXISTS Exist_Books(
  Exist_Books_id INTEGER PRIMARY KEY AUTOINCREMENT,
  id_catalog INTEGER NOT NULL,
  type TEXT CHECK(type IN ('book','ebook', 'magazine')),
  FOREIGN KEY(id_catalog) REFERENCES catalog_libery(id)
  )
''')

# create table users
cursor.execute('''
 CREATE TABLE IF NOT EXISTS users(
   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
   First_Name TEXT,
   Last_Name TEXT,
   Adress TEXT,
   Email TEXT CHECK(email LIKE  '%_@_%.com'),
   Phone TEXT,
   Password TEXT NOT NULL CHECK(length(password) >= 8)
   )
''')

# create table User_permission
cursor.execute('''
 CREATE TABLE IF NOT EXISTS User_permission(
   user_id INTEGER PRIMARY KEY,
   permission TEXT NOT NULL CHECK(permission IN ('USER', 'ADMIN')),
   FOREIGN KEY (user_id) REFERENCES users(user_id)
   )
''')

# create table borrowed_book
cursor.execute('''
 CREATE TABLE IF NOT EXISTS borrowed_book(
   Exist_Books_id INTEGER NOT NULL,
   id_user INTEGER NOT NULL,
   Date_to_take DATE NOT NULL,
   FOREIGN KEY (id_user) REFERENCES users(user_id),
   FOREIGN KEY (Exist_Books_id) REFERENCES Exist_Books(Exist_Books_id),
   PRIMARY KEY(Exist_Books_id, id_user)
   )
''')

connect_db.commit()
connect_db.close()