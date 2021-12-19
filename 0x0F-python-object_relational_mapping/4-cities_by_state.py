#!/usr/bin/python3
'''testing one'''

import MySQLdb
import sys

argv = sys.argv

# Create states table in hbtn_0e_0_usa with some data

if(__name__ == '__main__'):

    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3], charset="utf8")

    cur = conn.cursor()

    cur.execute("SELECT cities.name, states.name, cities.id\
                FROM cities JOIN states ON cities.state_id = states.id;")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
