import sqlite3
from sqlite3 import Error
from create_database import create_connection
"""http://www.sqlitetutorial.net/sqlite-python/ and youtube sentdex channel"""
def add_new_info(table_name, name, surname, wikia, news):
    try:
        conn = create_connection()
        cur = conn.cursor()
        sql = ''' INSERT INTO ''' + table_name + ''' (name, surname, summary, news) VALUES(?,?,?,?)'''
        valor = (name, surname, wikia, news) #still need to assign the variables
        cur.execute(sql, valor)
        conn.commit()
    except Error:
        print("Error! cannot add new info to the database.")
def main():
    table_name = "Sport"
    name = "Name"
    surname = "Surname"
    wikia = "Info"
    news = "News"
    add_new_info(table_name, name, surname, wikia, news)

if __name__ == "__main__":
    main()
    