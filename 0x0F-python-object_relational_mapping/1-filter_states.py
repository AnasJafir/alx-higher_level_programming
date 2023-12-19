#!/usr/bin/python3
"""List all states from a database"""


import MySQLdb
from sys import argv


if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )
    cursor = connection.cursor()
    query = "SELECT * FROM states ORDER BY id;"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        if row[1].startswith("N"):
            print(row)
    cursor.close()
    connection.close()
