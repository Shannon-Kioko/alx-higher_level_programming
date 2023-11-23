#!/usr/bin/python3
"""
Module lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":

    # Connnecting to the db
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3])

    # getting a cursor->gives ability to havem multiple separate
    # working environments through the same
    # ~connection to the db
    cur = db.cursor()

    # To execute queries, use the cursor obj and call execute
    cur.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
