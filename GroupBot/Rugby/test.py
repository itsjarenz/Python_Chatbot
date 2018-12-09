#I used the code from Joao/create_db.db but changed it to create db for rugby in Rugby/
import sqlite3
def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except sqlite3.Error:
        print("Error! cannot create the database connection.")
    return None
def create_table(conn, table_name):
    c_table = """CREATE TABLE IF NOT EXISTS """ + table_name + """ (team, coach, captain, Location, stadium);"""
    try:
        c = conn.cursor()
        c.execute(c_table)
    except sqlite3.Error:
        print("Error! cannot create that table.")
def main():
    database = "rugby.db"
    conn = create_connection(database)
    create_table(conn,"pro14" )

main()