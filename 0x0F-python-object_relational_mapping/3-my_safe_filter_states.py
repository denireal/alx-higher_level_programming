#!/usr/bin/python3
"""This script displays the rows from the states table where the
state name matches the provided arguments
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = db.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    curs = db_connect.cursor()
    curs.execute(
    "SELECT * FROM states WHERE name LIKE %s
            ORDER BY states.id ASC", (argv[4],))
    rows_ = curs.fetchall()
    for row in rows_:
        print(row)
