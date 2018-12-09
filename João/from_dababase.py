from sqlite3 import Error
from create_database import create_connection
"""http://www.sqlitetutorial.net/sqlite-python/ and youtube sentdex channel"""
def get_from_database(table, name, surname, input_name, input_surname):
    try:
        conn = create_connection()
        cur = conn.cursor()
        if wanna know summary:
            cur.execute("""SELECT * FROM {} WHERE {} = '{}' AND {} = '{}'""".format(table, name, input_name, surname, input_surname))
            for row in c.fetchall():
                return row[2]
        elif wanna know news:
            cur.execute("""SELECT * FROM {} WHERE {} = '{}' AND {} = '{}'""".format(table, name, input_name, surname, input_surname))
            for row in c.fetchall():
                return row[3]
    except Error:
        print("Error! cannot retrieve data from the database.")
        
if __name__ == "__main__":
    get_from_database()
    