#!/usr/bin/env python3
"""This script selects all states from
a database
"""

import sys
import MySQLdb


db = MySQLdb.connect(host="localhost", user="{}".format(sys.argv[1]),
                     passwd="{}".format(sys.argv[2]),
                     db="{}".format(sys.argv[3]))

cur = db.cursor()

cur.execute("SELECT * FROM states")
rows = cur.fetchall()
for row in rows:
    print(row)
