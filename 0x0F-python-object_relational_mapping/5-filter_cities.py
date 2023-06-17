#!/usr/bin/python3
"""
This script takes in the name of a state as
an argument and lists all cities of that state
"""


import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user="{}".format(sys.argv[1]),
                         passwd="{}".format(sys.argv[2]),
                         db="{}".format(sys.argv[3]))

    cur = db.cursor()
    cur.execute("""SELECT cities.name
                    FROM cities
                    JOIN states
                    ON states.id = cities.state_id
                    WHERE states.name = %s
                    ORDER BY cities.id;""", ([sys.argv[4]], ))
    rows = cur.fetchall()
    for i in range(len(rows)):
        if i == (len(rows) - 1):
            print("{}".format(str(rows[i]).strip("(),'")), end='')
        else:
            print("{}, ".format(str(rows[i]).strip("(),'")), end='')
    print()

    cur.close()
    db.close()
