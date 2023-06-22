#!/usr/bin/python3
"""
This script selects all states starting with N
from a database
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user="{}".format(sys.argv[1]),
                         passwd="{}".format(sys.argv[2]),
                         db="{}".format(sys.argv[3]))

    cur = db.cursor()
    cur.execute("""
                SELECT * FROM states
                WHERE REGEXP_LIKE(name, '^N' COLLATE utf8mb4_0900_as_cs)
                ORDER BY states.id
                """)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
