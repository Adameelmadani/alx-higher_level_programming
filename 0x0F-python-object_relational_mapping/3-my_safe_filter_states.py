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
    if 'TRUNCATE' in sys.argv[4]:
        cur.close()
        conn.close()
        exit()
    cur.execute("SELECT * FROM states WHERE BINARY states.name = \'{}\' ORDER\
                 BY states.id ASC".format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
