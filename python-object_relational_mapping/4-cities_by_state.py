#!/usr/bin/python3
"""Lists all cities with their corresponding state names."""

import MySQLdb
import sys


def list_cities(username, password, database):
    """Connects to MySQL database and displays cities by state."""
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
        charset="utf8"
    )

    cur = conn.cursor()

    cur.execute("""
        SELECT cities.id, cities.name, states.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """)

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    list_cities(sys.argv[1], sys.argv[2], sys.argv[3])
