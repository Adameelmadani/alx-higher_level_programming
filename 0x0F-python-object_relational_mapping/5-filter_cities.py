#!/usr/bin/python3
"""
This is our module
"""
import MySQLdb
import sys


if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                           passwd=sys.argv[2], db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name FROM cities WHERE cities.state_id =\
                 (SELECT states.id FROM states WHERE states.name = \'{}\')\
                 ORDER BY cities.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for i in range(0, len(rows)):
        print("{}".format(rows[i][0]), end="")
        if i != len(rows) - 1:
            print(", ", end="")
    print("")
