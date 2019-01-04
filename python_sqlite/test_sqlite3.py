        # db_utils.py
import os  
import sqlite3

def db_connect(db_path):  
    con = sqlite3.connect(db_path)
    return con

if __name__ == '__main__':
    try:
        # create a default path to connect to and create (if necessary) a database
        # called 'database.sqlite3' in the same directory as this script
        DEFAULT_PATH = os.path.join(os.path.dirname(__file__), 'database.sqlite3')
        conn = db_connect(DEFAULT_PATH)
        cur = conn.cursor()
        cur.execute('Select * from IOTDHTData')
        results = cur.fetchall()
        for row in results:
            print(row)
  
    except Exception as e:
        print(str(e))