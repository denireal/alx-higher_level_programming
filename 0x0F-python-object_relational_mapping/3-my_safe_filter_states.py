#!/usr/bin/python3
"""This script displays the rows from the states table where the
state name matches the provided argument."""

import MySQLdb
import sys


def display_matching_states():
    """This function takes command-line arguments to filter and
    display states from the database based on the provided state name.

        Arguments:
                sys.argv[1]: MySQL username
                sys.argv[2]: MySQL password
                sys.argv[3]: Database name
                sys.argv[4]: State name
                """
                if len(sys.argv) != 5:
                    print("Usage: python3 script.py <username> <password> <database_name> <state_name>")
                    return
                try:
                    # Connect to the MySQL database
                    conn = MySQLdb.connect(
                            host="localhost",
                            port=3306,
                            user=sys.argv[1],
                            passwd=sys.argv[2],
                            db=sys.argv[3]
                            )
                    cur = conn.cursor()

                    # Use a parameterized query to prevent SQL injection
                    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
                    cur.execute(query, (sys.argv[4],))

                    # Fetch and display the matching rows
                    rows = cur.fetchall()
                    for r in rows:
                        print(r)
                        except MySQLdb.Error as e:
                            print("Error:", e)
                            finally:
                                                                                                                                                                                                # Close the cursor and database connection
                        if cur:
                            cur.close()
                                                                                                                                                                                                    if conn:
                            conn.close()

                            if __name__ == "__main__":
                                display_matching_states()
