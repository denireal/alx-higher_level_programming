#!/usr/bin/python3
"""This script displays the rows from the states table where the
state name matches the provided arguments
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = db.cursor()
    match = sys.argv[4]
    curs.execute("SELECT * FROM states WHERE name LIKE %s", (match, ))
    rows = curs.fetchall()
    for row in rows:
        print(row)
    curs.close()
    db.close()
