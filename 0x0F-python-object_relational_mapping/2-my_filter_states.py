#!/usr/bin/python3
"""values in the states table of hbtn_0e_0_usa where
name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")
    cnew = conn.cursor()
    query = """
SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY states.id ASC"""
    query = query.format(argv[4])
    cnew.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cnew.close()
    conn.close()
