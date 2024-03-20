#!/usr/bin/python3
"""
Displays all values in the states table of
hbtn_0e_0_usa where name matches the argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    # Connecting MySQL DB
     conn = MySQLdb.connect(
             host="localhost",
             user=sys.argv[1],
             passwd=sys.argv[2],
             db=sys.argv[3],
             port=3306
             )

     # Create object to execute queries
     cursor = connection.cursor()

         # Prepare and execute the SQL query
         query = """SELECT * FROM states
         WHERE name LIKE BINARY %s
         ORDER BY id ASC"""

         name_to_match = (sys.argv[4],)
         cursor.execute(query, name_to_match)

         # Fetch and print the results
         results = cursor.fetchall()
         for row in results:
            print(row)

            # Close the cursor and connection
            cursor.close()

            conn.close()
