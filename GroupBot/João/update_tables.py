import sqlite3
from sqlite3 import Error
from create_database import create_connection
"""http://www.sqlitetutorial.net/sqlite-python/ and youtube sentdex channel"""
def update_task(table_name, task):
    try:
        conn = create_connection()
        cur = conn.cursor()
        sql = ''' UPDATE {} SET summary = ? , news = ? WHERE name = ? AND surname = ?'''.format(table_name)
        cur.execute(sql, task)
        conn.commit()
    except Error:
        print("Error! cannot update data into the database.")
def main():
    update_task("sport", ("info", "news", "name", "surname"))

if __name__ == '__main__':
    main()
    