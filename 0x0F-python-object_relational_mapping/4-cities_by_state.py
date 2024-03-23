#!/usr/bin/python3
"""
cript that lists all cities from the hbtn_0e_4_usa database
"""


if __name__ == "__main__":



    import MySQLdb
    from sys import argv

    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
            passwd=argv[2], db=argv[3], charset="utf8")

    curs = conn.cursor()
    curs.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = states.id;")
    
    rows_ = cursor.fetchall()
    for row in rows_:
        print(row)
