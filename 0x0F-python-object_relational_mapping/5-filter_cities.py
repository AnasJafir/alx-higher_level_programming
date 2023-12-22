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
        db=argv[3],
    )
    cursor = connection.cursor()
    query = """SELECT cities.id, cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC
            """
    cursor.execute(query, (argv[4], ))
    rows = cursor.fetchall()
    for i, row in enumerate(rows):
        print(row[1], end='')
        if i < len(rows) - 1:
            print(', ', end='')
    print()
    cursor.close()
    connection.close()
