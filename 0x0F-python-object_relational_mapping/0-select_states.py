#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":

    #Connnecting to the db
    db = MySQLdb.connect(host="localhost", port=3306,user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    # getting a cursor->gives ability to havem multiple separate working environments through the same
    # ~connection to the db
    cur = db.cursor()

    #To execute queries, use the cursoe obj and call execute
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()