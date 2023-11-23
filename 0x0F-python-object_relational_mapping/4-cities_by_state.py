#!/usr/bin/python3
"""
Module akes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(argv) != 4:
        print("Usage: {} username password database_name".format(argv[0]))
        exit(1)

    # Connnecting to the db
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=argv[1], passwd=argv[2], db=argv[3])

    # getting a cursor->gives ability to havem multiple separate
    # working environments through the same
    # ~connection to the db
    cur = db.cursor()

    # To execute queries, use the cursor obj and call execute
    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        LEFT JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
