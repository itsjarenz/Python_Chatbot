import sqlite3
from sqlite3 import Error
from create_database import create_connection
"""Got part of the code from http://www.sqlitetutorial.net/sqlite-python/ and youtube sentdex channel"""
def add_info(conn, column, valor):
    sql = """ INSERT INTO sports_table(name, surname, sport, summary, news)
              VALUES(?,?,?,?,?)"""
    cur = conn.cursor()
    if column == "name":
        valor2 = (valor, "", "", "", "")
    elif column == "surname":
        valor2 = ("", valor, "", "", "")
    elif column == "sport":
        valor2 = ("", "", valor, "", "")
    elif column == "summary":
        valor2 = ("", "", "", valor, "")
    else:
        valor2 = ("", "", "", "", valor)
    cur.execute(sql, valor2)
    conn.commit()
def main():
    database = "chatbot_db.db"
    conn = create_connection(database)
    add_info(conn, "name", "João")
if __name__ == "__main__":
    main()