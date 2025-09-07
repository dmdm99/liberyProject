import sqlite3

connect_db = sqlite3.connect("libery_DB_sqlite.db")
cursor = connect_db.cursor()




connect_db.close()