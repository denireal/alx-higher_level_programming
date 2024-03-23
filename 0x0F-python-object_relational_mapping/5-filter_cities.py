#!/usr/bin/python3
"""Script that list all cities of a state
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        try:
            database = MySQLdb.connect(
                    host="localhost",
                    port=3306,
                    user=sys.argv[1],
                    passwd=sys.argv[2],
                    db=sys.argv[3])
            cursor = database.cursor()
            # Using parameterized query to prevent SQL injection
            cursor.execute("SELECT cities.name FROM cities\
                    JOIN states ON cities.state_id = states.id\
                    AND states.name = %s\
                    ORDER BY cities.id ASC", (sys.argv[4],))

            rows_data = cursor.fetchall()
            cities = [row[0] for row in rows_data]
            print(", ".join(cities))
            cursor.close()
            database.close()
        except MySQLdb.Error as error:
                print("MySQL Error:", error)
    else:
        print("Usage: {} <username> <password> <database> <state>".format(sys.argv[0]))
