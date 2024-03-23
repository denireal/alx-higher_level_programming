#!/usr/bin/python3
"""This script displays the rows from the states table where the
state name matches the provided arguments
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=argv[1],
            passwd=argv[2],
            db=argv[3])

    curs = conn.cursor()
    curs.execute(
    "SELECT * FROM states WHERE name LIKE \
            BINARY %(name)s ORDER BY states.id ASC", {'name': argv[4]})
    rows_ = curs.fetchall()
    for row in rows_:
        print(row)
