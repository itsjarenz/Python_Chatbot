import sqlite3
from sqlite3 import Error
"""http://www.sqlitetutorial.net/sqlite-python/ and youtube sentdex channel"""
def create_connection():
    database = "chatbot_db.db"
    try:
        conn = sqlite3.connect(database)
        return conn
    except Error:
        print("Error! cannot create the database connection.")
    return None
def create_table(table_name):
    c_table = """CREATE TABLE IF NOT EXISTS """ + table_name + """ (name, surname, summary, news);"""
    try:
        conn = create_connection()
        cur = conn.cursor()
        cur.execute(c_table)
    except Error:
        print("Error! cannot create that table.")
    finally:
        conn.close()
def main():
    create_table("Table Name")
    
if __name__ == '__main__':
    main()
    