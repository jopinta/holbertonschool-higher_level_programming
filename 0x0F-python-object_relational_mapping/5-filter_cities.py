#!/usr/bin/python3
'''testing one'''

import MySQLdb
import sys

argv = sys.argv


# Your code should not be executed when imported para que no se ejecute,
if(__name__ == '__main__'):

    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT cities.name
                FROM cities JOIN states
                ON cities.state_id=states.id
                WHERE states.name LIKE % s", [argv[4]])
    query_rows = cur.fetchall()
    lista = []
    for row in query_rows:
        lista += row
    print(", ".join(lista))
    cur.close()
    conn.close()
